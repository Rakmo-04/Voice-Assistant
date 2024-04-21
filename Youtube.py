from selenium import webdriver
from selenium.webdriver.common.by import By

class music():
    def __init__(self):
        self.driver = webdriver.Chrome()
    
    def play(self, query):
        self.query = query
        self.driver.get(url='https://www.youtube.com/results?search_query=' + query)
        # Wait for the search results to load
        videos = self.driver.find_elements(By.CSS_SELECTOR, '#video-title')
        if videos:
            # Click on the first video link
            videos[0].click()
            input("Press Enter to close the browser...")
        else:
            print("No videos found for the query:", query)
        # Close the browser window
        self.driver.quit()

