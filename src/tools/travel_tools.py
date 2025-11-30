"""
Core travel planning tools for TripCraft AI
Built with AI Agent Development Kit (ADK)
"""
# AI Agent Development Kit imports
try:
    from amazon_adk import LlmAgent, ParallelAgent, SequentialAgent, InMemoryRunner
    from amazon_adk.tools import ToolContext
except ImportError:
    # Fallback for development without ADK
    pass

import random
from datetime import datetime
from typing import Dict, Any, List
from config import logger
from utils.memory import save_memory, load_memory

def search_flights_ultimate(destination: str, depart_date: str, return_date: str, context) -> Dict[str, Any]:
    """
    Advanced flight search with multi-parameter filtering
    
    Args:
        destination: Travel destination
        depart_date: Departure date
        return_date: Return date
        context: Tool context with user information
        
    Returns:
        Dictionary with flight search results
    """
    user_id = getattr(context, 'user_id', 'anonymous')
    logger.info(f"[search_flights_ultimate] user={user_id} {destination}->{depart_date} {return_date} passengers=1")
    
    # Mock flight data with realistic pricing
    base_prices = {
        'tokyo': 800, 'paris': 650, 'london': 600, 'bangkok': 450,
        'singapore': 500, 'sydney': 900, 'dubai': 550, 'mumbai': 400
    }
    
    base_price = base_prices.get(destination.lower(), 600)
    
    flights = []
    airlines = ['Emirates', 'Singapore Airlines', 'Qatar Airways', 'Lufthansa', 'British Airways']
    
    for i in range(2):
        price = base_price + random.randint(-100, 200)
        flights.append({
            'id': f'FL-{destination.upper()}-{i+1}',
            'airline': random.choice(airlines),
            'price': price,
            'duration': f"{random.randint(8, 16)}h {random.randint(0, 59)}m",
            'aircraft': random.choice(['Boeing 777', 'Airbus A350', 'Boeing 787']),
            'departure': {
                'airport': 'Origin Airport',
                'datetime': f'{depart_date}T{random.randint(6, 23):02d}:00:00'
            },
            'arrival': {
                'airport': f'{destination} International',
                'datetime': f'{depart_date}T{random.randint(6, 23):02d}:00:00'
            },
            'stops': random.choice([0, 1]),
            'cabin': 'economy',
            'fare': {
                'amount': price,
                'currency': 'USD',
                'refundable': random.choice([True, False]),
                'baggage': '1x23kg'
            },
            'amenities': random.sample(['WiFi', 'Meals', 'Entertainment', 'Power'], 3)
        })
    
    result = {
        'status': 'success',
        'destination': destination,
        'flights': flights,
        'search_context': {
            'user_id': user_id,
            'session_id': getattr(context, 'session_id', 'default'),
            'timestamp': datetime.now().isoformat(),
            'search_type': 'flight_search'
        }
    }
    
    # Save to memory
    save_memory(f"flight_search_{destination}", result, user_id)
    
    return result

def find_hotels_ultimate(destination: str, checkin: str, checkout: str, budget_per_night: float, guests: int, context) -> Dict[str, Any]:
    """
    Intelligent accommodation discovery with budget optimization
    
    Args:
        destination: Travel destination
        checkin: Check-in date
        checkout: Check-out date
        budget_per_night: Budget per night
        guests: Number of guests
        context: Tool context
        
    Returns:
        Dictionary with hotel search results
    """
    user_id = getattr(context, 'user_id', 'anonymous')
    logger.info(f"[find_hotels_ultimate] user={user_id} destination={destination} {checkin}->{checkout} budget={budget_per_night}")
    
    # Mock hotel data with location-based pricing
    base_prices = {
        'tokyo': 120, 'paris': 95, 'london': 110, 'bangkok': 25,
        'singapore': 80, 'sydney': 130, 'dubai': 90, 'mumbai': 35
    }
    
    base_price = base_prices.get(destination.lower(), budget_per_night)
    
    hotels = []
    hotel_chains = ['Marriott', 'Hilton', 'Hyatt', 'InterContinental', 'Sheraton']
    
    for i in range(2):
        price = max(20, min(budget_per_night * 1.2, base_price + random.randint(-20, 40)))
        hotels.append({
            'id': f'HT-{destination.upper()}-{i+1}',
            'name': f'{random.choice(hotel_chains)} {destination}',
            'rating': round(3.5 + random.random() * 1.5, 1),
            'price_per_night': int(price),
            'currency': 'USD',
            'address': f'{destination} City Center, District {i+1}',
            'distance_to_center_km': round(0.5 + i * 1.5, 1),
            'amenities': random.sample([
                'WiFi', 'Pool', 'Gym', 'Spa', 'Restaurant', 'Bar', 
                'Room Service', 'Concierge', 'Business Center'
            ], 5),
            'room_types': [
                {
                    'type': 'Standard Room',
                    'beds': random.choice([1, 2]),
                    'max_guests': guests,
                    'size_sqm': random.randint(25, 40)
                }
            ],
            'policies': {
                'cancellation': 'Free cancellation until 24h before check-in',
                'payment': 'Pay at hotel or online',
                'pets': random.choice(['Allowed', 'Not allowed'])
            }
        })
    
    result = {
        'status': 'success',
        'destination': destination,
        'hotels': hotels,
        'search_context': {
            'user_id': user_id,
            'budget_per_night': budget_per_night,
            'guests': guests,
            'timestamp': datetime.now().isoformat(),
            'search_type': 'hotel_search'
        }
    }
    
    # Save to memory
    save_memory(f"hotel_search_{destination}", result, user_id)
    
    return result

def save_user_preferences_ultimate(user_id: str, context) -> Dict[str, Any]:
    """
    Save user preferences with intelligent categorization
    
    Args:
        user_id: User identifier
        context: Tool context with preference data
        
    Returns:
        Dictionary with saved preferences
    """
    logger.info(f"[save_user_preferences_ultimate] saving preferences for user={user_id}")
    
    # Extract preferences from context or use defaults
    preferences = {
        'user_id': user_id,
        'travel_style': getattr(context, 'travel_style', 'mid-range'),
        'budget_range': getattr(context, 'budget_range', 'moderate'),
        'interests': getattr(context, 'interests', ['culture', 'food']),
        'preferred_airlines': getattr(context, 'preferred_airlines', []),
        'hotel_preferences': getattr(context, 'hotel_preferences', {}),
        'dietary_restrictions': getattr(context, 'dietary_restrictions', []),
        'accessibility_needs': getattr(context, 'accessibility_needs', []),
        'last_updated': datetime.now().isoformat()
    }
    
    # Save to memory
    save_memory('travel_preferences', preferences, user_id)
    
    return {
        'status': 'success',
        'user_id': user_id,
        'preferences_saved': len(preferences),
        'categories': list(preferences.keys())
    }

def aggregate_travel_results_ultimate(flights: Dict, hotels: Dict, preferences: Dict, context) -> Dict[str, Any]:
    """
    Context-aware result compilation and optimization
    
    Args:
        flights: Flight search results
        hotels: Hotel search results
        preferences: User preferences
        context: Tool context
        
    Returns:
        Aggregated travel plan with recommendations
    """
    user_id = getattr(context, 'user_id', 'anonymous')
    logger.info(f"[aggregate_travel_results_ultimate] Aggregating results from sub-agents")
    
    # Load user preferences from memory
    saved_prefs = load_memory('travel_preferences', user_id)
    
    # Calculate total budget
    flight_costs = [f.get('price', 0) for f in flights.get('flights', [])]
    hotel_costs = [h.get('price_per_night', 0) for h in hotels.get('hotels', [])]
    
    min_flight = min(flight_costs) if flight_costs else 0
    min_hotel = min(hotel_costs) if hotel_costs else 0
    
    # Create aggregated plan
    aggregated_plan = {
        'destination': flights.get('destination', 'Unknown'),
        'user_id': user_id,
        'session_id': getattr(context, 'session_id', 'default'),
        'timestamp': datetime.now().isoformat(),
        'flights': {
            'total_options': len(flights.get('flights', [])),
            'price_range': f"${min(flight_costs)}-${max(flight_costs)}" if flight_costs else "N/A",
            'recommended': flights.get('flights', [])[0] if flights.get('flights') else None
        },
        'hotels': {
            'total_options': len(hotels.get('hotels', [])),
            'price_range': f"${min(hotel_costs)}-${max(hotel_costs)}" if hotel_costs else "N/A",
            'recommended': hotels.get('hotels', [])[0] if hotels.get('hotels') else None
        },
        'budget_analysis': {
            'estimated_flight_cost': min_flight,
            'estimated_hotel_cost_per_night': min_hotel,
            'total_estimated_cost': min_flight + (min_hotel * 5)  # Assuming 5 nights
        },
        'user_preferences': saved_prefs,
        'recommendations': [
            "Book flights early for better prices",
            "Consider hotels with free breakfast",
            "Check visa requirements for destination"
        ]
    }
    
    # Save aggregated results
    save_memory('aggregated_results', aggregated_plan, user_id)
    
    logger.info(f"[aggregate_travel_results_ultimate] Aggregation complete and saved to memory key=aggregated_results_{user_id}")
    
    return aggregated_plan