import os
import json
from datetime import datetime

MEMORY_FILE = os.path.join(os.path.dirname(__file__), "remember.json")


def save_memory(message):
    """Save a message to persistent memory with timestamp."""
    memories = load_all_memories()
    memories.append({
        "message": message,
        "timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    })
    with open(MEMORY_FILE, "w") as f:
        json.dump(memories, f, indent=2)


def load_all_memories():
    """Load all saved memories from file."""
    if not os.path.exists(MEMORY_FILE):
        return []
    try:
        with open(MEMORY_FILE, "r") as f:
            return json.load(f)
    except (json.JSONDecodeError, IOError):
        return []


def get_last_memory():
    """Get the most recent memory."""
    memories = load_all_memories()
    if memories:
        return memories[-1]["message"]
    return None


def get_all_memories_text():
    """Get all memories as formatted text."""
    memories = load_all_memories()
    if not memories:
        return "I don't have any saved memories."
    lines = []
    for i, mem in enumerate(memories, 1):
        lines.append(f"{i}. {mem['message']} (saved on {mem['timestamp']})")
    return "\n".join(lines)
