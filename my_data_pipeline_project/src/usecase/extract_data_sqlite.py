import sqlite3
import pandas as pd
from pyspark.sql import SparkSession
import yaml

def load_config(path="config/settings.yaml"):
    with open(path, "r") as f:
        return yaml.safe_load(f)
    
def extract_table(table_name):
    config = load_config()
    sqlite_path = config["data"]["sqlite_path"]

    # Connect to SQLite and read table in Pandas
    conn = sqlite3.connect(sqlite_path)
    df = pd.read_sql_query(f"SELECT * FROM {table_name}", conn)
    conn.close()

    print("Pandas shape:", df.shape)

    # Convert to Spark DataFrame
    spark = SparkSession.builder.appName(config["spark"]["app_name"]).getOrCreate()
    spark_df = spark.createDataFrame(df)

    return spark_df