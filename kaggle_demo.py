"""
TripCraft AI - Kaggle/Jupyter Compatible Demo
Built with AI Agent Development Kit (ADK)
"""

import random
import json
from datetime import datetime
from typing import Dict, Any

# Simple context class for Kaggle environment
class SimpleToolContext:
    def __init__(self, user_id: str = "kaggle_user"):
        self.user_id = user_id
        self.session_id = f"session_{random.randint(1000, 9999)}"

# Memory storage for demo
_DEMO_MEMORY = {}

def save_memory_demo(key: str, data: Any, user_id: str = "default"):
    """Simple memory save for demo"""
    memory_key = f"{key}_{user_id}"
    _DEMO_MEMORY[memory_key] = data
    return True

def parse_travel_request_demo(user_input: str) -> Dict:
    """Simple travel request parser for demo"""
    user_lower = user_input.lower()
    
    # Extract destination
    destination = "Tokyo"  # Default
    if "paris" in user_lower:
        destination = "Paris"
    elif "london" in user_lower:
        destination = "London"
    elif "bangkok" in user_lower:
        destination = "Bangkok"
    
    # Extract budget
    budget = 2000  # Default
    if "budget" in user_lower or "cheap" in user_lower:
        budget = 1500
    elif "luxury" in user_lower or "premium" in user_lower:
        budget = 5000
    
    # Extract duration
    duration = 5  # Default
    if "3 days" in user_input or "3 day" in user_input:
        duration = 3
    elif "7 days" in user_input or "7 day" in user_input:
        duration = 7
    
    return {
        'destination': destination,
        'budget': budget,
        'duration': duration,
        'style': 'budget' if budget < 2000 else 'luxury',
        'interests': ['culture', 'food']
    }

def search_flights_demo(destination: str, depart_date: str, return_date: str, context) -> Dict[str, Any]:
    """Demo flight search function"""
    print(f"🔍 Searching flights to {destination}...")
    
    # Mock flight data
    base_prices = {
        'tokyo': 800, 'paris': 650, 'london': 600, 'bangkok': 450
    }
    
    base_price = base_prices.get(destination.lower(), 600)
    airlines = ['Emirates', 'Singapore Airlines', 'Qatar Airways', 'Lufthansa']
    
    flights = []
    for i in range(2):
        price = base_price + random.randint(-100, 200)
        flights.append({
            'id': f'FL-{destination.upper()}-{i+1}',
            'airline': random.choice(airlines),
            'price': price,
            'duration': f"{random.randint(8, 16)}h {random.randint(0, 59)}m",
            'stops': random.choice([0, 1])
        })
    
    result = {
        'status': 'success',
        'destination': destination,
        'flights': flights
    }
    
    # Save to demo memory
    save_memory_demo(f"flight_search_{destination}", result, context.user_id)
    
    return result

def find_hotels_demo(destination: str, checkin: str, checkout: str, budget_per_night: float, guests: int, context) -> Dict[str, Any]:
    """Demo hotel search function"""
    print(f"🏨 Searching hotels in {destination}...")
    
    # Mock hotel data
    base_prices = {'tokyo': 120, 'paris': 95, 'london': 110, 'bangkok': 25}
    base_price = base_prices.get(destination.lower(), 80)
    hotel_chains = ['Marriott', 'Hilton', 'Hyatt', 'InterContinental']
    
    hotels = []
    for i in range(2):
        price = max(20, min(budget_per_night * 1.2, base_price + random.randint(-20, 40)))
        hotels.append({
            'id': f'HT-{destination.upper()}-{i+1}',
            'name': f'{random.choice(hotel_chains)} {destination}',
            'rating': round(3.5 + random.random() * 1.5, 1),
            'price_per_night': int(price)
        })
    
    return {
        'status': 'success',
        'destination': destination,
        'hotels': hotels
    }

def run_minimal_demo(request: str = 'Budget Travel to Tokyo'):
    """Minimal demo for Kaggle/Jupyter"""
    print("🚀 TripCraft AI - Kaggle Demo")
    print("=" * 40)
    
    # Parse request
    parsed = parse_travel_request_demo(request)
    print(f"📝 Request: {request}")
    print(f"🎯 Parsed: {parsed}")
    
    # Create context
    context = SimpleToolContext()
    print(f"🔧 Session: {context.session_id}")
    
    # Search flights
    flights = search_flights_demo(
        parsed['destination'], 
        '2024-02-01', 
        '2024-02-06', 
        context
    )
    
    # Search hotels
    hotels = find_hotels_demo(
        parsed['destination'],
        '2024-02-01',
        '2024-02-06',
        parsed['budget'] / parsed['duration'],
        2,
        context
    )
    
    # Display results
    print(f"\n✈️ FLIGHTS to {flights['destination']}:")
    for flight in flights['flights']:
        print(f"   {flight['airline']}: ${flight['price']} ({flight['duration']})")
    
    print(f"\n🏨 HOTELS in {hotels['destination']}:")
    for hotel in hotels['hotels']:
        print(f"   {hotel['name']}: ${hotel['price_per_night']}/night (⭐{hotel['rating']})")
    
    # Budget analysis
    min_flight = min(f['price'] for f in flights['flights'])
    min_hotel = min(h['price_per_night'] for h in hotels['hotels'])
    total_cost = min_flight + (min_hotel * parsed['duration'])
    
    print(f"\n💰 BUDGET ANALYSIS:")
    print(f"   Flight: ${min_flight}")
    print(f"   Hotels: ${min_hotel}/night × {parsed['duration']} nights = ${min_hotel * parsed['duration']}")
    print(f"   Total: ${total_cost}")
    
    print(f"\n🎉 Demo completed! Memory keys: {len(_DEMO_MEMORY)}")
    
    return {
        'flights': flights,
        'hotels': hotels,
        'total_cost': total_cost,
        'parsed_request': parsed
    }

# Run the demo
if __name__ == "__main__":
    result = run_minimal_demo('Budget Travel to Tokyo')