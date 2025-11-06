from entities.extractor import get_customer
from entities.extractor import get_invoices
from entities.extractor import get_customer_new

def run_extraction(db_path):
    df = get_customer(db_path)
    print(df.head())

    df2 = get_customer_new(db_path)
    print(df2.head())