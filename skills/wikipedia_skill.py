# skills/wikipedia_skill.py
# Jarvis reads Wikipedia summaries out loud

import wikipedia

def get_summary(topic):
    """Get a short Wikipedia summary for any topic"""
    try:
        # Search Wikipedia
        results = wikipedia.search(topic)
        
        if not results:
            return f"I couldn't find anything about {topic} on Wikipedia."
        
        # Get the first result
        page = wikipedia.summary(results[0], sentences=3)
        return page
    
    except wikipedia.exceptions.DisambiguationError as e:
        # Multiple results found - pick first one
        page = wikipedia.summary(e.options[0], sentences=3)
        return page
    
    except Exception as e:
        return f"Sorry, I couldn't find information about {topic}."