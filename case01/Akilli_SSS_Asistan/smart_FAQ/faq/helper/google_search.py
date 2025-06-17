from serpapi.google_search import GoogleSearch
import os
import requests
from bs4 import BeautifulSoup

def google_search(query):
    api_key = os.getenv("SERPAPI_API_KEY")
    
    if not api_key:
        print("Error: SERPAPI_API_KEY is not set. Please check your environment variables.")
        return "API key missing."

    params = {
        "api_key": api_key,
        "engine": "google",
        "q": query,
    }

    search = GoogleSearch(params)

    try:
        result = search.get_dict()
        
        if 'error' in result:
            print(f"API Error: {result['error']}")
            return "API Error: Unable to fetch results."

        search_results = [item.get('snippet', '') for item in result.get('organic_results', [])]

        if not search_results:
            return "No relevant search results found."

        return ' '.join(search_results)

    except Exception as e:
        print(f"Exception occurred: {e}")
        return "Error: Unable to fetch search results."


def search_in_urls(query, urls):
    """
    Verilen URL listesinde query kelimesini arar.
    Bulunan ilk eşleşmeyi döner.
    Eğer hiçbir URL'de bulunamazsa None döner.
    """
    for url in urls:
        try:
            response = requests.get(url, timeout=5)
            if response.status_code == 200:
                soup = BeautifulSoup(response.text, 'html.parser')
                page_text = soup.get_text(separator=' ', strip=True).lower()
                if query.lower() in page_text:
                    return f"Bu bilgi şu sayfada bulunuyor: {url}"
        except Exception as e:
            print(f"Error fetching {url}: {e}")
            continue

    return None