require 'spreadsheet'

workbook = Spreadsheet.open './MyLibrary.xls'
worksheets = workbook.worksheets
puts "Found #{worksheets.count}"

worksheets.each do |worksheet|
  next unless worksheet.name == 'Books'

  counter = 0

  File.open('books.txt', 'w') do |file|
    # file.write '<div class="book-list">'
    # file.write "\n\n"
    worksheet.rows.each do |row|
      # puts "#{counter}: #{row[0]}"
      # - ![Emperor of all Maladies](/images/covers/emperor-of-all-maladies.jpg)Emperor of All Maladies
      file.write "#{counter}. #{row[0]} by #{row[1]}\n"
      file.write "\n"
      counter += 1
    end
    # file.write '</div>'
  end
end
