import cloudscraper

def get_cf_clearance(url: str):
    # Create a CloudScraper instance
    scraper = cloudscraper.create_scraper()  # user_agent='custom-user-agent' # Optional: Custom user-agent

    # Perform a GET request to the target URL
    response = scraper.get(url)

    # Extract cookies from the response
    cookies = response.cookies.get_dict()

    # Extract the cf_clearance cookie
    cf_clearance = cookies.get('cf_clearance')

    # Handle case where cf_clearance is not found
    if cf_clearance is None:
        print("cf_clearance cookie not found!")
    else:
        print("cf_clearance:", cf_clearance)

    # Return the cookie for further use
    return cf_clearance

if __name__ == '__main__':
    url = 'https://lyntr.com'  # Replace with the actual URL
    cf_clearance_cookie = get_cf_clearance(url)