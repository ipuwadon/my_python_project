def write_csv(df, filename):
    df.to_csv(filename, index=False)