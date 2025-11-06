class CaptureUseCase:
    def __init__(self, scraper):
        self.scraper = scraper

    def execute(self, url: str, message: str):
        return self.scraper.capture(url, message)