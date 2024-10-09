AUTHOR = "Deepak"
SITENAME = "deekap.com"
SITEURL = "https://deekap.com"

THEME = "theme"
RELATIVE_URLS = True

STATIC_PATHS = ["images"]

PATH = "content"

TIMEZONE = "Australia/Sydney"

DEFAULT_LANG = "en"
MENUITEMS = [
    ("Home", "/"),
    ("Blog", "/blog"),
    ("About", "/pages/about"),
]
DISPLAY_CATEGORIES_ON_MENU = False

ARTICLE_URL = "{date:%Y}/{date:%m}/{date:%d}/{slug}/"
ARTICLE_SAVE_AS = "{date:%Y}/{date:%m}/{date:%d}/{slug}/index.html"
INDEX_SAVE_AS = "index.html"
BLOG_URL = "blog/"  # Blog will be accessible at /blog/
BLOG_SAVE_AS = "blog/index.html"  # The blog page will be saved at blog/index.html
TAG_SAVE_AS = "tag/{slug}.html"
TAGS_SAVE_AS = "tags.html"


# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Blogroll
LINKS = (
    ("Pelican", "https://getpelican.com/"),
    ("Python.org", "https://www.python.org/"),
    ("Jinja2", "https://palletsprojects.com/p/jinja/"),
    ("You can modify those links in your config file", "#"),
)

# Social widget
SOCIAL = (
    ("You can add links in your config file", "#"),
    ("Another social link", "#"),
)

DEFAULT_PAGINATION = 0

MARKDOWN = {
    "extensions": ["codehilite", "extra"],
    "extension_configs": {
        "codehilite": {
            "css_class": "highlight",
            "linenums": False,
        }
    },
    "output_format": "html5",
}
# Uncomment following line if you want document-relative URLs when developing
# RELATIVE_URLS = True
