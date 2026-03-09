# browser/controller.py
from playwright.sync_api import sync_playwright

class BrowserController:
    
    def __init__(self):
        self.playwright = None
        self.browser = None
        self.page = None
    
    def start(self):
        """Open the browser"""
        self.playwright = sync_playwright().start()
        self.browser = self.playwright.chromium.launch(
            headless=False
        )
        self.page = self.browser.new_page()
        print("Browser started.")
    
    def go_to(self, url):
        """Navigate to a URL"""
        self.page.wait_for_load_state("load")
        self.page.goto(url)
        print(f"Navigated to {url}")
    
    def click(self, selector):
        """Click an element"""
        self.page.click(selector)
    
    def type_text(self, selector, text):
        """Type text into an element"""
        self.page.fill(selector, text)
    
    def get_text(self, selector):
        """Read text from an element"""
        return self.page.inner_text(selector)
    
    def screenshot(self):
        """Take a screenshot"""
        return self.page.screenshot()
    
    def search_google(self, query):
        """Search Google directly via URL"""
        self.page.wait_for_load_state("load")
        search_url = f"https://www.google.com/search?q={query.replace(' ', '+')}"
        self.page.goto(search_url)
        self.page.wait_for_load_state("load")
        print(f"Searched for: {query}")
    
    def search_youtube(self, query):
        """Search YouTube directly via URL"""
        search_url = f"https://www.youtube.com/results?search_query={query.replace(' ', '+')}"
        self.page.goto(search_url)
        self.page.wait_for_load_state("load")
        print(f"Searched YouTube for: {query}")
    
    def play_youtube(self, query):
        """Search and play first YouTube result"""
        self.search_youtube(query)
        self.page.wait_for_timeout(2000)
        first_video = self.page.query_selector('ytd-video-renderer a#thumbnail')
        if first_video:
            first_video.click()
            self.page.wait_for_load_state("load")
            print(f"Playing: {query}")
        else:
            print("Could not find video to click")
    
    def open_maps(self, location):
        """Open Google Maps for a location"""
        maps_url = f"https://www.google.com/maps/search/{location.replace(' ', '+')}"
        self.page.goto(maps_url)
        self.page.wait_for_load_state("load")
        print(f"Opened maps for: {location}")
    
    def get_weather(self, location):
        """Search weather for a location"""
        search_url = f"https://www.google.com/search?q=weather+in+{location.replace(' ', '+')}"
        self.page.goto(search_url)
        self.page.wait_for_load_state("load")
        print(f"Weather for: {location}")
    
    def get_news(self, topic=""):
        """Open Google News"""
        if topic:
            url = f"https://news.google.com/search?q={topic.replace(' ', '+')}"
        else:
            url = "https://news.google.com"
        self.page.goto(url)
        self.page.wait_for_load_state("load")
        print(f"Opened news for: {topic}")
    
    def stop(self):
        """Close the browser"""
        self.browser.close()
        self.playwright.stop()