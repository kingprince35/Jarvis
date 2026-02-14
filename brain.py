from groq import Groq
from config import GROQ_API_KEY, GROQ_MODEL, GROQ_TEMPERATURE, GROQ_MAX_TOKENS, USER_NAME

client = Groq(api_key=GROQ_API_KEY)

# System prompt that defines Jarvis's personality
SYSTEM_PROMPT = f"""You are Jarvis, an advanced AI assistant created for {USER_NAME}.
You are inspired by Iron Man's JARVIS - intelligent, helpful, and slightly witty.
Keep your responses concise (1-3 sentences) unless the user asks for more detail.
You call the user '{USER_NAME}' or 'Sir'.
You can help with: answering questions, calculations, explanations, coding help,
general knowledge, advice, and conversation.
If asked about your capabilities, mention that you can also control apps,
search the web, read news, and control media through voice commands.
Always be respectful and professional."""

# Conversation history for context
conversation_history = [
    {"role": "system", "content": SYSTEM_PROMPT}
]

# Keep only last N messages to avoid token limits
MAX_HISTORY = 20


def ask(user_input):
    """Send a message to GROQ AI and return the response."""
    conversation_history.append({"role": "user", "content": user_input})

    # Trim history if too long (keep system prompt + last N messages)
    if len(conversation_history) > MAX_HISTORY + 1:
        conversation_history[1:] = conversation_history[-(MAX_HISTORY):]

    try:
        response = client.chat.completions.create(
            model=GROQ_MODEL,
            messages=conversation_history,
            temperature=GROQ_TEMPERATURE,
            max_tokens=GROQ_MAX_TOKENS
        )
        reply = response.choices[0].message.content
        conversation_history.append({"role": "assistant", "content": reply})
        return reply
    except Exception as e:
        error_msg = f"Sorry {USER_NAME}, I encountered an error: {str(e)}"
        print(f"GROQ API Error: {e}")
        return error_msg


def clear_history():
    """Clear conversation history but keep system prompt."""
    conversation_history.clear()
    conversation_history.append({"role": "system", "content": SYSTEM_PROMPT})
