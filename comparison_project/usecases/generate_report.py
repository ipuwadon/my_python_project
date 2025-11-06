from adapters.sqlite_reader import read_table
from entities.comparator import compare_customer
from adapters.report_writer import write_csv

def run_comparison(db_path):
    old = read_table("Customer", db_path)
    new = read_table("Customer_New", db_path)
    diff = compare_customer(old, new)

    print(type(diff))
    print(diff.head())

    write_csv(diff, "customer_diff.csv")