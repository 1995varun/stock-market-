import sys
import os
import datetime
from colorama import init, Fore, Style
from src.news_scraper import get_stock_news
from src.youtube_scraper import get_stock_videos
from src.infographic import generate_infographic
from src.emailer import send_weekly_email
from src.stock_data import INDIAN_STOCKS

# Initialize colorama
init()

# Force utf-8 output for Windows console
if sys.platform.startswith('win'):
    sys.stdout.reconfigure(encoding='utf-8')

def print_header():
    print(Fore.CYAN + "=" * 60)
    print(Fore.YELLOW + "      INDIAN STOCK MARKET INSIGHTS AUTOMATION      ")
    print(Fore.CYAN + "=" * 60 + Style.RESET_ALL)

def print_section(title):
    print(f"\n{Fore.GREEN}>>> {title} {Style.RESET_ALL}")
    print("-" * 40)

def extract_stocks_from_text(items):
    """
    Scans titles and returns a list of unique stock names found.
    """
    found_stocks = []
    seen = set()
    
    # Simple keyword matching
    for item in items:
        text = item['title']
        for stock in INDIAN_STOCKS:
            # Check if stock name is in the text (case-insensitiveish)
            if stock.lower() in text.lower() and stock not in seen:
                found_stocks.append(stock)
                seen.add(stock)
    
    return found_stocks

def main():
    print_header()
    
    default_news_query = "Top stocks to buy this week India"
    default_video_query = "Best Indian shares to buy this week"

    print("This tool searches for trending Indian stock information.")
    
    if len(sys.argv) > 1 and sys.argv[1] == "--auto":
        print("Running in AUTOMATION mode (using defaults).")
        news_query = default_news_query
        video_query = default_video_query
    else:
        print("Press Enter to use default queries or type your own.")
        try:
            news_query = input(f"{Fore.BLUE}Enter News Search Query (default: '{default_news_query}'): {Style.RESET_ALL}") or default_news_query
            video_query = input(f"{Fore.BLUE}Enter YouTube Search Query (default: '{default_video_query}'): {Style.RESET_ALL}") or default_video_query
        except EOFError:
            news_query = default_news_query
            video_query = default_video_query
    
    # 1. Fetch News
    print_section("FETCHING GOOGLE NEWS")
    news = get_stock_news(news_query)
    
    # 2. Fetch Videos
    print_section("FETCHING YOUTUBE VIDEOS")
    videos = get_stock_videos(video_query)
    
    # 3. Analyze and Extract Stock Names
    all_items = (news if news else []) + (videos if videos else [])
    mentioned_stocks = extract_stocks_from_text(all_items)
    
    # Fallback if no specific stocks found
    if not mentioned_stocks:
        mentioned_stocks = ["Nifty 50", "Sensex", "See Report Details"]
        print(f"{Fore.RED}No specific stock names matched in the summaries.{Style.RESET_ALL}")
    else:
        print(f"{Fore.GREEN}Found mentions of: {', '.join(mentioned_stocks)}{Style.RESET_ALL}")

    
    summary_text = f"Stock Market Insights Report - {datetime.date.today()}\n"
    summary_text += f"Top Identified Stocks: {', '.join(mentioned_stocks)}\n\n"
    
    print(Fore.CYAN + "\n" + "=" * 60)
    print(Fore.WHITE + "              FINAL SUMMARY REPORT              ")
    print(Fore.CYAN + "=" * 60 + Style.RESET_ALL)
    
    print(f"\n{Fore.YELLOW}--- TOP NEWS ARTICLES ---{Style.RESET_ALL}")
    summary_text += "--- TOP NEWS ARTICLES ---\n"
    if news:
        for i, item in enumerate(news, 1):
            line = f"{i}. {item['title']}"
            print(line)
            print(f"   {Fore.LIGHTBLACK_EX}Source: {item['publisher']} | {item['published']}{Style.RESET_ALL}")
            print(f"   Link: {item['link']}\n")
            summary_text += f"{line}\nLink: {item['link']}\n\n"
    else:
        print("No news found.")
        summary_text += "No news found.\n"

    print(f"\n{Fore.YELLOW}--- TOP YOUTUBE VIDEOS ---{Style.RESET_ALL}")
    summary_text += "\n--- TOP YOUTUBE VIDEOS ---\n"
    if videos:
        for i, item in enumerate(videos, 1):
            line = f"{i}. {item['title']}"
            print(line)
            print(f"   {Fore.LIGHTBLACK_EX}Channel: {item['channel']} | Views: {item['views']}{Style.RESET_ALL}")
            print(f"   Link: {item['link']}\n")
            summary_text += f"{line}\nLink: {item['link']}\n\n"
    else:
        print("No videos found.")
        summary_text += "No videos found.\n"
    
    # Save to file
    with open("stock_report.txt", "w", encoding="utf-8") as f:
        f.write(summary_text)
    print(f"\n{Fore.GREEN}Report saved to 'stock_report.txt'.{Style.RESET_ALL}")

    # 4. Generate Infographic with STOCK NAMES
    print_section("GENERATING INFOGRAPHIC")
    image_path = generate_infographic(mentioned_stocks)

    # 5. Email Automation
    TARGET_EMAIL = "varunlakebright04@gmail.com"
    
    # Retrieve credentials from environment variables for security
    SENDER_EMAIL = os.environ.get("GMAIL_USER")
    SENDER_PASSWORD = os.environ.get("GMAIL_PASS")

    if SENDER_EMAIL and SENDER_PASSWORD:
        print_section("SENDING EMAIL")
        send_weekly_email(
            TARGET_EMAIL, 
            f"Weekly Top Indian Stocks - {datetime.date.today()}", 
            summary_text, 
            image_path,
            SENDER_EMAIL,
            SENDER_PASSWORD
        )
    else:
        print(f"\n{Fore.RED}[!] Email credentials (GMAIL_USER, GMAIL_PASS) not found in environment variables.")
        print(f"    Email to {TARGET_EMAIL} was skipped.{Style.RESET_ALL}")

if __name__ == "__main__":
    main()
