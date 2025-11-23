# PySpark ETL Pipeline (Local VSCode Project)

This project is a modular ETL pipeline built with PySpark and SQLite, designed for local development using VSCode. It includes CI/CD automation, clean architecture, and unit testing.

## Tech Stack
- Python
- PySpark
- SQLite
- Git + GitHub Actions
- pytest + chispa
- flake8 + black

## Project Structure
my_data_pipeline_project/ 
my_data_pipeline_project/
├── 📁 scripts/                  # Core ETL logic (modular Python scripts)
│   ├── extract.py              # Load data from CSV, API, or other sources
│   ├── transform.py            # Clean and transform data using PySpark
│   ├── load.py                 # Save transformed data into SQLite
│   └── main.py                 # Orchestrates the ETL pipeline (calls extract → transform → load)
│
├── 📁 data/                     # Input and output data files
│   └── sample_data.csv         # Example input dataset
│
├── 📁 tests/                    # Unit tests for pipeline components
│   └── test_transform.py       # Tests for PySpark transformations using `chispa`
│
├── 📁 .github/                  # GitHub Actions CI/CD configuration
│   └── workflows/
│       └── ci.yml              # Workflow for testing, linting, and formatting
│
├── requirements.txt            # Python dependencies
├── README.md                   # Project overview and instructions



