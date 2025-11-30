"""
Tests for TripCraft AI tools
"""
import pytest
from src.tools import (
    search_flights_ultimate,
    find_hotels_ultimate,
    save_user_preferences_ultimate,
    aggregate_travel_results_ultimate
)
from src.main import MockToolContext

class TestTravelTools:
    """Test suite for travel planning tools"""
    
    def setup_method(self):
        """Setup test context"""
        self.context = MockToolContext("test_user", "test_session")
    
    def test_search_flights_ultimate(self):
        """Test flight search functionality"""
        result = search_flights_ultimate("Tokyo", "2024-02-01", "2024-02-06", self.context)
        
        assert result['status'] == 'success'
        assert result['destination'] == 'Tokyo'
        assert 'flights' in result
        assert len(result['flights']) > 0
        assert 'search_context' in result
    
    def test_find_hotels_ultimate(self):
        """Test hotel search functionality"""
        result = find_hotels_ultimate("Tokyo", "2024-02-01", "2024-02-06", 100.0, 2, self.context)
        
        assert result['status'] == 'success'
        assert result['destination'] == 'Tokyo'
        assert 'hotels' in result
        assert len(result['hotels']) > 0
        assert 'search_context' in result
    
    def test_save_user_preferences_ultimate(self):
        """Test user preference saving"""
        result = save_user_preferences_ultimate("test_user", self.context)
        
        assert result['status'] == 'success'
        assert result['user_id'] == 'test_user'
        assert 'preferences_saved' in result
    
    def test_aggregate_travel_results_ultimate(self):
        """Test result aggregation"""
        # Create mock data
        flights = {'flights': [{'price': 500}], 'destination': 'Tokyo'}
        hotels = {'hotels': [{'price_per_night': 100}]}
        preferences = {'status': 'success'}
        
        result = aggregate_travel_results_ultimate(flights, hotels, preferences, self.context)
        
        assert 'destination' in result
        assert 'budget_analysis' in result
        assert 'flights' in result
        assert 'hotels' in result

if __name__ == "__main__":
    pytest.main([__file__])