import pandas as pd

def compare_customer(old_df, new_df):
    # Merge both datasets on CustomerId
    merged = old_df.merge(new_df, on='CustomerId', how='outer', suffixes=('_old', '_new'), indicator=True)
    compare_cols = ['FirstName', 'LastName', 'Fax', 'Email', 'SupportRepId']
    result_rows = []

    for _, row in merged.iterrows():
        result = {
            'CustomerId': row['CustomerId'],
            '_merge': row['_merge']
        }

        for col in compare_cols:
            old_val = row.get(f"{col}_old", "")
            new_val = row.get(f"{col}_new", "")

            # Include both old and new values in separate columns
            result[f"{col}_Customer"] = old_val
            result[f"{col}_Customer_New"] = new_val

            # Optional: add a diff marker column
            if row['_merge'] != 'both' or old_val != new_val:
                result[f"{col}_Changed"] = "<<red>>YES<</red>>"
            else:
                result[f"{col}_Changed"] = ""

        result_rows.append(result)

    return pd.DataFrame(result_rows)