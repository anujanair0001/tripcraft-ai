"""
Memory management utilities for TripCraft AI
"""
import json
from typing import Dict, Any, List, Optional
from datetime import datetime
from config import logger

# In-memory database for session persistence
_MEMORY_DB: Dict[str, str] = {}

def save_memory(key: str, data: Any, user_id: str = "default") -> bool:
    """Save data to memory with user-specific key"""
    try:
        memory_key = f"{key}_{user_id}"
        serialized_data = json.dumps(data) if not isinstance(data, str) else data
        _MEMORY_DB[memory_key] = serialized_data
        logger.info(f"[save_memory] saved key={memory_key} (size={len(serialized_data)} chars)")
        return True
    except Exception as e:
        logger.error(f"[save_memory] error saving {key}: {e}")
        return False

def load_memory(key: str, user_id: str = "default") -> Optional[Any]:
    """Load data from memory with user-specific key"""
    try:
        memory_key = f"{key}_{user_id}"
        if memory_key in _MEMORY_DB:
            data = _MEMORY_DB[memory_key]
            try:
                return json.loads(data)
            except json.JSONDecodeError:
                return data
        return None
    except Exception as e:
        logger.error(f"[load_memory] error loading {key}: {e}")
        return None

def search_memory(query: str, user_id: str = "default", limit: int = 10) -> Dict[str, Any]:
    """Search memory for keys matching query"""
    try:
        matching_keys = [k for k in _MEMORY_DB.keys() if query in k and user_id in k]
        results = []
        
        for key in matching_keys[:limit]:
            results.append({
                "key": key,
                "data": _MEMORY_DB[key][:100] + "..." if len(_MEMORY_DB[key]) > 100 else _MEMORY_DB[key]
            })
        
        logger.info(f"[search_memory] query={query} user_id={user_id} found={len(results)}")
        return {
            "query": query,
            "user_id": user_id,
            "total_found": len(matching_keys),
            "results": results
        }
    except Exception as e:
        logger.error(f"[search_memory] error searching {query}: {e}")
        return {"query": query, "user_id": user_id, "total_found": 0, "results": []}

def get_memory_stats() -> Dict[str, Any]:
    """Get memory database statistics"""
    return {
        "total_keys": len(_MEMORY_DB),
        "total_size": sum(len(v) for v in _MEMORY_DB.values()),
        "keys": list(_MEMORY_DB.keys())
    }