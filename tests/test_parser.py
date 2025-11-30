"""
Tests for TripCraft AI natural language parser
"""
import pytest
from src.utils import parse_travel_request

class TestTravelParser:
    """Test suite for travel request parsing"""
    
    def test_basic_parsing(self):
        """Test basic travel request parsing"""
        result = parse_travel_request("Budget travel to Tokyo for 5 days")
        
        assert result['destination'] == 'Tokyo'
        assert result['duration'] == 5
        assert result['style'] == 'budget'
        assert 'culture' in result['interests'] or 'food' in result['interests']
    
    def test_budget_extraction(self):
        """Test budget extraction from requests"""
        result = parse_travel_request("I want to visit Paris with $1500 budget")
        
        assert result['destination'] == 'Paris'
        assert result['budget'] == 1500
    
    def test_luxury_style_detection(self):
        """Test luxury travel style detection"""
        result = parse_travel_request("Luxury trip to Dubai")
        
        assert result['destination'] == 'Dubai'
        assert result['style'] == 'luxury'
    
    def test_interest_extraction(self):
        """Test interest category extraction"""
        result = parse_travel_request("I love food and shopping in Bangkok")
        
        assert result['destination'] == 'Bangkok'
        assert 'food' in result['interests']
        assert 'shopping' in result['interests']
    
    def test_default_values(self):
        """Test default value assignment"""
        result = parse_travel_request("Just want to travel somewhere")
        
        assert result['destination'] == 'Tokyo'  # Default
        assert result['budget'] == 2000  # Default
        assert result['duration'] == 5  # Default
        assert len(result['interests']) > 0  # Default interests

if __name__ == "__main__":
    pytest.main([__file__])