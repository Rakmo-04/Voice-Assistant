from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

class infow():
    def __init__(self):
        self.driver = webdriver.Chrome()
    
    def get_info(self, query):
        self.driver.get("https://www.wikipedia.org")
        search = self.driver.find_element(By.XPATH, '//*[@id="searchInput"]') 
        search.send_keys(query)
        search.send_keys(Keys.RETURN)
        input("Press any key to close the browser...")  # Wait for user input
        self.driver.quit()  # Close the browser

