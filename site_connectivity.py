from urllib.request import Request, urlopen


print("Site Connectivity Checker")

def main(url):
    print("Checking connectivity...")
    
    # Required for Secure connections, so it doesn't get an error
    req = Request(
        url,
        headers={'User-Agent': 'Mozilla/5.0'}
    )
    
    response = urlopen(req)
    print("Connected to", url, "success")
    print("Response Code:", response.getcode())
    
input_url = input("Check URL: ")
main(input_url)