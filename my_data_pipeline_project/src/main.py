from src.usecase.extract_data_sqlite import extract_table
from src.usecase.extract_data_sqlite import load_config
from src.usecase.transform_data_sqlite import transform_album_data
from src.usecase.load_data_csv import save_to_csv
import findspark
import os
import sys

# Force Spark to use the current Python interpreter
os.environ["PYSPARK_PYTHON"] = sys.executable
os.environ["PYSPARK_DRIVER_PYTHON"] = sys.executable

findspark.init()
print("Spark will use:", os.environ["PYSPARK_PYTHON"])

# Extract
df_album = extract_table("Album")
df_artist = extract_table("Artist")
df_album.show()
df_artist.show()

# Transform
df_transform = transform_album_data(df_album, df_artist)
df_transform.show()

# Load
config = load_config()
output_path = config["data"]["output_path"]

save_to_csv(df_transform, f"{output_path}/album_summary_result")

