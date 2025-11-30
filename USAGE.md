# TripCraft AI Usage Guide

## Quick Start

### Prerequisites
- Python 3.7+ (via Anaconda recommended)
- No external dependencies required for basic demo

### Running the Application

1. **Navigate to the project directory:**
   ```bash
   cd tripcraft-ai/src
   ```

2. **Run the demo:**
   ```bash
   python main.py
   ```

3. **Custom travel request:**
   ```bash
   python -c "from main import run_demo; run_demo('Luxury trip to Paris for 7 days')"
   ```

## Usage Examples

### Basic Demo
```python
from main import run_demo

# Default demo
run_demo()

# Custom requests
run_demo("Budget travel to Tokyo for 5 days")
run_demo("Family vacation to Singapore with kids")
run_demo("Business trip to London for 3 days")
```

### Interactive Mode
Uncomment the interactive mode in `main.py`:
```python
if __name__ == "__main__":
    run_interactive_demo()  # Enable this line
```

Then run:
```bash
python main.py
```

## Features Demonstrated

- **Natural Language Processing**: Parses travel requests into structured data
- **Multi-Agent System**: Simulates parallel and sequential agent coordination
- **Memory Management**: Persistent storage of user preferences and search results
- **Travel Planning Tools**: Flight search, hotel booking, preference management
- **Budget Analysis**: Cost estimation and optimization

## Sample Output

```
🚀 TripCraft AI - Context-Aware Multi-Agent Travel Planning
============================================================
📝 Request: Budget travel to Tokyo for 5 days
🎯 Parsed: {'destination': 'Tokyo', 'budget': 2000, 'duration': 5, 'style': 'budget', 'interests': ['culture', 'food']}
🔧 Session: session_1234

🤖 Attempting Multi-Agent System...
✅ Multi-Agent Response: {'status': 'completed', 'message': 'Mock execution completed'}

🔍 Running Individual Tools...
✅ All tools executed successfully

============================================================
🎯 TRIPCRAFT AI TRAVEL PLAN
============================================================
📍 Destination: Tokyo

✈️ FLIGHTS (2 options)
   Price Range: $700-$900
   Recommended: Emirates - $850

🏨 HOTELS (2 options)
   Price Range: $100-$140
   Recommended: Marriott Tokyo - $120/night

💰 BUDGET ANALYSIS
   Flight Cost: $700
   Hotel Cost/Night: $100
   Total Estimated: $1200
============================================================

📊 Memory Stats: 4 keys, 2847 bytes

🎉 TripCraft AI Demo Completed!
```

## Architecture Overview

```
TripCraft AI
├── main.py              # Entry point and demo runner
├── agents/              # Multi-agent system
│   ├── __init__.py
│   └── multi_agent_system.py
├── tools/               # Travel planning tools
│   ├── __init__.py
│   └── travel_tools.py
├── utils/               # Utilities
│   ├── __init__.py
│   ├── memory.py        # Memory management
│   └── parser.py        # NLP parsing
└── config/              # Configuration
    ├── __init__.py
    └── settings.py
```

## Customization

### Adding New Destinations
Edit `travel_tools.py` to add pricing for new destinations:
```python
base_prices = {
    'tokyo': 800, 'paris': 650, 'london': 600,
    'your_city': 500  # Add here
}
```

### Modifying Travel Styles
Update `parser.py` to recognize new travel styles:
```python
if any(word in user_lower for word in ['eco', 'sustainable']):
    style = 'eco-friendly'
```

### Custom Interests
Add new interest categories in `parser.py`:
```python
interest_keywords = {
    'photography': ['photo', 'camera', 'scenic', 'instagram'],
    # Add more categories
}
```

## Troubleshooting

### Import Errors
If you get `ModuleNotFoundError`, ensure you're running from the `src` directory:
```bash
cd tripcraft-ai/src
python main.py
```

### Python Not Found
If using Anaconda:
```bash
conda activate base
cd tripcraft-ai/src
python main.py
```

## Development

### Running Tests
```bash
cd tripcraft-ai
python -m pytest tests/
```

### Code Structure
- All imports are relative to the `src` directory
- Mock implementations replace external dependencies
- Memory is stored in-memory (resets on restart)
- Logging is configured for development visibility

## License
MIT License - Built for educational purposes.