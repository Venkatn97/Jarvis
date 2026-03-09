# main.py
from core.voice_input import listen
from core.voice_output import speak
from core.brain import think, extract_intent
from browser.controller import BrowserController
from skills.wikipedia_skill import get_summary

browser = BrowserController()
browser.start()

URLS = {
    "youtube": "https://www.youtube.com",
    "google": "https://www.google.com",
    "linkedin": "https://www.linkedin.com",
    "github": "https://www.github.com",
    "twitter": "https://www.twitter.com",
    "reddit": "https://www.reddit.com",
    "netflix": "https://www.netflix.com",
    "amazon": "https://www.amazon.com",
    "maps": "https://www.google.com/maps",
    "news": "https://news.google.com",
    "wikipedia": "https://www.wikipedia.org",
}

def run():
    speak("Hello, I am Jarvis. Browser is ready.")
    
    try:
        while True:
            user_input = listen()
            
            if user_input is None:
                continue
            
            if "exit" in user_input or "stop" in user_input:
                speak("Goodbye sir.")
                browser.stop()
                break
            
            # Let AI understand the intent
            intent = extract_intent(user_input)
            action = intent.get("action", "chat")
            query = intent.get("query", "").strip()
            
            print(f"ACTION: {action} | QUERY: {query}")
            
            if action == "search_google":
                if not query:
                    speak("What should I search for?")
                    continue
                speak(f"Searching Google for {query}")
                browser.search_google(query)
            
            elif action == "search_youtube":
                if not query:
                    speak("What should I search on YouTube?")
                    continue
                speak(f"Searching YouTube for {query}")
                browser.search_youtube(query)
            
            elif action == "play_youtube":
                if not query:
                    speak("What should I play?")
                    continue
                speak(f"Playing {query} on YouTube")
                browser.play_youtube(query)
            
            elif action == "open_website":
                url = URLS.get(query.lower())
                if url:
                    speak(f"Opening {query}")
                    browser.go_to(url)
                elif " " in query:
                    # Has spaces - it's a search not a website
                    speak(f"Searching Google for {query}")
                    browser.search_google(query)
                else:
                    speak(f"Opening {query}")
                    browser.go_to(f"https://www.{query}.com")
            

            
            elif action == "weather":
                if not query:
                    speak("Which city?")
                    continue
                speak(f"Checking weather for {query}")
                browser.get_weather(query)
            
            elif action == "maps":
                if not query:
                    speak("Where should I search on maps?")
                    continue
                speak(f"Opening maps for {query}")
                browser.open_maps(query)
            
            elif action == "news":
                speak(f"Opening news for {query}" if query else "Opening latest news")
                browser.get_news(query)
            
            elif action == "wikipedia":
                if not query:
                    speak("What would you like to know about?")
                    continue
                speak(f"Looking up {query} on Wikipedia")
                result = get_summary(query)
                speak(result)
            
            elif action == "chat":
                response = think(user_input)
                speak(response)
    
    except KeyboardInterrupt:
        speak("Shutting down.")
        browser.stop()

if __name__ == "__main__":
    run()