from adapters.sqlite_reader import read_table

def get_customer(db_path):
    return read_table("Customer", db_path)

def get_invoices(db_path):
    return read_table("Invoice", db_path)

def get_customer_new(db_path):
    return read_table("Customer_New", db_path)