class ExtractTitleUseCase:
    def __init__(self, scraper):
        self.scraper = scraper

    def execute(self, html: str) -> str:
        return self.scraper.extract_title(html)
