import json
import os
from datetime import datetime

def load_json_file(filepath):
    """Load JSON data from file"""
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            return json.load(f)
    except FileNotFoundError:
        print(f"Error: File {filepath} not found")
        return None
    except json.JSONDecodeError:
        print(f"Error: Invalid JSON in {filepath}")
        return None

def generate_sentiment_stats(sentiment_data):
    """Generate statistics from sentiment data"""
    positive_count = 0
    negative_count = 0
    neutral_count = 0
    
    for sentiment in sentiment_data.values():
        if sentiment is None:
            neutral_count += 1
        elif sentiment > 0.05:
            positive_count += 1
        elif sentiment < -0.05:
            negative_count += 1
        else:
            neutral_count += 1
    
    return {
        'total_countries': len(sentiment_data),
        'positive': positive_count,
        'negative': negative_count,
        'neutral': neutral_count
    }

def format_articles_data_for_js(articles_data):
    """Format articles data for JavaScript embedding"""
    js_data = {}
    
    for country, articles in articles_data.items():
        js_articles = []
        for article in articles:
            js_article = {
                'title': article.get('title', '').replace('"', '\\"').replace("'", "\\'"),
                'source': article.get('source', '').replace('"', '\\"').replace("'", "\\'"),
                'date': article.get('date', ''),
                'sentiment': article.get('sentiment')
            }
            js_articles.append(js_article)
        js_data[country] = js_articles
    
    return js_data

def generate_embedded_map_html(sentiment_file, articles_file, output_file):
    """Generate complete HTML page with embedded map"""
    
    # Load JSON files
    print(f"Loading sentiment data from: {sentiment_file}")
    sentiment_json = load_json_file(sentiment_file)
    if sentiment_json is None:
        return False
    
    print(f"Loading articles data from: {articles_file}")
    articles_json = load_json_file(articles_file)
    if articles_json is None:
        return False
    
    # Extract data
    sentiment_data = sentiment_json.get('average_sentiment_by_country', {})
    articles_data = articles_json.get('articles_by_country', {})
    
    # Generate statistics
    stats = generate_sentiment_stats(sentiment_data)
    total_articles = sum(len(articles) for articles in articles_data.values())
    
    # Format articles for JavaScript
    js_articles = format_articles_data_for_js(articles_data)
    
    # Generate sentiment data string for JavaScript
    sentiment_data_js = json.dumps(sentiment_data, indent=12)
    
    # Generate articles data string for JavaScript
    articles_data_js = json.dumps(js_articles, indent=12, ensure_ascii=False)
    
    # Complete HTML page with embedded map
    embedded_map_html = f'''<!DOCTYPE html>
<html lang="en">

<head>
    <meta charset="UTF-8" />
    <meta name="viewport" content="width=device-width, initial-scale=1.0" />
    <title>Collective Gabirú</title>
    <link rel="stylesheet" href="../../css/fresta.css" />
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/leaflet/1.9.4/leaflet.css" />
    <script src="https://cdnjs.cloudflare.com/ajax/libs/leaflet/1.9.4/leaflet.min.js"></script>
    <style>
        .leaflet-popup-content-wrapper {{
            background: rgba(255, 255, 255, 0.95);
            border-radius: 10px;
            box-shadow: 0 4px 12px rgba(0,0,0,0.3);
        }}
        
        .leaflet-popup-content {{
            margin: 10px;
            font-family: Arial, sans-serif;
            max-width: 300px;
        }}
        
        .popup-header {{
            display: flex;
            align-items: center;
            justify-content: space-between;
            margin-bottom: 10px;
            padding-bottom: 8px;
            border-bottom: 1px solid #eee;
        }}
        
        .popup-country {{
            font-size: 1.3em;
            font-weight: bold;
            color: #333;
        }}
        
        .popup-sentiment {{
            padding: 4px 8px;
            border-radius: 12px;
            color: white;
            font-weight: bold;
            font-size: 0.8em;
        }}
        
        .sentiment-negative-popup {{
            background: #d73027;
        }}
        
        .sentiment-neutral-popup {{
            background: #666;
        }}
        
        .sentiment-positive-popup {{
            background: #4575b4;
        }}
        
        .popup-articles {{
            max-height: 200px;
            overflow-y: auto;
            margin-top: 10px;
        }}
        
        .popup-article {{
            margin-bottom: 8px;
            padding: 8px;
            background: rgba(248, 249, 250, 0.8);
            border-radius: 6px;
            border-left: 3px solid #333;
        }}
        
        .popup-article-title {{
            font-weight: bold;
            margin-bottom: 4px;
            line-height: 1.2;
            color: #222;
            font-size: 0.9em;
        }}
        
        .popup-article-meta {{
            display: flex;
            justify-content: space-between;
            font-size: 0.75em;
            color: #666;
        }}
        
        #sentiment-map {{
            height: 500px; 
            width: 100%; 
            border-radius: 8px; 
            box-shadow: 0 4px 8px rgba(0,0,0,0.1);
        }}
    </style>
</head>

<body>
    <nav>
        <div class="nav-container">
            <ul class="nav-items">
                <li class="nav-item"><a href="../coletivo.html">The collective</a></li>
                <li class="nav-item">
                    <a href="projetos-home.html">Projects</a>
                </li>
                <li class="nav-item">
                    <a href="../residencias.html">Residencies</a>
                </li>
                <li class="nav-item"><a href="../pesquisa.html">Research</a></li>
            </ul>
        </div>
    </nav>

    <h1>South America News Sentiment Mapping</h1>

    <div class="container-residencia">
        <div class="img-container">
            <div id="sentiment-map"></div>
        </div>

        <div class="legenda-imagem">
            <p>
                South America News Sentiment Mapping is a data visualization project that captures the emotional pulse of the continent through its news landscape. Every 24 hours, the project scans the most popular and widely-shared news articles across 13 South American countries, analyzing the sentiment and tone of what's currently dominating public attention in each nation. By examining which stories are resonating most with people - the ones being shared, discussed, and engaged with online - it creates a real-time emotional map of the continent.
            </p>

            <p>
                The interactive visualization translates this data into a living, breathing representation of South America's collective mood. Each country is colored according to the average sentiment of its trending news stories, revealing patterns of optimism, concern, or neutrality across the region. This approach offers a unique window into the social and political climate of South America, showing not just what's happening, but how these events are being received and felt by the public. Through this lens, South America News Sentiment Mapping aims to foster understanding of the diverse experiences and perspectives that shape this vibrant continent, making visible the emotional currents that flow through its media landscape.
            </p>
        </div>

    </div>

    <footer>
        <a href="../../../index.html ">
            <h1>Collective Gabirú</h1>
        </a>
    </footer>

<link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/leaflet/1.9.4/leaflet.css" />
<script src="https://cdnjs.cloudflare.com/ajax/libs/leaflet/1.9.4/leaflet.min.js"></script>

<style>
    .leaflet-popup-content-wrapper {{
        background: rgba(255, 255, 255, 0.95);
        border-radius: 10px;
        box-shadow: 0 4px 12px rgba(0,0,0,0.3);
    }}
    
    .leaflet-popup-content {{
        margin: 10px;
        font-family: Arial, sans-serif;
        max-width: 300px;
    }}
    
    .popup-header {{
        display: flex;
        align-items: center;
        justify-content: space-between;
        margin-bottom: 10px;
        padding-bottom: 8px;
        border-bottom: 1px solid #eee;
    }}
    
    .popup-country {{
        font-size: 1.3em;
        font-weight: bold;
        color: #333;
    }}
    
    .popup-sentiment {{
        padding: 4px 8px;
        border-radius: 12px;
        color: white;
        font-weight: bold;
        font-size: 0.8em;
    }}
    
    .sentiment-negative-popup {{
        background: #d73027;
    }}
    
    .sentiment-neutral-popup {{
        background: #666;
    }}
    
    .sentiment-positive-popup {{
        background: #4575b4;
    }}
    
    .popup-articles {{
        max-height: 200px;
        overflow-y: auto;
        margin-top: 10px;
    }}
    
    .popup-article {{
        margin-bottom: 8px;
        padding: 8px;
        background: rgba(248, 249, 250, 0.8);
        border-radius: 6px;
        border-left: 3px solid #333;
    }}
    
    .popup-article-title {{
        font-weight: bold;
        margin-bottom: 4px;
        line-height: 1.2;
        color: #222;
        font-size: 0.9em;
    }}
    
    .popup-article-meta {{
        display: flex;
        justify-content: space-between;
        font-size: 0.75em;
        color: #666;
    }}
</style>

<script>
    (function() {{
        // Embedded data from your JSON files
        const sentimentData = {sentiment_data_js};
        const articlesData = {articles_data_js};

        let sentimentMap;
        let geojsonLayer;

        // Get sentiment category
        function getSentimentCategory(sentiment) {{
            if (sentiment === null || sentiment === undefined) return 'neutral';
            if (sentiment > 0.05) return 'positive';
            if (sentiment < -0.05) return 'negative';
            return 'neutral';
        }}

        // Get sentiment label
        function getSentimentLabel(sentiment) {{
            if (sentiment === null || sentiment === undefined) return 'Neutro';
            if (sentiment > 0.05) return 'Positivo';
            if (sentiment < -0.05) return 'Negativo';
            return 'Neutro';
        }}

        // Format date
        function formatDate(dateStr) {{
            const date = new Date(dateStr);
            return date.toLocaleDateString('pt-BR', {{
                day: '2-digit',
                month: '2-digit',
                year: 'numeric'
            }});
        }}

        // Create popup content with articles
        function createPopupContent(country, sentiment, articles) {{
            const category = getSentimentCategory(sentiment);
            const label = getSentimentLabel(sentiment);

            let content = `
                <div class="popup-header">
                    <span class="popup-country">${{country}}</span>
                    <span class="popup-sentiment sentiment-${{category}}-popup">
                        ${{sentiment !== null && sentiment !== undefined ? sentiment.toFixed(3) : 'N/A'}}
                    </span>
                </div>
            `;
            
            if (articles.length > 0) {{
                content += `<div><strong>📰 Artigos (${{articles.length}}):</strong></div>`;
                content += `<div class="popup-articles">`;
                
                articles.slice(0, 3).forEach(article => {{
                    content += `
                        <div class="popup-article">
                            <div class="popup-article-title">${{article.title}}</div>
                            <div class="popup-article-meta">
                                <span>📍 ${{article.source}}</span>
                                <span>📅 ${{formatDate(article.date)}}</span>
                            </div>
                        </div>
                    `;
                }});
                
                if (articles.length > 3) {{
                    content += `<div style="text-align: center; color: #666; font-style: italic; margin-top: 8px; font-size: 0.8em;">... e mais ${{articles.length - 3}} artigos</div>`;
                }}
                
                content += `</div>`;
            }}
            
            return content;
        }}

        // Get color based on sentiment
        function getSentimentColor(sentiment) {{
            if (sentiment === null || sentiment === undefined) {{
                return '#f0f0f0'; // Very light gray for no data
            }}
            
            if (sentiment > 0.05) {{
                // Positive sentiment - blue
                return '#4575b4';
            }} else if (sentiment < -0.05) {{
                // Negative sentiment - red
                return '#d73027';
            }} else {{
                // Neutral sentiment - yellow
                return '#ffffcc';
            }}
        }}

        // Initialize embedded map
        function initializeEmbeddedMap() {{
            console.log('🗺️ Inicializando mapa incorporado...');
            
            // Create map focused on South America in the container
            sentimentMap = L.map('sentiment-map').setView([-15, -60], 3);

            // Add OpenStreetMap tile layer
            L.tileLayer('https://{{s}}.tile.openstreetmap.org/{{z}}/{{x}}/{{y}}.png', {{
                attribution: '© OpenStreetMap contributors',
                maxZoom: 18
            }}).addTo(sentimentMap);

            // Load real world countries GeoJSON
            fetch('https://raw.githubusercontent.com/johan/world.geo.json/master/countries.geo.json')
                .then(response => {{
                    if (!response.ok) {{
                        throw new Error('Primeira fonte falhou');
                    }}
                    return response.json();
                }})
                .catch(() => {{
                    return fetch('https://raw.githubusercontent.com/datasets/geo-countries/master/data/countries.geojson')
                        .then(response => response.json());
                }})
                .then(data => {{
                    console.log('✅ Dados geográficos carregados');
                    processWorldDataEmbedded(data);
                }})
                .catch(error => {{
                    console.error('❌ Erro ao carregar dados geográficos:', error);
                }});
        }}

        function processWorldDataEmbedded(data) {{
            // Country name mapping for different naming conventions
            const countryNameMap = {{
                'United States of America': 'United States',
                'United States': 'United States',
                'USA': 'United States',
                'US': 'United States',
                'Brasil': 'Brazil',
                'Brazil': 'Brazil',
                'Chile': 'Chile',
                'Argentina': 'Argentina',
                'Colombia': 'Colombia',
                'Republic of Colombia': 'Colombia',
                'Bolivia': 'Bolivia',
                'Plurinational State of Bolivia': 'Bolivia',
                'Ecuador': 'Ecuador',
                'Republic of Ecuador': 'Ecuador',
                'French Guiana': 'French Guiana',
                'Guyana': 'Guyana',
                'Paraguay': 'Paraguay',
                'Republic of Paraguay': 'Paraguay',
                'Peru': 'Peru',
                'Republic of Peru': 'Peru',
                'Suriname': 'Suriname',
                'Republic of Suriname': 'Suriname',
                'Uruguay': 'Uruguay',
                'Oriental Republic of Uruguay': 'Uruguay',
                'Venezuela': 'Venezuela',
                'Bolivarian Republic of Venezuela': 'Venezuela'
            }};

            // Style function for each country
            function style(feature) {{
                const possibleNames = [
                    feature.properties.NAME,
                    feature.properties.NAME_EN,
                    feature.properties.ADMIN,
                    feature.properties.name,
                    feature.properties.country,
                    feature.properties.Country,
                    feature.properties.NAME_LONG
                ];
                
                let countryName = null;
                for (let name of possibleNames) {{
                    if (name) {{
                        countryName = name;
                        break;
                    }}
                }}
                
                if (!countryName) {{
                    return {{
                        fillColor: '#f0f0f0',
                        weight: 1,
                        opacity: 1,
                        color: 'white',
                        fillOpacity: 0.7
                    }};
                }}
                
                const mappedName = countryNameMap[countryName] || countryName;
                const sentiment = sentimentData[mappedName];
                const color = getSentimentColor(sentiment);
                
                return {{
                    fillColor: color,
                    weight: 1,
                    opacity: 1,
                    color: 'white',
                    fillOpacity: 0.8
                }};
            }}
            
            // Function for each feature (country)
            function onEachFeature(feature, layer) {{
                const possibleNames = [
                    feature.properties.NAME,
                    feature.properties.NAME_EN,
                    feature.properties.ADMIN,
                    feature.properties.name,
                    feature.properties.country,
                    feature.properties.Country,
                    feature.properties.NAME_LONG
                ];
                
                let countryName = null;
                for (let name of possibleNames) {{
                    if (name) {{
                        countryName = name;
                        break;
                    }}
                }}
                
                if (!countryName) return;
                
                const mappedName = countryNameMap[countryName] || countryName;
                const sentiment = sentimentData[mappedName];
                const articles = articlesData[mappedName] || [];
                
                // Add popup only for countries with data
                if (sentiment !== undefined) {{
                    const popupContent = createPopupContent(mappedName, sentiment, articles);
                    layer.bindPopup(popupContent, {{
                        maxWidth: 300,
                        className: 'custom-popup'
                    }});
                }}
                
                // Add hover effects
                layer.on({{
                    mouseover: function(e) {{
                        const layer = e.target;
                        layer.setStyle({{
                            weight: 3,
                            color: '#333',
                            fillOpacity: 0.9
                        }});
                        layer.bringToFront();
                    }},
                    mouseout: function(e) {{
                        geojsonLayer.resetStyle(e.target);
                    }}
                }});
            }}
            
            // Add GeoJSON layer to map
            geojsonLayer = L.geoJSON(data, {{
                style: style,
                onEachFeature: onEachFeature
            }}).addTo(sentimentMap);
            
            // Zoom to South America bounds
            zoomToSouthAmericaEmbedded();
            
            console.log('🎯 Mapa incorporado carregado');
        }}
        
        // Function to zoom map to South America
        function zoomToSouthAmericaEmbedded() {{
            // South America bounding box coordinates
            const southAmericaBounds = [
                [-56, -82], // Southwest corner (lat, lng) - covers southern Chile/Argentina
                [13, -34]   // Northeast corner (lat, lng) - covers northern Venezuela/Guyana
            ];
            
            // Fit map to South America bounds with padding
            sentimentMap.fitBounds(southAmericaBounds, {{
                padding: [5, 5],
                maxZoom: 4
            }});
        }}

        // Initialize when DOM is ready
        if (document.readyState === 'loading') {{
            document.addEventListener('DOMContentLoaded', initializeEmbeddedMap);
        }} else {{
            initializeEmbeddedMap();
        }}
        
        // Also initialize when the map container becomes visible (in case it's initially hidden)
        const observer = new IntersectionObserver((entries) => {{
            entries.forEach(entry => {{
                if (entry.isIntersecting && sentimentMap) {{
                    setTimeout(() => {{
                        sentimentMap.invalidateSize();
                    }}, 100);
                }}
            }});
        }});
        
        const mapContainer = document.getElementById('sentiment-map');
        if (mapContainer) {{
            observer.observe(mapContainer);
        }}
    }})();
    </script>
</body>
</html>'''

    # Write HTML file
    try:
        with open(output_file, 'w', encoding='utf-8') as f:
            f.write(embedded_map_html)
        print(f"✅ Embedded map HTML generated successfully: {output_file}")
        return True
    except Exception as e:
        print(f"❌ Error writing HTML file: {e}")
        return False

def main():
    """Main function to generate embedded map HTML from command line arguments"""
    import sys
    
    # Default file paths
    sentiment_file = "average_sentiment_per_country.json"
    articles_file = "most_viewed_articles_24h.json"
    output_file = "assets/pages/projetos/projeto-map.html"
    
    # Check if custom file paths are provided
    if len(sys.argv) >= 4:
        sentiment_file = sys.argv[1]
        articles_file = sys.argv[2]
        output_file = sys.argv[3]
    elif len(sys.argv) == 2:
        # If only one argument, assume it's the output file
        output_file = sys.argv[1]
    
    print("🚀 Embedded HTML Generator for World Sentiment Map")
    print("=" * 50)
    print(f"📊 Sentiment file: {sentiment_file}")
    print(f"📰 Articles file: {articles_file}")
    print(f"📄 Output file: {output_file}")
    print("=" * 50)
    
    # Check if input files exist
    if not os.path.exists(sentiment_file):
        print(f"❌ Error: Sentiment file not found: {sentiment_file}")
        return
    
    if not os.path.exists(articles_file):
        print(f"❌ Error: Articles file not found: {articles_file}")
        return
    
    # Create output directory if it doesn't exist
    output_dir = os.path.dirname(output_file)
    if output_dir and not os.path.exists(output_dir):
        os.makedirs(output_dir, exist_ok=True)
        print(f"📁 Created output directory: {output_dir}")
    
    # Generate embedded map HTML
    success = generate_embedded_map_html(sentiment_file, articles_file, output_file)
    
    if success:
        print("🎉 Generation completed successfully!")
        print(f"🌐 Include the contents of {output_file} in your HTML page")
        print("💡 Replace the img tag with the generated map HTML")
    else:
        print("💥 Generation failed!")

if __name__ == "__main__":
    main()