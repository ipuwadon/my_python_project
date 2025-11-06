from usecases.generate_report import run_comparison
from usecases.extract_data import run_extraction

if __name__ == "__main__":
    run_comparison("Chinook.db")
    run_extraction("Chinook.db")