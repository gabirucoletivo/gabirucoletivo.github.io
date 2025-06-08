import json
import time
from datetime import datetime, timedelta

from eventregistry import *

# Initialize Event Registry
# Get your API key from http://eventregistry.org/
API_KEY = "65a3dde5-6d84-41af-a1cb-ea5cc40ccdda"
er = EventRegistry(apiKey=API_KEY)


def get_most_viewed_articles_by_country(country_name, max_articles=20):
    """
    Get the most viewed articles from a specific country in the last 24 hours

    Args:
        country_name: Name of the country (e.g., "United States", "Germany", "France")
        max_articles: Number of articles to retrieve

    Returns:
        List of articles with their details
    """
    try:
        # Get the country URI
        country_uri = er.getLocationUri(country_name)
        if not country_uri:
            print(f"Could not find URI for country: {country_name}")
            return []

        print(f"Country URI for {country_name}: {country_uri}")

        # Calculate date range for last 24 hours
        end_date = datetime.now()
        start_date = end_date - timedelta(days=1)

        # Create query for articles from the specific country in last 24h
        q = QueryArticlesIter(
            sourceLocationUri=country_uri,
            dateStart=start_date.strftime("%Y-%m-%d"),
            dateEnd=end_date.strftime("%Y-%m-%d"),
            dataType=["news"],  # Only news articles, not blogs
        )

        # Execute query and get articles sorted by social score (most viewed/shared)
        articles = []
        for article in q.execQuery(er, sortBy="socialScore", maxItems=max_articles):
            articles.append(
                {
                    "title": article.get("title", ""),
                    "url": article.get("url", ""),
                    "source": article.get("source", {}).get("title", ""),
                    "date": article.get("date", ""),
                    "dateTime": article.get("dateTime", ""),
                    "socialScore": article.get("socialScore", 0),
                    "sentiment": article.get("sentiment", 0),
                    "country": country_name,
                    "lang": article.get("lang", ""),
                    "body": (
                        article.get("body", "")[:200] + "..."
                        if article.get("body")
                        else ""
                    ),  # First 200 chars
                }
            )

        return articles

    except Exception as e:
        print(f"Error getting articles for {country_name}: {e}")
        return []


def get_trending_articles_alternative(country_name, max_articles=20):
    """
    Alternative method using QueryArticles with RequestArticlesInfo
    """
    try:
        # Get the country URI
        country_uri = er.getLocationUri(country_name)
        if not country_uri:
            return []

        # Calculate date range for last 24 hours
        end_date = datetime.now()
        start_date = end_date - timedelta(days=1)

        # Create query
        q = QueryArticles(
            sourceLocationUri=country_uri,
            dateStart=start_date.strftime("%Y-%m-%d"),
            dateEnd=end_date.strftime("%Y-%m-%d"),
            dataType=["news"],
        )

        # Set requested result with sorting by social score
        q.setRequestedResult(
            RequestArticlesInfo(
                count=max_articles,
                sortBy="socialScore",
                sortByAsc=False,
                returnInfo=ReturnInfo(
                    articleInfo=ArticleInfoFlags(
                        title=True,
                        body=True,
                        url=True,
                        source=True,
                        date=True,
                        dateTime=True,
                        socialScore=True,
                        sentiment=True,
                        lang=True,
                    )
                ),
            )
        )

        # Execute query
        result = er.execQuery(q)

        articles = []
        if "articles" in result and "results" in result["articles"]:
            for article in result["articles"]["results"]:
                articles.append(
                    {
                        "title": article.get("title", ""),
                        "url": article.get("url", ""),
                        "source": article.get("source", {}).get("title", ""),
                        "date": article.get("date", ""),
                        "dateTime": article.get("dateTime", ""),
                        "socialScore": article.get("socialScore", 0),
                        "sentiment": article.get("sentiment", 0),
                        "country": country_name,
                        "lang": article.get("lang", ""),
                        "body": (
                            article.get("body", "")[:200] + "..."
                            if article.get("body")
                            else ""
                        ),
                    }
                )

        return articles

    except Exception as e:
        print(f"Error with alternative method for {country_name}: {e}")
        return []


def get_most_viewed_articles_multiple_countries(countries, articles_per_country=10):
    """
    Get most viewed articles from multiple countries

    Args:
        countries: List of country names
        articles_per_country: Number of articles to get per country

    Returns:
        Dictionary with country names as keys and article lists as values
    """
    all_articles = {}

    for country in countries:
        print(f"\n{'='*50}")
        print(f"Fetching articles for: {country}")
        print(f"{'='*50}")

        # Try primary method first
        articles = get_most_viewed_articles_by_country(country, articles_per_country)

        # If primary method fails, try alternative
        if not articles:
            print(f"Primary method failed, trying alternative...")
            articles = get_trending_articles_alternative(country, articles_per_country)

        if articles:
            all_articles[country] = articles
            print(f"✓ Found {len(articles)} articles for {country}")
        else:
            print(f"✗ No articles found for {country}")

        # Rate limiting - be respectful to the API
        time.sleep(2)

    return all_articles


def display_articles(articles_by_country):
    """Display articles in a readable format"""
    for country, articles in articles_by_country.items():
        print(f"\n{'='*60}")
        print(f"MOST VIEWED ARTICLES IN {country.upper()} (Last 24h)")
        print(f"{'='*60}")

        if not articles:
            print("No articles found.")
            continue

        for i, article in enumerate(articles, 1):
            print(f"\n{i}. {article['title']}")
            print(f"   📰 Source: {article['source']}")
            print(f"   📅 Date: {article['dateTime'] or article['date']}")
            print(f"   🔥 Social Score: {article['socialScore']}")
            print(f"   😊 Sentiment: {article['sentiment']}")
            print(f"   🌐 Language: {article['lang']}")
            print(f"   🔗 URL: {article['url']}")
            if article["body"]:
                print(f"   📝 Preview: {article['body']}")


def save_articles_to_json(
    articles_by_country, filename="most_viewed_articles_24h.json"
):
    """Save articles to JSON file"""
    # Add metadata
    output_data = {
        "metadata": {
            "generated_at": datetime.now().isoformat(),
            "time_period": "Last 24 hours",
            "total_countries": len(articles_by_country),
            "total_articles": sum(
                len(articles) for articles in articles_by_country.values()
            ),
        },
        "articles_by_country": articles_by_country,
    }

    with open(filename, "w", encoding="utf-8") as f:
        json.dump(output_data, f, indent=2, ensure_ascii=False)

    print(f"\n💾 Results saved to {filename}")


def calculate_average_sentiment_per_country(
    input_filename="most_viewed_articles_24h.json",
    output_filename="average_sentiment_per_country.json",
):
    """
    Calculate average sentiment per country from the articles JSON file

    Args:
        input_filename: Path to the JSON file containing articles by country
        output_filename: Path where to save the average sentiment results

    Returns:
        Dictionary with countries as keys and average sentiment as values
    """
    try:
        # Load the articles data
        with open(input_filename, "r", encoding="utf-8") as f:
            data = json.load(f)

        articles_by_country = data.get("articles_by_country", {})
        average_sentiment = {}

        print(f"\n📊 Calculating average sentiment per country...")

        for country, articles in articles_by_country.items():
            if not articles:
                print(f"⚠️  No articles found for {country}")
                continue

            # Extract sentiment values and filter out invalid ones
            sentiments = []
            for article in articles:
                sentiment = article.get("sentiment", 0)
                # Convert to float if it's a string, skip if invalid
                try:
                    sentiment_float = float(sentiment) if sentiment is not None else 0.0
                    sentiments.append(sentiment_float)
                except (ValueError, TypeError):
                    # Skip invalid sentiment values
                    continue

            if sentiments:
                avg_sentiment = sum(sentiments) / len(sentiments)
                average_sentiment[country] = round(avg_sentiment, 4)
                print(
                    f"📍 {country}: {avg_sentiment:.4f} (from {len(sentiments)} articles)"
                )
            else:
                print(f"⚠️  No valid sentiment data for {country}")

        # Create output data with metadata
        output_data = {
            "metadata": {
                "generated_at": datetime.now().isoformat(),
                "source_file": input_filename,
                "calculation_method": "arithmetic_mean",
                "sentiment_scale": "Typically ranges from -1 (negative) to +1 (positive)",
                "total_countries": len(average_sentiment),
            },
            "average_sentiment_by_country": average_sentiment,
        }

        # Save to JSON file
        with open(output_filename, "w", encoding="utf-8") as f:
            json.dump(output_data, f, indent=2, ensure_ascii=False)

        print(f"\n💾 Average sentiment data saved to {output_filename}")

        # Display summary
        if average_sentiment:
            print(f"\n📈 SENTIMENT SUMMARY:")
            sorted_countries = sorted(
                average_sentiment.items(), key=lambda x: x[1], reverse=True
            )
            print(
                f"Most positive: {sorted_countries[0][0]} ({sorted_countries[0][1]:.4f})"
            )
            print(
                f"Most negative: {sorted_countries[-1][0]} ({sorted_countries[-1][1]:.4f})"
            )
            overall_avg = sum(average_sentiment.values()) / len(average_sentiment)
            print(f"Overall average: {overall_avg:.4f}")

        return average_sentiment

    except FileNotFoundError:
        print(f"❌ Error: File {input_filename} not found!")
        print("Make sure you've run the article fetching function first.")
        return {}
    except json.JSONDecodeError:
        print(f"❌ Error: Invalid JSON in {input_filename}")
        return {}
    except Exception as e:
        print(f"❌ Error calculating average sentiment: {e}")
        return {}


def get_single_country_articles(country_name, max_articles=20):
    """
    Get most viewed articles for a single country
    """
    print(f"Getting most viewed articles for {country_name} in the last 24 hours...")

    articles = get_most_viewed_articles_by_country(country_name, max_articles)

    if not articles:
        articles = get_trending_articles_alternative(country_name, max_articles)

    if articles:
        print(f"\n📊 Found {len(articles)} articles for {country_name}")

        # Display top 5 for quick preview
        print(f"\nTop 5 most viewed articles in {country_name}:")
        for i, article in enumerate(articles[:5], 1):
            print(f"{i}. {article['title']}")
            print(
                f"   Social Score: {article['socialScore']} | Source: {article['source']}"
            )

        return articles
    else:
        print(f"❌ No articles found for {country_name}")
        return []


# Main execution
if __name__ == "__main__":
    print("🌍 Event Registry - Most Viewed Articles by Country (Last 24h)")
    print("=" * 70)
    print("Make sure to set your API key in the API_KEY variable!")
    print("Get your free API key at: http://eventregistry.org/")

    # List of major countries to check
    major_countries = [
        "United States",
        "United Kingdom",
        "Ireland",
        "New Zealand",
        "India",
    ]

    # Example 1: Get articles from multiple countries
    print(
        f"\n🔍 Fetching most viewed articles from {len(major_countries)} countries..."
    )
    results = get_most_viewed_articles_multiple_countries(
        major_countries[:5], articles_per_country=5
    )

    # Display results
    display_articles(results)

    # Save to file
    save_articles_to_json(results)

    # Calculate and save average sentiment per country
    print("\n" + "=" * 70)
    average_sentiments = calculate_average_sentiment_per_country()

    # Summary
    total_articles = sum(len(articles) for articles in results.values())
    print(f"\n📈 SUMMARY:")
    print(f"Countries processed: {len(results)}")
    print(f"Total articles found: {total_articles}")

    print("\n" + "=" * 70)
    print("Example usage for single country:")
    print("articles = get_single_country_articles('United States', 10)")
    print("\nExample usage for sentiment analysis:")
    print("sentiments = calculate_average_sentiment_per_country()")

# Example function calls you can use:

# Get articles for a specific country
# articles_usa = get_single_country_articles("United States", 15)

# Get articles for custom list of countries
# custom_countries = ["Germany", "France", "Spain"]
# results = get_most_viewed_articles_multiple_countries(custom_countries, 8)

# Calculate average sentiment from existing JSON file
# sentiments = calculate_average_sentiment_per_country("most_viewed_articles_24h.json", "average_sentiment_per_country.json")

# Search by different country names (try variations if one doesn't work)
# articles_uk = get_single_country_articles("United Kingdom", 10)
# articles_uk = get_single_country_articles("UK", 10)  # Alternative name
