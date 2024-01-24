# WebScraperPackage

## Description:
Developed a Python package named "WebScraperPackage" for web scraping tasks, including extracting quotes, images, and links from web pages. Implemented using the requests library for HTTP requests, BeautifulSoup for HTML parsing, and PIL for image processing. The package offers a versatile and user-friendly interface for content extraction, making it suitable for a variety of web scraping applications.

## Key Contributions:

-Created a robust web scraper class with methods for extracting quotes, saving quotes to a file, scraping images, and scraping links.
-Implemented error handling and logging for improved reliability and debugging.
-Included support for data URLs, enhancing flexibility in handling various types of content.
-Integrated unit tests to ensure the reliability of the package across different scenarios.

##Technologies Used:
 Python, requests, BeautifulSoup, PIL (Pillow).

## Installation

You can install the package directly from the GitHub repository:

```bash
pip install git+https://github.com/preetamlenka3/WebScraperPackage.git
```
# How to Use
## Usage ### examples/example.py

### Here's a simple example to get you going:
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

### Run this command to see one in action:
```bash
python examples/example.py
```
💬 Any issue or anything [here](https://github.com/preetamlenka3/WebScraperPackage/issues)**
