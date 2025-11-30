"""
Main entry point for TripCraft AI
"""
import random
from typing import Dict, Any
from config import logger
from utils import parse_travel_request, save_memory, get_memory_stats
from tools import (
    search_flights_ultimate,
    find_hotels_ultimate,
    save_user_preferences_ultimate,
    aggregate_travel_results_ultimate
)
from agents import get_agent_system

class MockToolContext:
    """Mock ToolContext for demonstration - compatible with ADK ToolContext"""
    def __init__(self, user_id: str = "demo_user", session_id: str = None, invocation_context=None):
        self.user_id = user_id
        self.session_id = session_id or f"session_{random.randint(1000, 9999)}"
        self.invocation_context = invocation_context or {}
        
    @classmethod
    def create_mock(cls, user_id: str = "demo_user"):
        """Create a mock context without requiring invocation_context"""
        return cls(user_id=user_id)

def format_travel_results(result: Dict[str, Any]):
    """Format and display travel results"""
    print("\n" + "="*60)
    print("🎯 TRIPCRAFT AI TRAVEL PLAN")
    print("="*60)
    
    if 'destination' in result:
        print(f"📍 Destination: {result['destination']}")
    
    if 'flights' in result:
        flights = result['flights']
        print(f"\n✈️ FLIGHTS ({flights.get('total_options', 0)} options)")
        print(f"   Price Range: {flights.get('price_range', 'N/A')}")
        if flights.get('recommended'):
            flight = flights['recommended']
            print(f"   Recommended: {flight.get('airline', 'N/A')} - ${flight.get('price', 'N/A')}")
    
    if 'hotels' in result:
        hotels = result['hotels']
        print(f"\n🏨 HOTELS ({hotels.get('total_options', 0)} options)")
        print(f"   Price Range: {hotels.get('price_range', 'N/A')}")
        if hotels.get('recommended'):
            hotel = hotels['recommended']
            print(f"   Recommended: {hotel.get('name', 'N/A')} - ${hotel.get('price_per_night', 'N/A')}/night")
    
    if 'budget_analysis' in result:
        budget = result['budget_analysis']
        print(f"\n💰 BUDGET ANALYSIS")
        print(f"   Flight Cost: ${budget.get('estimated_flight_cost', 0)}")
        print(f"   Hotel Cost/Night: ${budget.get('estimated_hotel_cost_per_night', 0)}")
        print(f"   Total Estimated: ${budget.get('total_estimated_cost', 0)}")
    
    if 'recommendations' in result:
        print(f"\n💡 RECOMMENDATIONS")
        for i, rec in enumerate(result['recommendations'], 1):
            print(f"   {i}. {rec}")
    
    print("="*60)

def run_demo(request: str = "Budget travel to Tokyo for 5 days"):
    """
    Run TripCraft AI demonstration
    
    Args:
        request: Natural language travel request
    """
    print("🚀 TripCraft AI - Context-Aware Multi-Agent Travel Planning")
    print("="*60)
    
    # Parse the travel request
    parsed = parse_travel_request(request)
    print(f"📝 Request: {request}")
    print(f"🎯 Parsed: {parsed}")
    
    # Create context
    context = MockToolContext.create_mock()
    print(f"🔧 Session: {context.session_id}")
    
    # Try multi-agent system first
    print("\n🤖 Attempting Multi-Agent System...")
    try:
        agent_system = get_agent_system()
        response = agent_system["runner"].run(request)
        print(f"✅ Multi-Agent Response: {response}")
    except Exception as e:
        print(f"⚠️ Multi-Agent system unavailable: {e}")
    
    # Run individual tools as demonstration
    print("\n🔍 Running Individual Tools...")
    
    try:
        # Execute travel planning tools
        flights = search_flights_ultimate(
            parsed['destination'], 
            '2024-02-01', 
            '2024-02-06', 
            context
        )
        
        hotels = find_hotels_ultimate(
            parsed['destination'],
            '2024-02-01',
            '2024-02-06',
            parsed['budget'] / parsed['duration'],
            2,
            context
        )
        
        preferences = save_user_preferences_ultimate(
            context.user_id,
            context
        )
        
        aggregated = aggregate_travel_results_ultimate(
            flights,
            hotels,
            preferences,
            context
        )
        
        print("✅ All tools executed successfully")
        
        # Display formatted results
        format_travel_results(aggregated)
        
        # Show memory statistics
        stats = get_memory_stats()
        print(f"\n📊 Memory Stats: {stats['total_keys']} keys, {stats['total_size']} bytes")
        
    except Exception as e:
        logger.error(f"Tool execution failed: {e}")
        print(f"❌ Tool execution failed: {e}")
        
        # Fallback display
        print(f"\n📊 Parsed Request Summary:")
        print(f"   Destination: {parsed['destination']}")
        print(f"   Budget: ${parsed['budget']}")
        print(f"   Duration: {parsed['duration']} days")
        print(f"   Style: {parsed['style']}")
        print(f"   Interests: {', '.join(parsed['interests'])}")
    
    print("\n🎉 TripCraft AI Demo Completed!")
    return "Demo completed successfully"

def run_interactive_demo():
    """Run interactive TripCraft AI demo"""
    print("🤖 TripCraft AI Interactive Demo")
    print("💬 Enter travel requests or 'quit' to exit")
    print("-" * 50)
    
    while True:
        try:
            user_input = input("\n👤 Your travel request: ")
            
            if user_input.lower() in ['quit', 'exit', 'bye']:
                print("✈️ Happy travels! Goodbye!")
                break
            
            if not user_input.strip():
                print("🤔 Please enter a travel request")
                continue
            
            run_demo(user_input)
            
        except KeyboardInterrupt:
            print("\n✈️ Demo interrupted. Goodbye!")
            break
        except Exception as e:
            print(f"❌ Error: {e}")

def create_simple_context(user_id: str = "demo_user"):
    """Create a simple context object for Kaggle/Jupyter environments"""
    class SimpleContext:
        def __init__(self, user_id):
            self.user_id = user_id
            self.session_id = f"session_{random.randint(1000, 9999)}"
    return SimpleContext(user_id)

def run_minimal_demo(request: str = "Budget travel to Tokyo for 5 days"):
    """Minimal demo for Kaggle/Jupyter environments"""
    print("🚀 TripCraft AI - Minimal Demo")
    print("=" * 40)
    
    try:
        # Simple imports and context
        from utils.parser import parse_travel_request
        from tools.travel_tools import search_flights_ultimate, find_hotels_ultimate
        
        # Parse request
        parsed = parse_travel_request(request)
        print(f"📝 Request: {request}")
        print(f"🎯 Parsed: {parsed}")
        
        # Create simple context
        context = create_simple_context()
        print(f"🔧 Session: {context.session_id}")
        
        # Run flight search
        flights = search_flights_ultimate(
            parsed['destination'], 
            '2024-02-01', 
            '2024-02-06', 
            context
        )
        
        # Display results
        print(f"\n✈️ Found {len(flights['flights'])} flights to {flights['destination']}")
        for flight in flights['flights']:
            print(f"   {flight['airline']}: ${flight['price']} ({flight['duration']})")
        
        print("\n✅ Demo completed successfully!")
        return flights
        
    except Exception as e:
        print(f"❌ Error in minimal demo: {e}")
        return None

if __name__ == "__main__":
    # Run default demo
    run_demo()
    
    # Uncomment for interactive mode
    # run_interactive_demo()
    
    # Uncomment for minimal demo (Kaggle/Jupyter)
    # run_minimal_demo()