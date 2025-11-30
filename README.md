# TripCraft AI

**Context-Aware Multi-Agent System for Personalized Travel Planning & Budget Optimization**

## Overview

TripCraft AI is an advanced travel planning assistant that demonstrates sophisticated multi-agent coordination, persistent memory management, and intelligent context processing. Built as a comprehensive capstone project for the 5-day AI Agent Development course using the **AI Agent Development Kit (ADK)**.

### Built with AI Agent Development Kit
- **LlmAgent**: Specialized AI agents for flight, hotel, and activity research
- **ParallelAgent**: Concurrent execution of research agents
- **SequentialAgent**: Coordinated workflow management
- **InMemoryRunner**: Production-ready agent execution
- **ToolContext**: Context-aware tool integration

## Features

- **Multi-Agent Architecture**: Parallel and Sequential agents with LLM coordination
- **Advanced Tools**: Custom travel planning tools with context integration
- **Memory & Sessions**: Persistent user preferences and session management
- **Context Engineering**: Natural language processing and intelligent parsing
- **Production Ready**: Comprehensive error handling and observability

## Architecture

```
TripCraft AI
├── Root Agent (SequentialAgent)
│   ├── Parallel Research Team
│   │   ├── Flight Researcher (LlmAgent)
│   │   ├── Hotel Researcher (LlmAgent)
│   │   └── Activity Researcher (LlmAgent)
│   └── Travel Aggregator (LlmAgent)
```

## Quick Start

```python
from src.main import run_demo
run_demo("Budget travel to Tokyo for 5 days")
```

## Project Structure

- `src/agents/` - Multi-agent system implementation
- `src/tools/` - Custom travel planning tools
- `src/utils/` - Utility functions and helpers
- `src/config/` - Configuration and setup
- `tests/` - Test files
- `docs/` - Documentation

## Course Compliance

Implements 6/10 required features:
- ✅ Multi-agent systems (LLM, Parallel, Sequential)
- ✅ Custom tools with context integration
- ✅ Sessions & Memory management
- ✅ Context engineering
- ✅ Observability & logging
- ✅ Agent evaluation

## License

MIT License - Built for educational purposes as part of AI Agent Development course.