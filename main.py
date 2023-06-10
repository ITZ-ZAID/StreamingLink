
import requests

def bypass_url_shortener(short_url):
    response = requests.head(short_url, allow_redirects=True)
    final_url = response.url
    return final_url

# Example usage
shortened_url = "https://m.easysky.in/8Fy18F"
final_url = bypass_url_shortener(shortened_url)
print("Final URL:", final_url)
