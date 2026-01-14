from youtubesearchpython import VideosSearch

def get_stock_videos(query="Best Indian Stocks to buy now", limit=10):
    """
    Fetches YouTube videos related to the stock market query.
    """
    search = VideosSearch(query, limit=limit)
    
    print(f"Searching YouTube for: {query}...")
    try:
        results = search.result()
        videos = []
        
        if 'result' in results:
            for video in results['result']:
                videos.append({
                    'title': video.get('title'),
                    'link': video.get('link'),
                    'views': video.get('viewCount', {}).get('text'),
                    'channel': video.get('channel', {}).get('name'),
                    'published': video.get('publishedTime')
                })
        return videos
    except Exception as e:
        print(f"Error fetching videos: {e}")
        return []

if __name__ == "__main__":
    # Test
    videos = get_stock_videos()
    for v in videos:
        print(f"- {v['title']} ({v['views']})")
