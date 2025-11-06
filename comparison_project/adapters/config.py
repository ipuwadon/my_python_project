import os

# Path to SQLite database
DB_PATH = os.path.join(os.path.dirname(__file__), "..", "Chinook.db")

# Output folder for reports
OUTPUT_DIR = os.path.join(os.path.dirname(__file__), "..", "reports")

# Default filenames
CUSTOMER_DIFF_REPORT = "customer_diff.csv"
INVOICE_COMPARISON_REPORT = "invoice_diff.csv"

LOG_LEVEL = "INFO"