from abc import ABC, abstractmethod

class ScraperInterface(ABC):
    @abstractmethod
    def capture(self, url: str) -> str:
        pass

    @abstractmethod
    def extract_title(self, html: str) -> str:
        pass