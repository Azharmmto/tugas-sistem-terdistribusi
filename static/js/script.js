// Theme Toggle Functionality
document.addEventListener('DOMContentLoaded', function() {
    // Initialize theme from localStorage or default to light
    const savedTheme = localStorage.getItem('theme') || 'light';
    document.documentElement.setAttribute('data-theme', savedTheme);
    
    // Theme toggle button
    const themeToggle = document.getElementById('theme-toggle');
    if (themeToggle) {
        themeToggle.addEventListener('click', function() {
            const currentTheme = document.documentElement.getAttribute('data-theme');
            const newTheme = currentTheme === 'light' ? 'dark' : 'light';
            
            document.documentElement.setAttribute('data-theme', newTheme);
            localStorage.setItem('theme', newTheme);
        });
    }
    
    // Load all data on page load
    loadWeather();
    loadCurrency();
    loadNews();
});

// Fungsi untuk mendapatkan emoji cuaca berdasarkan kondisi
function getWeatherEmoji(condition) {
    const weather = condition.toLowerCase();
    if (weather.includes('cerah') && !weather.includes('berawan')) {
        return '☀️'; // Cerah
    } else if (weather.includes('cerah berawan') || weather.includes('cerah-berawan')) {
        return '⛅'; // Cerah Berawan
    } else if (weather.includes('berawan')) {
        return '☁️'; // Berawan
    } else if (weather.includes('hujan lebat') || weather.includes('hujan petir')) {
        return '⛈️'; // Hujan Petir
    } else if (weather.includes('hujan')) {
        return '🌧️'; // Hujan
    } else if (weather.includes('petir') || weather.includes('badai')) {
        return '⚡'; // Petir/Badai
    } else if (weather.includes('kabut')) {
        return '🌫️'; // Kabut
    } else {
        return '🌤️'; // Default
    }
}

// Fungsi untuk load data cuaca
async function loadWeather() {
    const weatherContent = document.getElementById('weather-content');
    weatherContent.innerHTML = '<div class="loading">Memuat data cuaca...</div>';
    
    try {
        // Default kode wilayah Makassar (Karuwisi Utara)
        const response = await fetch('/api/weather?adm4=73.71.09.1009');
        const result = await response.json();
        
        if (result.status === 'success' && result.data.current_weather) {
            const weather = result.data.current_weather;
            const lokasi = result.data.lokasi;
            const weatherEmoji = getWeatherEmoji(weather.weather_desc);
            
            weatherContent.innerHTML = `
                <div class="weather-info">
                    <div class="weather-icon-temp">
                        <div class="weather-icon-large">${weatherEmoji}</div>
                        <div class="weather-temp">${weather.t}°C</div>
                    </div>
                    <div class="weather-condition">${weather.weather_desc}</div>
                    <div class="weather-details">
                        <div class="weather-item">
                            <strong>💨 Kecepatan Angin</strong>
                            ${weather.ws} km/h
                        </div>
                        <div class="weather-item">
                            <strong>🧭 Arah Angin</strong>
                            ${weather.wd} (${weather.wd_deg}°)
                        </div>
                        <div class="weather-item">
                            <strong>💧 Kelembaban</strong>
                            ${weather.hu}%
                        </div>
                        <div class="weather-item">
                            <strong>👁️ Jarak Pandang</strong>
                            ${weather.vs_text}
                        </div>
                        <div class="weather-item">
                            <strong>🕐 Waktu Update</strong>
                            ${new Date(weather.local_datetime).toLocaleString('id-ID')}
                        </div>
                    </div>
                    <p style="margin-top: 15px; color: #999; font-size: 0.9rem;">
                        ${lokasi.kecamatan}, ${lokasi.kotkab}, ${lokasi.provinsi}
                    </p>
                    <p style="margin-top: 5px; color: #999; font-size: 0.9rem;">
                        Sumber data: <a href="https://bmkg.go.id/" target="_blank">BMKG (Badan Meteorologi, Klimatologi, dan Geofisika)</a>
                    </p>
                </div>
            `;
        } else {
            throw new Error(result.message || 'Data cuaca tidak tersedia');
        }
    } catch (error) {
        weatherContent.innerHTML = `<div class="error">Gagal memuat data cuaca: ${error.message}</div>`;
    }
}

// Fungsi untuk load nilai tukar mata uang
async function loadCurrency() {
    const currencyContent = document.getElementById('currency-content');
    currencyContent.innerHTML = '<div class="loading">Memuat data mata uang...</div>';
    
    try {
        const response = await fetch('/api/currency');
        const result = await response.json();
        
        if (result.status === 'success') {
            const data = result.data;
            const rates = data.rates;
            
            let html = `<p style="margin-bottom: 15px; color: #999;">Base: ${data.base} (${data.date})</p>`;
            html += '<ul class="currency-list">';
            
            for (const [currency, rate] of Object.entries(rates)) {
                html += `
                    <li class="currency-item">
                        <span class="currency-name">${currency}</span>
                        <span class="currency-rate">${rate.toFixed(2)}</span>
                    </li>
                `;
            }
            
            html += '</ul>';
            currencyContent.innerHTML = html;
        } else {
            throw new Error(result.message);
        }
    } catch (error) {
        currencyContent.innerHTML = `<div class="error">Gagal memuat data mata uang: ${error.message}</div>`;
    }
}

// Extract image URL from various API response formats
function extractImageUrl(article) {
    // Priority order: thumbnail > image > poster > urlToImage > enclosure
    if (article.thumbnail) return article.thumbnail;
    if (article.image) return article.image;
    if (article.poster) return article.poster;
    if (article.urlToImage) return article.urlToImage;
    
    // Check enclosure object (common in RSS feeds)
    if (article.enclosure && article.enclosure.url) return article.enclosure.url;
    
    // Check media array (some APIs use this)
    if (article.media && Array.isArray(article.media) && article.media.length > 0) {
        return article.media[0].url || article.media[0].link;
    }
    
    return null;
}

// Fungsi untuk load berita dengan rich media support
async function loadNews() {
    const newsContent = document.getElementById('news-content');
    newsContent.innerHTML = '<div class="loading"><div class="loading-spinner"></div><p>Memuat berita...</p></div>';
    
    try {
        const response = await fetch('/api/news');
        const result = await response.json();
        
        if (result.status === 'success') {
            const articles = result.data.articles;
            
            if (articles.length === 0) {
                newsContent.innerHTML = '<p style="text-align: center; color: var(--text-tertiary); padding: var(--spacing-xl);">Tidak ada berita tersedia</p>';
                return;
            }
            
            let html = '<ul class="news-list">';
            
            articles.forEach((article, index) => {
                if (article.title && article.title !== '[Removed]') {
                    // Extract image from multiple possible fields
                    const imageUrl = extractImageUrl(article);
                    const hasImage = imageUrl && imageUrl.trim() !== '';
                    
                    // Create image element with error handling
                    const imageHtml = hasImage 
                        ? `<img src="${imageUrl}" alt="${article.title}" class="news-image" loading="lazy" onerror="this.parentElement.innerHTML='<div class=\\'news-image-placeholder\\'>📰</div>'">` 
                        : '<div class="news-image-placeholder">📰</div>';
                    
                    html += `
                        <li class="news-item">
                            <div class="news-image-wrapper">
                                ${imageHtml}
                            </div>
                            <div class="news-content">
                                <span class="news-title">${article.title}</span>
                                ${article.description ? `<p class="news-description">${article.description}</p>` : ''}
                                <a href="${article.url}" target="_blank" class="news-link">
                                    Baca selengkapnya
                                    <svg width="12" height="12" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
                                        <path d="M5 12h14M12 5l7 7-7 7"/>
                                    </svg>
                                </a>
                            </div>
                        </li>
                    `;
                }
            });
            
            html += '</ul>';
            newsContent.innerHTML = html;
        } else {
            throw new Error(result.message);
        }
    } catch (error) {
        newsContent.innerHTML = `<div class="error">Gagal memuat berita: ${error.message}</div>`;
    }
}

// Fungsi untuk mengirim daily briefing via Telegram
async function sendBriefing(event) {
    event.preventDefault();
    
    const telegramInput = document.getElementById('telegram-input');
    const telegramId = telegramInput.value.trim();
    const statusDiv = document.getElementById('briefing-status');
    
    // Validasi Telegram ID
    if (!/^\d+$/.test(telegramId)) {
        statusDiv.innerHTML = '<div class="error">✗ Telegram ID harus berupa angka</div>';
        setTimeout(() => { statusDiv.innerHTML = ''; }, 3000);
        return;
    }
    
    // Show loading
    statusDiv.innerHTML = '<div class="loading">Mengirim daily briefing ke Telegram...</div>';
    
    try {
        const response = await fetch('/api/send-briefing', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
            },
            body: JSON.stringify({ telegram_id: telegramId })
        });
        
        const result = await response.json();
        
        if (result.status === 'success') {
            statusDiv.innerHTML = `<div class="success">✓ ${result.message}</div>`;
            telegramInput.value = '';
        } else {
            throw new Error(result.message);
        }
    } catch (error) {
        statusDiv.innerHTML = `<div class="error">✗ Gagal mengirim: ${error.message}</div>`;
    }
    
    // Clear status after 5 seconds
    setTimeout(() => {
        statusDiv.innerHTML = '';
    }, 5000);
}

// Footer Subscribe Handler
async function handleFooterSubscribe(event) {
    event.preventDefault();
    
    const form = event.target;
    const input = form.querySelector('.subscribe-input');
    const button = form.querySelector('.subscribe-btn');
    const email = input.value.trim();
    
    if (!email) {
        return;
    }
    
    // Save original button content
    const originalContent = button.innerHTML;
    
    // Show loading state
    button.innerHTML = '<svg class="loading-spinner" width="16" height="16" viewBox="0 0 24 24"><circle cx="12" cy="12" r="10" stroke="currentColor" stroke-width="3" fill="none" opacity="0.3"/><circle cx="12" cy="12" r="10" stroke="currentColor" stroke-width="3" fill="none" stroke-dasharray="60" stroke-dashoffset="15" style="animation: spin 1s linear infinite;"/></svg>';
    button.disabled = true;
    
    try {
        // Simulate API call (replace with your actual endpoint)
        await new Promise(resolve => setTimeout(resolve, 1500));
        
        // Success animation
        button.innerHTML = '<svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="3"><polyline points="20 6 9 17 4 12"/></svg>';
        button.style.background = 'linear-gradient(135deg, #10b981 0%, #059669 100%)';
        
        // Clear input
        input.value = '';
        
        // Reset button after 2 seconds
        setTimeout(() => {
            button.innerHTML = originalContent;
            button.style.background = '';
            button.disabled = false;
        }, 2000);
        
    } catch (error) {
        // Error state
        button.innerHTML = '<svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="3"><line x1="18" y1="6" x2="6" y2="18"/><line x1="6" y1="6" x2="18" y2="18"/></svg>';
        button.style.background = 'linear-gradient(135deg, #ef4444 0%, #dc2626 100%)';
        
        setTimeout(() => {
            button.innerHTML = originalContent;
            button.style.background = '';
            button.disabled = false;
        }, 2000);
    }
}
