// Load semua data saat halaman dimuat
document.addEventListener('DOMContentLoaded', function() {
    loadWeather();
    loadCurrency();
    loadNews();
});

// Fungsi untuk load data cuaca
async function loadWeather() {
    const weatherContent = document.getElementById('weather-content');
    weatherContent.innerHTML = '<div class="loading">Memuat data cuaca...</div>';
    
    try {
        // Default koordinat Jakarta
        const response = await fetch('/api/weather?lat=-5.1477&lon=119.4327');;
        const result = await response.json();
        
        if (result.status === 'success') {
            const weather = result.data.current_weather;
            weatherContent.innerHTML = `
                <div class="weather-info">
                    <div class="weather-temp">${weather.temperature}°C</div>
                    <div class="weather-details">
                        <div class="weather-item">
                            <strong>Kecepatan Angin</strong>
                            ${weather.windspeed} km/h
                        </div>
                        <div class="weather-item">
                            <strong>Arah Angin</strong>
                            ${weather.winddirection}°
                        </div>
                        <div class="weather-item">
                            <strong>Waktu</strong>
                            ${new Date(weather.time).toLocaleString('id-ID')}
                        </div>
                        <div class="weather-item">
                            <strong>Kondisi</strong>
                            Cuaca Code: ${weather.weathercode}
                        </div>
                    </div>
                    <p style="margin-top: 15px; color: #999; font-size: 0.9rem;">Lokasi: Makassar, Indonesia</p>
                </div>
            `;
        } else {
            throw new Error(result.message);
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

// Fungsi untuk load berita
async function loadNews() {
    const newsContent = document.getElementById('news-content');
    newsContent.innerHTML = '<div class="loading">Memuat berita...</div>';
    
    try {
        const response = await fetch('/api/news');
        const result = await response.json();
        
        if (result.status === 'success') {
            const articles = result.data.articles;
            
            if (articles.length === 0) {
                newsContent.innerHTML = '<p style="text-align: center; color: #999;">Tidak ada berita tersedia</p>';
                return;
            }
            
            let html = '<ul class="news-list">';
            
            articles.forEach(article => {
                if (article.title && article.title !== '[Removed]') {
                    html += `
                        <li class="news-item">
                            <span class="news-title">${article.title}</span>
                            <p class="news-description">${article.description || 'Tidak ada deskripsi'}</p>
                            <a href="${article.url}" target="_blank" class="news-link">Baca selengkapnya →</a>
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
