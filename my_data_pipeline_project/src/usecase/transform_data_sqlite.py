from pyspark.sql import DataFrame
from pyspark.sql.functions import length

def transform_album_data(df_album: DataFrame, df_artist: DataFrame) -> DataFrame:
    """
    Apply basic transformations to the album DataFrame:
    - Join Artist name
    - Filter by ArtistId == 2
    - Add a column for title length
    - Group by ArtistId and count albums
    """
    df_joined = df_album.join(df_artist, on="ArtistId", how="inner")

    df_filtered = df_joined.filter(df_joined.ArtistId == 2)
    df_with_length = df_filtered.withColumn("TitleLength", length(df_filtered.Title))
    df_grouped = df_with_length.groupBy("ArtistId", "Name").count()
    
    return df_grouped