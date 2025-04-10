import json
from firecrawl import FirecrawlApp
from env_load import firecrawl_api_key

def scrapping_function(website_url):
    app = FirecrawlApp(api_key=firecrawl_api_key)
    specific_pages = [
        website_url,
        f"{website_url}/about-us",
        f"{website_url}/contact",
        f"{website_url}/services",
        f"{website_url}/products",
        f"{website_url}/blog",
        f"{website_url}/faq",
        f"{website_url}/testimonials",
        f"{website_url}/careers",
        f"{website_url}/portfolio",
        f"{website_url}/pricing",
        f"{website_url}/team",
        f"{website_url}/privacy-policy",
        f"{website_url}/terms-of-service",
        f"{website_url}/return-policy",
        f"{website_url}/shipping-info",
        f"{website_url}/cookie-policy",
        f"{website_url}/landing-page",
        f"{website_url}/newsletter",
        f"{website_url}/events",
        f"{website_url}/press",
        f"{website_url}/partners",
        f"{website_url}/resources",
        f"{website_url}/support",
        f"{website_url}/login",
        f"{website_url}/documentation",
        f"{website_url}/community",
        f"{website_url}/sitemap",
        f"{website_url}/accessibility",
        f"{website_url}/investors",
        f"{website_url}/franchise",
        f"{website_url}/gallery",
        f"{website_url}/announcements",
        f"{website_url}/offers"
    ]
    scraped_data = {}
    for page in specific_pages:
        scrape_result = app.scrape_url(page, params={'formats': ['markdown']})
        scraped_data[page] = scrape_result.get('markdown', 'No content available')
    with open('scraped_data.json', 'w', encoding='utf-8') as md_file:
        json.dump(scraped_data, md_file, ensure_ascii=False, indent=4)
    return scraped_data