from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from bs4 import BeautifulSoup
from entities.scraper_interface import ScraperInterface
import time

class SeleniumScraper(ScraperInterface):
    def capture(self, url: str, message: str) -> str:
        driver = webdriver.Chrome()
        driver.get(url)

        try:
            allow_button = WebDriverWait(driver, 20).until(
                EC.element_to_be_clickable((By.CLASS_NAME, "iBeqJr"))
            )
            allow_button.click()
        except Exception as e:
            print("Allow All button not found or not clickable:", e)

        try:
            search_box = driver.find_element(By.CLASS_NAME, "hAtzHV")
            search_box.send_keys(message)
            search_box.send_keys(Keys.RETURN)
        except Exception as e:
            print("Search box not found:", e)

        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.CLASS_NAME, "hRJTCJ"))  # adjust as needed
        )

        link = driver.find_element(By.CLASS_NAME, "hRJTCJ")
        link.click()

        time.sleep(10)

        html = driver.page_source
        driver.quit()
        return html

    def extract_title(self, html: str) -> str:
        soup = BeautifulSoup(html, "html.parser")
        return soup.title.string.strip() if soup.title else "No title found"