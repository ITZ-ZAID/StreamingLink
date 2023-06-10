
import requests

def bypass_url_shortener(short_url):
    response = requests.head(short_url, allow_redirects=True)
    final_url = response.url
    return final_url

# Example usage
shortened_url = "https://bit.ly/ABC123"
final_url = bypass_url_shortener(shortened_url)
print("Final URL:", final_url)
