# WebScraperPackage

A web scraper package for extracting quotes, images, and links from web pages.

## Installation

You can install the package directly from the GitHub repository:

```bash
pip install git+https://github.com/preetamlenka3/WebScraperPackage.git
```

##Usage
###examples/example.py
```python
from WebScraperPackage import MyWebScraper

# Create a scraper instance with a URL
scraper = MyWebScraper('https://example.com')

# Get quotes from the web page
quotes = scraper.get_quotes()
print("Quotes:", quotes)

# Scrape images from the web page and save them to a folder
image_urls = scraper.scrape_images(save_folder='downloaded_images')
print("Image URLs:", image_urls)

# Scrape links from the web page
links = scraper.scrape_links()
print("Links:", links)
```

##Examples
Check out the 'examples' directory for usage example.
```bash
python examples/example.py
```
