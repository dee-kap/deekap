---
title: 'Capture XML in WCF Service'
date: Tue, 07 Jan 2014 10:16:00 +0000
draft: false
tags: ['.NET']
---

Working on a project where we wrote WCF Services a need was identified to capture the raw xml passed in to the service operation and also capture the reply xml sent back by the service. WCF does not provide such facility out of the box but it can be easily implemented using behaviours. In this article we will look at how to capture raw xml messages when a call is made to a service. As an example we will create a simple service which implements one operation called SayHello. Our service contract will look like this.```
 [ServiceContract]
public interface IHelloService
{ 
  [OperationContract] 
  string SayHello(string name);
} 
```In the operation “SayHello” we will return a string. Here is the implementation of IHelloService contract.```
 public class HelloService : IHelloService
{  
  public string SayHello(string name) 
  { 
    return string.Concat("Hello ", name); 
  }
} 
```We will host our Service In a Windows Forms application so that we can easily view xml we capture. Just to get a feel for it, our host application will look like this. Clicking the button will start the service and as calls are made we will see request and response content in the tabs. ![image](http://kapoor.io/wp-content/uploads/2014/01/image9-300x300.png "image")

### Capturing XML

To capture XML we need to implement two interfaces IDispatchMessageInspector and IServiceBehavior. The way our solution works is that we will add our implementation of IDispatchMessageInspector to MessageInspectors collection on endpoints used by our ServiceHost. We will first implement IDispatchMessaageInspector in a class called Inspector.```
 public class Inspector : IDispatchMessageInspector
{ 
  ///  
  /// Stores contents of Request message 
  /// passed to the service. 
  ///  
  /// The request XML. 
  public string Request { get; set; } 

  ///  
  /// Stores contents of Response messge 
  /// which is sent back to the client. 
  ///  
  /// The response XML. 
  public string Response { get; set; } 

  #region IDispatchMessageInspector Members 

  ///  
  /// Called after an inbound message has been received but 
  /// before the message is dispatched to the intended operation. 
  ///  
  ///The request message. 
  ///The incoming channel. 
  ///The current service instance. 
  ///  /// The object used to correlate state. 
  ///  
  public object AfterReceiveRequest(
    ref System.ServiceModel.Channels.Message request, 
    System.ServiceModel.IClientChannel channel, 
    System.ServiceModel.InstanceContext instanceContext) 
    { 
      Request = request.ToString(); 
      return null; 
    } 

  ///  
  /// Called after the operation has returned but before the reply message is sent. 
  ///  
  ///The reply message. 
  /// This value is null if the operation is one way.
  ///The correlation object returned from the 
  /// AfterReceiveRequest method. 
  public void BeforeSendReply(ref System.ServiceModel.Channels.Message reply, 
    object correlationState) 
    { 
      Response = reply.ToString(); 
    } 
  #endregion

} 
```Next we need to create a custom behaviour by implementing IServiceBehavior. The only method we are interested in this interface is the ApplyDispatchBehavior method. Here is our implementation of IServiceBehavior.```
 public class CustomBehavior : IServiceBehavior
{ 

  #region IServiceBehavior Members 
  ///  
  /// Provides the ability to pass custom data to binding elements 
  /// to support the contract implementation. 
  ///  
  ///The service description of the service. 
  ///The host of the service. 
  ///The service endpoints. 
  ///Custom objects to which binding elements have access. 
  ///  
  public void AddBindingParameters(ServiceDescription serviceDescription, 
    System.ServiceModel.ServiceHostBase serviceHostBase, 
    System.Collections.ObjectModel.Collection endpoints, 
    System.ServiceModel.Channels.BindingParameterCollection bindingParameters) 
  { 
    return; 
  } 

  ///  
  /// Provides the ability to change run-time property values or 
  /// insert custom extension objects such as error handlers, 
  /// message or parameter interceptors, 
  /// security extensions, and other custom extension objects. 
  ///  
  ///The service description. 
  ///The host that is currently being built. 
  public void ApplyDispatchBehavior(ServiceDescription serviceDescription, System.ServiceModel.ServiceHostBase serviceHostBase) 
  { 
    foreach (ChannelDispatcher dispatcher in serviceHostBase.ChannelDispatchers) 
    { 
      dispatcher.Endpoints
        .ToList()
        .ForEach(x => x.DispatchRuntime.MessageInspectors.Add(new Inspector())); 
    } 
  } 

  ///  
  /// Provides the ability to inspect the service host and 
  /// the service description to confirm that the service 
  /// can run successfully. 
  ///  
  ///The service description. 
  ///The service host that is currently being constructed. 
  ///  
  public void Validate(ServiceDescription serviceDescription, System.ServiceModel.ServiceHostBase serviceHostBase) 
  { 
    return; 
  }

  #endregion

} 
```As said earlier, we will host our service in a Windows Forms application and we would like to display messages in the UI. For this we need access to messages outside the Inspector class we created above. This can be done by raising events when messages are captured. To do just that we will extend our Inspector class with two events and raise them from AfterReceiveRequest and BeforeSendReply methods.```
 /// 
/// Triggered from AfterReceiveRequest method.
/// 
public event EventHandler RaiseRequestReceived;

/// 
/// Triggered from BeforeSendReply method.
/// 
public event EventHandler RaiseSendingReply;

protected void OnRaiseRequestReceived(string message)
{ 
  EventHandler handler = RaiseRequestReceived; 
  if (handler != null) 
  { 
    handler(this, new InspectorEventArgs(message)); 
  }
}

protected void OnRaiseSendingReply(string message)
{ 
  EventHandler handler = RaiseSendingReply;
  if (handler != null) 
  { 
    handler(this, new InspectorEventArgs(message)); 
  }
} 
```And we will also modify AfterReceiveRequest and BeforeSendReply to raise these events.```
 /// 
/// Called after an inbound message has been received but
/// before the message is dispatched to the intended operation.
///
/// This method will also raise RaiseRequestReceived event.
/// 
///The request message.
///The incoming channel.
///The current service instance.
/// 
/// The object used to correlate state.
/// 
public object AfterReceiveRequest( ref System.ServiceModel.Channels.Message request, 
System.ServiceModel.IClientChannel channel, 
System.ServiceModel.InstanceContext instanceContext)
{ 
  Request = request.ToString(); 
  OnRaiseRequestReceived(Request); 
  return null;
}

/// 
/// Called after the operation has returned but before the reply message is sent.
///
/// This method will also raise RaiseSendReply event.
/// 
///The reply message.
/// This value is null if the operation is one way.
///The correlation object returned from the
/// AfterReceiveRequest method.
public void BeforeSendReply(ref System.ServiceModel.Channels.Message reply, object correlationState)
{ 
  Response = reply.ToString(); 
  OnRaiseSendingReply(Response);
}
InspectorEventArgs is a simple class used to store and pass information with our events.
public class InspectorEventArgs : EventArgs
{ 
  public InspectorEventArgs(string message) 
  { 
    this.Message = message; 
  } 

  public string Message { get; set; }
} 
```InspectorEventArgs is a simple class used to store and pass information with our events.```
 public class InspectorEventArgs : EventArgs
{ 
  public InspectorEventArgs(string message) 
  { 
    this.Message = message; 
  } 

  public string Message { get; set; }
} 
```

### Hosting The Service And Using Inspector

Now we are at the point where we can use our behaviour to capture request and response messages. First of all we need to put in some code to host our service. This code will go in the click event handler for our button. There are two main things do here. First we add our custom behaviour to the Behaviors collection of our host and second we hook up the events that are raised by our Inspector class.```
 private void buttonStartService_Click(object sender, EventArgs e)
{ 
  // Add our Custom Behaviour to the list of behaviours 
  host.Description.Behaviors.Add(behavior); 

  // start the service 
  host.Open(); 

  // add event handlers 
  foreach (ChannelDispatcher dispatcher in host.ChannelDispatchers) 
  { 
    foreach (var endPoint in dispatcher.Endpoints) 
    { 

      // get a list of MessageInspectors that are of type Inspector 
      var query = (from ex in endPoint.DispatchRuntime.MessageInspectors 
        where ex.GetType() == typeof(Inspector) 
        select ex).Cast(); 

      // hook up the events 
      foreach (var item in query) 
      { 
        item.RaiseRequestReceived += 
          new EventHandler(Form1_RaiseRequestReceived); 

        item.RaiseSendingReply += 
          new EventHandler(Form1_RaiseSendingReply); 
      } 
    } 
  }
} 
```Now when HelloService is called we will see request and response xml in our Windows Forms application which is also a host for HelloService. We will use WebBrowser controls to display XML. Displaying XML in the WebBrowser control is not just setting a property. There is little but not too much work involved. I picked up a nice technique from this [link](http://www.c-sharpcorner.com/Forums/ShowMessages.aspx?ThreadID=51473).```
 /// 
/// Writes xml to browser.
/// WebBrowser control does render xml properly and to get around
/// I am using this handy tip from this link.
/// http://www.c-sharpcorner.com/Forums/ShowMessages.aspx?ThreadID=51473
/// 
///The browser.
///The message.
private void WriteToBrowser(WebBrowser browser, string message)
{ 
  XslCompiledTransform xTrans = new XslCompiledTransform(); 
  xTrans.Load("default.xslt"); 
  StringReader sr = new StringReader(message); 
  XmlReader xReader = XmlReader.Create(sr); 
  System.IO.MemoryStream ms = new MemoryStream(); 
  xTrans.Transform(xReader, null, ms); 
  ms.Position = 0; 
  browser.DocumentStream = ms;
} 
```

### Creating The Client

Client for HelloService is a simple Windows Forms application with a text box, button and a label. You can download the code at the end of this article and see it for yourself.

### The Output

Here are screenshots of both client and host showing request and response XML. ![WCF Request](http://kapoor.io/wp-content/uploads/2014/01/image11-300x180.png "WCF Request") ![WCF Response](http://kapoor.io/wp-content/uploads/2014/01/image21-300x180.png "WCF Response") ![WCF Client](http://kapoor.io/wp-content/uploads/2014/01/image31-300x133.png "WCF Client") [Code on GitHub](http://bit.ly/debug-release-wcf-capture-xml)