# test_browser.py
# Quick test to make sure Jarvis can control the browser

from browser.controller import BrowserController

# Create browser instance
browser = BrowserController()

# Start the browser
browser.start()

# Go to Google
browser.go_to("https://www.google.com")

print("Browser is working!")

# Wait 3 seconds so you can see it
import time
time.sleep(3)

# Close browser
browser.stop()
print("Browser closed.")