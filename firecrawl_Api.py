import json, time
from firecrawl import FirecrawlApp
from env_load import firecrawl_api_key

def scrapping_function(website_url):
    app = FirecrawlApp(api_key=firecrawl_api_key)
    # specific_pages = [
    #     website_url,  # Main page
    #     f"{website_url}/about-us",
    #     f"{website_url}/services",
    #     f"{website_url}/careers",
    #     f"{website_url}/portfolio",
    #     f"{website_url}/contact"
    # ]
    specific_pages = [
        website_url,  # Home
        f"{website_url}/about-us",
        f"{website_url}/contact",
        f"{website_url}/services",
        f"{website_url}/products",
        # f"{website_url}/blog",
        # f"{website_url}/careers",
        # f"{website_url}/portfolio",
        # f"{website_url}/pricing",
        # f"{website_url}/team",
        # f"{website_url}/privacy-policy",
        # f"{website_url}/landing-page",
        # f"{website_url}/events",
        # f"{website_url}/partners",
        # f"{website_url}/support",
        # f"{website_url}/login",
        # f"{website_url}/community",
        # f"{website_url}/sitemap",
        # f"{website_url}/accessibility",
        # f"{website_url}/announcements",
        # f"{website_url}/offers"
    ]
    scraped_data = {}
    # for page in specific_pages:
    #     scrape_result = app.scrape_url(page, params={'formats': ['markdown']})
    #     scraped_data[page] = scrape_result.get('markdown', 'No content available')
    # with open('scraped_data.json', 'w', encoding='utf-8') as md_file:
    #     json.dump(scraped_data, md_file, ensure_ascii=False, indent=4)
    # return scraped_data
    for page in specific_pages:
            try:
                scrape_result = app.scrape_url(page, params={'formats': ['markdown']})
            except Exception as e:
                print(f"❌ {page}: {str(e)}")

scrapping_function('designgaga.ca')