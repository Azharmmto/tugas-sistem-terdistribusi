"""
Unit tests untuk Distributed Systems Dashboard
"""
import unittest
import json
from app import app

class TestDistributedSystemsDashboard(unittest.TestCase):
    """Test cases untuk API endpoints"""
    
    def setUp(self):
        """Setup test client"""
        self.app = app
        self.app.config['TESTING'] = True
        self.client = self.app.test_client()
    
    def test_index_route(self):
        """Test homepage route"""
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'Distributed Systems Dashboard', response.data)
    
    def test_weather_endpoint(self):
        """Test weather API endpoint"""
        response = self.client.get('/api/weather')
        self.assertEqual(response.status_code, 200)
        data = json.loads(response.data)
        self.assertEqual(data['status'], 'success')
        self.assertIn('data', data)
        self.assertIn('timestamp', data)
    
    def test_quote_endpoint(self):
        """Test quote API endpoint"""
        response = self.client.get('/api/quote')
        self.assertEqual(response.status_code, 200)
        data = json.loads(response.data)
        self.assertEqual(data['status'], 'success')
        self.assertIn('data', data)
        self.assertIn('content', data['data'])
        self.assertIn('author', data['data'])
    
    def test_currency_endpoint(self):
        """Test currency API endpoint"""
        response = self.client.get('/api/currency')
        self.assertEqual(response.status_code, 200)
        data = json.loads(response.data)
        self.assertEqual(data['status'], 'success')
        self.assertIn('data', data)
        self.assertIn('rates', data['data'])
    
    def test_news_endpoint(self):
        """Test news API endpoint"""
        response = self.client.get('/api/news')
        self.assertEqual(response.status_code, 200)
        data = json.loads(response.data)
        self.assertEqual(data['status'], 'success')
        self.assertIn('data', data)
        self.assertIn('articles', data['data'])
    
    def test_health_endpoint(self):
        """Test health check endpoint"""
        response = self.client.get('/api/health')
        self.assertEqual(response.status_code, 200)
        data = json.loads(response.data)
        self.assertEqual(data['status'], 'healthy')
        self.assertIn('service', data)
        self.assertIn('timestamp', data)
    
    def test_weather_with_params(self):
        """Test weather endpoint with custom coordinates"""
        response = self.client.get('/api/weather?lat=-7.2575&lon=112.7521')
        self.assertEqual(response.status_code, 200)
        data = json.loads(response.data)
        self.assertEqual(data['status'], 'success')

if __name__ == '__main__':
    unittest.main()
