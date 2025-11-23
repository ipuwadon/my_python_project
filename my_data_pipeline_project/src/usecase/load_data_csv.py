def save_to_csv(df, output_path: str) -> None:
    #df.coalesce(1).write.mode("overwrite").option("header", "true").csv(output_path)
    pdf = df.toPandas()
    pdf.to_csv(f"{output_path}.csv", index=False)