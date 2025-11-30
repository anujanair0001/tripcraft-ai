"""
Natural language parsing utilities for travel requests
"""
import re
from typing import Dict, List
from config import TRAVEL_DEFAULTS

def parse_travel_request(user_input: str) -> Dict:
    """
    Parse natural language travel request into structured data
    
    Args:
        user_input: Natural language travel request
        
    Returns:
        Dictionary with parsed travel information
    """
    user_lower = user_input.lower()
    
    # Extract destination using multiple patterns
    patterns = [
        r'to\s+([A-Za-z]+)', 
        r'visit\s+([A-Za-z]+)', 
        r'travel\s+to\s+([A-Za-z]+)',
        r'going\s+to\s+([A-Za-z]+)',
        r'trip\s+to\s+([A-Za-z]+)'
    ]
    
    destination = TRAVEL_DEFAULTS["default_destination"]
    for pattern in patterns:
        match = re.search(pattern, user_input, re.IGNORECASE)
        if match:
            destination = match.group(1).title()
            break
    
    # Extract budget with currency handling
    budget_match = re.findall(r'\$?(\d+)', user_input)
    budget = int(budget_match[-1]) if budget_match else TRAVEL_DEFAULTS["default_budget"]
    
    # Extract duration
    dur = re.search(r'(\d+)\s*days?', user_input)
    duration = int(dur.group(1)) if dur else TRAVEL_DEFAULTS["default_duration"]
    
    # Classify travel style
    if any(word in user_lower for word in ['budget', 'cheap', 'affordable', 'low-cost']):
        style = 'budget'
    elif any(word in user_lower for word in ['luxury', 'premium', 'high-end', 'expensive']):
        style = 'luxury'
    else:
        style = TRAVEL_DEFAULTS["default_style"]
    
    # Extract interests
    interest_keywords = {
        'culture': ['culture', 'history', 'museum', 'art', 'heritage', 'traditional'],
        'food': ['food', 'cuisine', 'restaurant', 'dining', 'culinary', 'local food'],
        'shopping': ['shopping', 'market', 'shop', 'boutique', 'mall', 'souvenirs'],
        'adventure': ['adventure', 'hiking', 'outdoor', 'sports', 'activities', 'nature'],
        'nightlife': ['nightlife', 'bars', 'clubs', 'entertainment', 'party'],
        'relaxation': ['relax', 'spa', 'beach', 'peaceful', 'quiet', 'wellness']
    }
    
    interests = []
    for category, keywords in interest_keywords.items():
        if any(keyword in user_lower for keyword in keywords):
            interests.append(category)
    
    if not interests:
        interests = TRAVEL_DEFAULTS["default_interests"]
    
    return {
        'destination': destination,
        'budget': budget,
        'duration': duration,
        'style': style,
        'interests': interests,
        'original_request': user_input
    }