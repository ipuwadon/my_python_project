from adapters.selenium_scraper import SeleniumScraper
from usecases.capture_use_case import CaptureUseCase

if __name__ == "__main__":
    url = "https://www.viagogo.com/th/"
    message = "Jackson Wang"

    scraper = SeleniumScraper()
    use_case = CaptureUseCase(scraper)
    html = use_case.execute(url, message)
    #print(html)