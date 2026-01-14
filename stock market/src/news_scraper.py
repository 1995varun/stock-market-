from gnews import GNews

def get_stock_news(query="Top Indian Stocks", period="7d", max_results=10):
    """
    Fetches news articles related to the stock market query.
    """
    google_news = GNews(period=period, max_results=max_results)
    google_news.country = 'India'
    google_news.language = 'english'
    
    print(f"Searching Google News for: {query}...")
    try:
        news_results = google_news.get_news(query)
        cleaned_results = []
        for article in news_results:
            cleaned_results.append({
                'title': article.get('title'),
                'link': article.get('url'),
                'published': article.get('published date'),
                'publisher': article.get('publisher', {}).get('title')
            })
        return cleaned_results
    except Exception as e:
        print(f"Error fetching news: {e}")
        return []

if __name__ == "__main__":
    # Test
    results = get_stock_news()
    for res in results:
        print(f"- {res['title']}")
