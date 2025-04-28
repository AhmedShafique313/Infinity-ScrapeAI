import json
from firecrawl import FirecrawlApp
from env_load import firecrawl_api_key

def scrapping_function(website_url):
    app = FirecrawlApp(api_key=firecrawl_api_key)
    specific_pages = [
        website_url,  # Main page
        f"{website_url}/about-us",
        f"{website_url}/services",
        f"{website_url}/careers",
        f"{website_url}/portfolio",
        f"{website_url}/contact"
    ]
    scraped_data = {}
    for page in specific_pages:
        try:
            scrape_result = app.scrape_url(page)  # Removed params argument
            scraped_data[page] = scrape_result.get('markdown', 'No content available')
        except Exception as e:
            scraped_data[page] = f"Error occurred: {str(e)}"  # Handle errors gracefully
    
    return scraped_data