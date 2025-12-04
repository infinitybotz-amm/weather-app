/* ===== WEATHER APP JAVASCRIPT ===== */

// Weather App State
const appState = {
    recentSearches: JSON.parse(localStorage.getItem('recentSearches')) || []
};
// Murali: Added to manage recent searches
// DOM Elements
const cityInput = document.getElementById('cityInput');
const searchBtn = document.getElementById('searchBtn');
const currentLocationBtn = document.getElementById('currentLocationBtn');
const errorMsg = document.getElementById('errorMsg');
const loading = document.getElementById('loading');
const weatherResult = document.getElementById('weatherResult');
const recentSearchesDiv = document.getElementById('recentSearches');

// In-memory suggestions store for the current result.
let currentSuggestions = [];

// Event Listeners
searchBtn.addEventListener('click', () => {
    const city = cityInput.value.trim();
    if (city) {
        fetchWeather(city);
    }
});

cityInput.addEventListener('keypress', (e) => {
    if (e.key === 'Enter') {
        const city = cityInput.value.trim();
        if (city) {
            fetchWeather(city);
        }
    }
});

currentLocationBtn.addEventListener('click', getLocationWeather);

// Fetch Weather Data
async function fetchWeather(city) {
    try {
        // Show loading, hide error
        loading.classList.remove('hidden');
        weatherResult.classList.add('hidden');
        errorMsg.classList.remove('show');
        errorMsg.textContent = '';

        // Make API call
        const response = await fetch('/api/weather', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify({ city })
        });

        if (!response.ok) {
            throw new Error('City not found or API error');
        }

        const data = await response.json();

        // Hide loading
        loading.classList.add('hidden');

        // Display weather
        displayWeather(data);

        // Add to recent searches
        addRecentSearch(city);

        // Clear input
        cityInput.value = '';

    } catch (error) {
        loading.classList.add('hidden');
        weatherResult.classList.add('hidden');
        showError('❌ ' + error.message);
    }
}

// Display Weather Data
function displayWeather(data) {
    // Update header
    document.getElementById('cityName').textContent = data.city || '-';
    document.getElementById('countryName').textContent = data.country || '-';
    document.getElementById('lastUpdated').textContent = `Updated: ${data.timestamp}`;

    // Update temperature
    document.getElementById('temperature').textContent = data.temperature;
    document.getElementById('temperatureF').textContent = `${data.temperature_f}°F`;
    document.getElementById('feelsLike').textContent = `Feels like: ${data.feels_like}°C`;

    // Update condition
    document.getElementById('conditionText').textContent = data.condition;
    document.getElementById('weatherCondition').textContent = data.condition;

    // Update wind
    document.getElementById('windSpeed').textContent = data.wind_speed;

    // Update humidity
    document.getElementById('humidityText').textContent = `${data.humidity}%`;
    document.getElementById('humidityBar').style.width = `${data.humidity}%`;

    // Update visibility
    document.getElementById('visibility').textContent = data.visibility;

    // Update pressure
    document.getElementById('pressure').textContent = data.pressure;

    // Update cloud cover
    document.getElementById('cloudText').textContent = `${data.cloudcover}%`;
    document.getElementById('cloudBar').style.width = `${data.cloudcover}%`;

    // Update precipitation
    document.getElementById('precipitation').textContent = data.precipitation;

    // Update UV index
    document.getElementById('uvIndex').textContent = data.uv_index;

    // Store suggestions and show/hide the toggle button (we'll wire the listener on DOMContentLoaded)
    currentSuggestions = data.suggestions || [];
    const showBtn = document.getElementById('showSuggestionsBtn');
    const section = document.getElementById('suggestionsSection');
    if (currentSuggestions.length > 0) {
        // make sure suggestions are hidden until user opens them
        if (section) section.classList.add('hidden');
        if (showBtn) {
            // remove any 'hidden' class and set inline display to be robust across builds/caches
            showBtn.classList.remove('hidden');
            showBtn.style.display = 'inline-block';
            showBtn.textContent = 'Places to visit';
            console.log('[weather] Showing suggestions toggle (count:', currentSuggestions.length, ')');
        }
    } else {
        if (showBtn) {
            showBtn.classList.add('hidden');
            showBtn.style.display = 'none';
        }
        if (section) section.classList.add('hidden');
    }

    // Show result
    weatherResult.classList.remove('hidden');
}

// Display suggestions under the weather result
function displaySuggestions(suggestions) {
    const section = document.getElementById('suggestionsSection');
    const list = document.getElementById('suggestionsList');

    list.innerHTML = '';

    if (!suggestions || suggestions.length === 0) {
        section.classList.add('hidden');
        return;
    }

    suggestions.forEach(item => {
        const card = document.createElement('div');
        card.className = 'suggestion-card';

        const title = document.createElement('h4');
        title.textContent = item.name || 'Unknown';
        card.appendChild(title);

        if (item.desc) {
            const desc = document.createElement('p');
            desc.className = 'suggestion-desc';
            desc.textContent = item.desc;
            card.appendChild(desc);
        }

        if (item.category) {
            const cat = document.createElement('span');
            cat.className = 'suggestion-cat';
            cat.textContent = item.category;
            card.appendChild(cat);
        }

        list.appendChild(card);
    });

    section.classList.remove('hidden');
}

// Show Error Message
function showError(message) {
    errorMsg.textContent = message;
    errorMsg.classList.add('show');
    setTimeout(() => {
        errorMsg.classList.remove('show');
    }, 5000);
}

// Add to Recent Searches
function addRecentSearch(city) {
    // Remove if already exists
    appState.recentSearches = appState.recentSearches.filter(
        item => item.toLowerCase() !== city.toLowerCase()
    );

    // Add to beginning
    appState.recentSearches.unshift(city);

    // Keep only 5 recent searches
    appState.recentSearches = appState.recentSearches.slice(0, 5);

    // Save to localStorage
    localStorage.setItem('recentSearches', JSON.stringify(appState.recentSearches));

    // Update display
    displayRecentSearches();
}

// Display Recent Searches
function displayRecentSearches() {
    recentSearchesDiv.innerHTML = '';

    if (appState.recentSearches.length === 0) {
        recentSearchesDiv.innerHTML = '<p style="color: #999;">No recent searches</p>';
        return;
    }

    appState.recentSearches.forEach(city => {
        const item = document.createElement('button');
        item.className = 'recent-item';
        item.textContent = city;
        item.addEventListener('click', () => fetchWeather(city));
        recentSearchesDiv.appendChild(item);
    });
}

// Get Weather for Current Location
function getLocationWeather() {
    if (!navigator.geolocation) {
        showError('❌ Geolocation is not supported by your browser');
        return;
    }

    navigator.geolocation.getCurrentPosition(
        (position) => {
            const { latitude, longitude } = position.coords;
            fetchWeatherByCoordinates(latitude, longitude);
        },
        (error) => {
            showError(`❌ Could not get location: ${error.message}`);
        }
    );
}

// Fetch Weather by Coordinates
async function fetchWeatherByCoordinates(lat, lon) {
    try {
        loading.classList.remove('hidden');
        weatherResult.classList.add('hidden');
        errorMsg.classList.remove('show');

        // Use wttr.in API with coordinates (approximate using wttr.in feature)
        const response = await fetch(`/api/weather/~${lat},${lon}`);

        if (!response.ok) {
            throw new Error('Could not fetch weather for your location');
        }

        const data = await response.json();
        loading.classList.add('hidden');
        displayWeather(data);
        addRecentSearch(`📍 ${data.city}`);

    } catch (error) {
        loading.classList.add('hidden');
        showError('❌ ' + error.message);
    }
}

// Initialize App
document.addEventListener('DOMContentLoaded', () => {
    displayRecentSearches();
    // Wire up suggestions toggle button (lookup when DOM is ready)
    const showSuggestionsBtn = document.getElementById('showSuggestionsBtn');
    if (showSuggestionsBtn) {
        // start hidden until a search returns suggestions
        showSuggestionsBtn.classList.add('hidden');
        showSuggestionsBtn.style.display = 'none';
        console.log('[weather] showSuggestionsBtn wired on DOMContentLoaded');
        showSuggestionsBtn.addEventListener('click', () => {
            const section = document.getElementById('suggestionsSection');
            if (!section) return;

            if (section.classList.contains('hidden')) {
                // show suggestions (render currentSuggestions)
                displaySuggestions(currentSuggestions || []);
                showSuggestionsBtn.textContent = 'Hide places';
            } else {
                section.classList.add('hidden');
                showSuggestionsBtn.textContent = 'Places to visit';
            }
        });
    }
});

// Optional: Example cities
document.addEventListener('load', () => {
    // You can add a button to load example cities
});
