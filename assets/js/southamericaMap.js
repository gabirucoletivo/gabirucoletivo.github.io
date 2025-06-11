
    (function() {
        // Embedded data from your JSON files
        const sentimentData = {
            "Argentina": -0.23,
            "Bolivia": 0.15,
            "Brazil": -0.41,
            "Chile": 0.67,
            "Colombia": -0.08,
            "Ecuador": 0.34,
            "French Guiana": -0.52,
            "Guyana": 0.0745,
            "Paraguay": 0.28,
            "Peru": -0.19,
            "Suriname": 0.83,
            "Uruguay": 0.45,
            "Venezuela": -0.74
};
        const articlesData = {
            "Argentina": [
                        {
                                    "title": "Liga Termense: el árbitro mostró la roja a un jugador y lo quisieron golpear - Diario Panorama",
                                    "source": "Diario Panorama",
                                    "date": "2025-06-08",
                                    "sentiment": null
                        },
                        {
                                    "title": "El Grupo de Puebla lanza una campaÃ±a internacional contra la detenciÃ³n de Cristina",
                                    "source": "La Política Online",
                                    "date": "2025-06-08",
                                    "sentiment": null
                        },
                        {
                                    "title": "El año y medio de gestión libertaria empieza a dar señales que alertan en Casa Rosada",
                                    "source": "El Litoral",
                                    "date": "2025-06-08",
                                    "sentiment": null
                        }
            ],
            "Bolivia": [
                        {
                                    "title": "Cochabamba sufre por el bloqueo evista y la violencia deja más de 50 heridos",
                                    "source": "EL DEBER",
                                    "date": "2025-06-08",
                                    "sentiment": null
                        },
                        {
                                    "title": "\\\"Nu ne vom mai reveni niciodată în acest domeniu\\\", îl contrează o cercetătoare pe deputatul USR Claudiu Năsui în privința bugetului cercetării românești - HotNews.ro",
                                    "source": "HotNews.ro",
                                    "date": "2025-06-08",
                                    "sentiment": null
                        },
                        {
                                    "title": "Los candidatos a la presidencia Manfred, Samuel y Tuto se reúnen en Cochabamba",
                                    "source": "EL DEBER",
                                    "date": "2025-06-08",
                                    "sentiment": null
                        }
            ],
            "Brazil": [
                        {
                                    "title": "Tiago Mali: 12 estados têm mais beneficiários do Bolsa Família do que carteira assinada",
                                    "source": "UOL  notícias",
                                    "date": "2025-06-08",
                                    "sentiment": null
                        },
                        {
                                    "title": "Governo e partidos decidem hoje se cortam supersalários para resolver IOF",
                                    "source": "UOL",
                                    "date": "2025-06-08",
                                    "sentiment": null
                        },
                        {
                                    "title": "Ministro da Defesa de Israel diz que impedirá que barco com Greta Thunberg e outros ativistas chegue a Gaza",
                                    "source": "globo.com",
                                    "date": "2025-06-08",
                                    "sentiment": null
                        }
            ],
            "Chile": [
                        {
                                    "title": "\\\"Es fundamental para salvar vidas\\\": Activan Código Azul en Los Ángeles por bajas temperaturas",
                                    "source": "BioBioChile",
                                    "date": "2025-06-08",
                                    "sentiment": null
                        },
                        {
                                    "title": "Participaron efectivos de Chile, Estados Unidos, España, Argentina, Colombia y Paraguay: cierra ejercicio Estrella Austral - La Tercera",
                                    "source": "LA TERCERA",
                                    "date": "2025-06-08",
                                    "sentiment": null
                        },
                        {
                                    "title": "Argentina: Encuentran en una planta de basura bolsa con el cuerpo de un recién nacido",
                                    "source": "24horas.cl - Home",
                                    "date": "2025-06-08",
                                    "sentiment": null
                        }
            ],
            "Colombia": [
                        {
                                    "title": "Marco Rubio estalla contra gobierno Petro tras atentado contra Miguel Uribe: \\\"resultado de la violenta retórica izquierdista\\\"",
                                    "source": "Semana.com   Últimas Noticias de Colombia y el Mundo",
                                    "date": "2025-06-08",
                                    "sentiment": null
                        },
                        {
                                    "title": "Fuerte temblor en Colombia: se sintió con fuerza en Bogotá, Medellín y Cali en la mañana de este domingo 8 de junio",
                                    "source": "Semana.com   Últimas Noticias de Colombia y el Mundo",
                                    "date": "2025-06-08",
                                    "sentiment": null
                        },
                        {
                                    "title": "\\\"El directamente responsable es Gustavo Petro\\\": Andrés Pastrana tras atentado a Miguel Uribe",
                                    "source": "Semana.com   Últimas Noticias de Colombia y el Mundo",
                                    "date": "2025-06-08",
                                    "sentiment": null
                        }
            ],
            "Ecuador": [
                        {
                                    "title": "Un perfil capaz de doblegar al crimen",
                                    "source": "Diario El Telégrafo",
                                    "date": "2025-06-08",
                                    "sentiment": null
                        },
                        {
                                    "title": "Fuerte sismo en Colombia también se detectó desde Ecuador este domingo",
                                    "source": "EL UNIVERSO",
                                    "date": "2025-06-08",
                                    "sentiment": null
                        },
                        {
                                    "title": "Ecuador pedirá visa a viajeros en tránsito de 45 países tras cambios en la Ley de Movilidad",
                                    "source": "Teleamazonas",
                                    "date": "2025-06-08",
                                    "sentiment": null
                        }
            ],
            "French Guiana": [
                        {
                                    "title": "Blada.com - infos citoyennes - Appel à candidatures : Lékòl dan bwa",
                                    "source": "Blada, le petit journal de Kourou",
                                    "date": "2025-06-09",
                                    "sentiment": null
                        },
                        {
                                    "title": "Blada.com - infos citoyennes - L\\'animal du mois : Le Grand Tinamou",
                                    "source": "Blada, le petit journal de Kourou",
                                    "date": "2025-06-09",
                                    "sentiment": null
                        },
                        {
                                    "title": "Blada.com - infos citoyennes - Lancement du concours de courts-métrages",
                                    "source": "Blada, le petit journal de Kourou",
                                    "date": "2025-06-09",
                                    "sentiment": null
                        }
            ],
            "Guyana": [
                        {
                                    "title": "Foulis construction worker shot dead, guard in custody - Stabroek News",
                                    "source": "Stabroek News",
                                    "date": "2025-06-09",
                                    "sentiment": -0.1686274509803921
                        },
                        {
                                    "title": "Fathers are important - Guyana Chronicle",
                                    "source": "Guyana Chronicle",
                                    "date": "2025-06-08",
                                    "sentiment": 0.3019607843137255
                        },
                        {
                                    "title": "DIFFICULT BUT PROFOUNDLY NECESSARY CONVERSATIONS WITH OUR OFFSPRING BRIDGE WORLDS TOWARDS SURVIVAL - Guyana Chronicle",
                                    "source": "Guyana Chronicle",
                                    "date": "2025-06-08",
                                    "sentiment": 0.09019607843137245
                        }
            ],
            "Paraguay": [
                        {
                                    "title": "Lanzamientos literarios y recomendaciones para leer",
                                    "source": "Última Hora",
                                    "date": "2025-06-08",
                                    "sentiment": null
                        },
                        {
                                    "title": "La OSCA lleva a Trinidad música, emociones y humor sinfónico",
                                    "source": "Última Hora",
                                    "date": "2025-06-08",
                                    "sentiment": null
                        },
                        {
                                    "title": "Egresa de Harvard paraguayo que activa contra corrupción",
                                    "source": "Última Hora",
                                    "date": "2025-06-08",
                                    "sentiment": null
                        }
            ],
            "Peru": [
                        {
                                    "title": "Ministerio de Vivienda impulsa Planes de Desarrollo Sostenible en zonas de frontera",
                                    "source": "andina.pe",
                                    "date": "2025-06-08",
                                    "sentiment": null
                        },
                        {
                                    "title": "Detenido presunto autor de disparos contra aspirante presidencial colombiano Miguel Uribe",
                                    "source": "andina.pe",
                                    "date": "2025-06-08",
                                    "sentiment": null
                        },
                        {
                                    "title": "López Aliaga y testaferro de Montesinos en la fiesta del abogado Wilber Medina",
                                    "source": "LaRepublica.pe",
                                    "date": "2025-06-08",
                                    "sentiment": null
                        }
            ],
            "Suriname": [
                        {
                                    "title": "Twintig verdachten in kader van operatie Delta Force aangehouden",
                                    "source": "Waterkant",
                                    "date": "2025-06-09",
                                    "sentiment": null
                        },
                        {
                                    "title": "Dronken man aangehouden voor brandstichting in Pikin Saron",
                                    "source": "Waterkant",
                                    "date": "2025-06-09",
                                    "sentiment": null
                        },
                        {
                                    "title": "OW-minister Nurmohammed op dienstreis naar China",
                                    "source": "Waterkant",
                                    "date": "2025-06-09",
                                    "sentiment": null
                        }
            ],
            "Uruguay": [
                        {
                                    "title": "¿Qué futuro?",
                                    "source": "Diario EL PAIS Uruguay",
                                    "date": "2025-06-08",
                                    "sentiment": null
                        },
                        {
                                    "title": "Sergio Puglia: su vida en Punta, la vigencia, volver al prime time y las criticas por ser del Partido Nacional",
                                    "source": "Diario EL PAIS Uruguay",
                                    "date": "2025-06-08",
                                    "sentiment": null
                        },
                        {
                                    "title": "Gobierno de Bukele arresta a abogado constitucionalista crítico del presidente salvadoreño",
                                    "source": "Diario EL PAIS Uruguay",
                                    "date": "2025-06-08",
                                    "sentiment": null
                        }
            ],
            "Venezuela": [
                        {
                                    "title": "Los chats, la mujer y el otro sicario: las primeras pistas sobre el atentado a Miguel Uribe Turbay",
                                    "source": "LaPatilla.com",
                                    "date": "2025-06-08",
                                    "sentiment": null
                        },
                        {
                                    "title": "Ataques israelíes exterminan a más de cien civiles de Gaza en el último día - teleSUR",
                                    "source": "teleSURtv.net",
                                    "date": "2025-06-08",
                                    "sentiment": null
                        },
                        {
                                    "title": "El precandidato Miguel Uribe sale de cirugía en estado crítico tras el intento de asesinato en Bogotá",
                                    "source": "El Universal: El UNIVERSAL",
                                    "date": "2025-06-08",
                                    "sentiment": null
                        }
            ]
};

        let sentimentMap;
        let geojsonLayer;

        // Get sentiment category
        function getSentimentCategory(sentiment) {
            if (sentiment === null || sentiment === undefined) return 'neutral';
            if (sentiment > 0.05) return 'positive';
            if (sentiment < -0.05) return 'negative';
            return 'neutral';
        }

        // Get sentiment label
        function getSentimentLabel(sentiment) {
            if (sentiment === null || sentiment === undefined) return 'Neutro';
            if (sentiment > 0.05) return 'Positivo';
            if (sentiment < -0.05) return 'Negativo';
            return 'Neutro';
        }

        // Format date
        function formatDate(dateStr) {
            const date = new Date(dateStr);
            return date.toLocaleDateString('pt-BR', {
                day: '2-digit',
                month: '2-digit',
                year: 'numeric'
            });
        }

        // Create popup content with articles
        function createPopupContent(country, sentiment, articles) {
            const category = getSentimentCategory(sentiment);
            const label = getSentimentLabel(sentiment);

            let content = `
                <div class="popup-header">
                    <span class="popup-country">${country}</span>
                    <span class="popup-sentiment sentiment-${category}-popup">
                        ${sentiment !== null && sentiment !== undefined ? sentiment.toFixed(3) : 'N/A'}
                    </span>
                </div>
            `;
            
            if (articles.length > 0) {
                content += `<div><strong>📰 Artigos (${articles.length}):</strong></div>`;
                content += `<div class="popup-articles">`;
                
                articles.slice(0, 3).forEach(article => {
                    content += `
                        <div class="popup-article">
                            <div class="popup-article-title">${article.title}</div>
                            <div class="popup-article-meta">
                                <span>📍 ${article.source}</span>
                                <span>📅 ${formatDate(article.date)}</span>
                            </div>
                        </div>
                    `;
                });
                
                if (articles.length > 3) {
                    content += `<div style="text-align: center; color: #666; font-style: italic; margin-top: 8px; font-size: 0.8em;">... e mais ${articles.length - 3} artigos</div>`;
                }
                
                content += `</div>`;
            }
            
            return content;
        }

        // Get color based on sentiment
        function getSentimentColor(sentiment) {
            if (sentiment === null || sentiment === undefined) {
                return '#f0f0f0'; // Very light gray for no data
            }
            
            if (sentiment > 0.05) {
                // Positive sentiment - blue
                return '#4575b4';
            } else if (sentiment < -0.05) {
                // Negative sentiment - red
                return '#d73027';
            } else {
                // Neutral sentiment - yellow
                return '#ffffcc';
            }
        }

        // Initialize embedded map
        function initializeEmbeddedMap() {
            console.log('🗺️ Inicializando mapa incorporado...');
            
            // Create map focused on South America in the container
            sentimentMap = L.map('sentiment-map').setView([-15, -60], 3);

            // Add OpenStreetMap tile layer
            L.tileLayer('https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png', {
                attribution: '© OpenStreetMap contributors',
                maxZoom: 18
            }).addTo(sentimentMap);

            // Load real world countries GeoJSON
            fetch('https://raw.githubusercontent.com/johan/world.geo.json/master/countries.geo.json')
                .then(response => {
                    if (!response.ok) {
                        throw new Error('Primeira fonte falhou');
                    }
                    return response.json();
                })
                .catch(() => {
                    return fetch('https://raw.githubusercontent.com/datasets/geo-countries/master/data/countries.geojson')
                        .then(response => response.json());
                })
                .then(data => {
                    console.log('✅ Dados geográficos carregados');
                    processWorldDataEmbedded(data);
                })
                .catch(error => {
                    console.error('❌ Erro ao carregar dados geográficos:', error);
                });
        }

        function processWorldDataEmbedded(data) {
            // Country name mapping for different naming conventions
            const countryNameMap = {
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
            };

            // Style function for each country
            function style(feature) {
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
                for (let name of possibleNames) {
                    if (name) {
                        countryName = name;
                        break;
                    }
                }
                
                if (!countryName) {
                    return {
                        fillColor: '#f0f0f0',
                        weight: 1,
                        opacity: 1,
                        color: 'white',
                        fillOpacity: 0.7
                    };
                }
                
                const mappedName = countryNameMap[countryName] || countryName;
                const sentiment = sentimentData[mappedName];
                const color = getSentimentColor(sentiment);
                
                return {
                    fillColor: color,
                    weight: 1,
                    opacity: 1,
                    color: 'white',
                    fillOpacity: 0.8
                };
            }
            
            // Function for each feature (country)
            function onEachFeature(feature, layer) {
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
                for (let name of possibleNames) {
                    if (name) {
                        countryName = name;
                        break;
                    }
                }
                
                if (!countryName) return;
                
                const mappedName = countryNameMap[countryName] || countryName;
                const sentiment = sentimentData[mappedName];
                const articles = articlesData[mappedName] || [];
                
                // Add popup only for countries with data
                if (sentiment !== undefined) {
                    const popupContent = createPopupContent(mappedName, sentiment, articles);
                    layer.bindPopup(popupContent, {
                        maxWidth: 300,
                        className: 'custom-popup'
                    });
                }
                
                // Add hover effects
                layer.on({
                    mouseover: function(e) {
                        const layer = e.target;
                        layer.setStyle({
                            weight: 3,
                            color: '#333',
                            fillOpacity: 0.9
                        });
                        layer.bringToFront();
                    },
                    mouseout: function(e) {
                        geojsonLayer.resetStyle(e.target);
                    }
                });
            }
            
            // Add GeoJSON layer to map
            geojsonLayer = L.geoJSON(data, {
                style: style,
                onEachFeature: onEachFeature
            }).addTo(sentimentMap);
            
            // Zoom to South America bounds
            zoomToSouthAmericaEmbedded();
            
            console.log('🎯 Mapa incorporado carregado');
        }
        
        // Function to zoom map to South America
        function zoomToSouthAmericaEmbedded() {
            // South America bounding box coordinates
            const southAmericaBounds = [
                [-56, -82], // Southwest corner (lat, lng) - covers southern Chile/Argentina
                [13, -34]   // Northeast corner (lat, lng) - covers northern Venezuela/Guyana
            ];
            
            // Fit map to South America bounds with padding
            sentimentMap.fitBounds(southAmericaBounds, {
                padding: [5, 5],
                maxZoom: 4
            });
        }

        // Initialize when DOM is ready
        if (document.readyState === 'loading') {
            document.addEventListener('DOMContentLoaded', initializeEmbeddedMap);
        } else {
            initializeEmbeddedMap();
        }
        
        // Also initialize when the map container becomes visible (in case it's initially hidden)
        const observer = new IntersectionObserver((entries) => {
            entries.forEach(entry => {
                if (entry.isIntersecting && sentimentMap) {
                    setTimeout(() => {
                        sentimentMap.invalidateSize();
                    }, 100);
                }
            });
        });
        
        const mapContainer = document.getElementById('sentiment-map');
        if (mapContainer) {
            observer.observe(mapContainer);
        }
    })();
