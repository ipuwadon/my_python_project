from adapters.selenium_scraper import SeleniumScraper
from usecases.extract_title_case import ExtractTitleUseCase

if __name__ == "__main__":
    url = "https://www.viagogo.com/th/"

    scraper = SeleniumScraper()
    usecase = ExtractTitleUseCase(scraper)

    html = scraper.capture(url, "Jackson")
    title = usecase.execute(html)

    print(f"Page title: {title}")