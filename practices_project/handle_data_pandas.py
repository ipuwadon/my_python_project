import pandas as pd

data = {
    "name": ["A","B","C","D"],
    "score": [85,90,78,92],
    "subject": ["Math","Math","Science","Science"]
}

df = pd.DataFrame(data)
print(df)

print(df[df["score"] > 80])

print(df.groupby("subject")["score"].mean())

students = {
    "name": ["Piti", "Manee", "Chuji", "Manid"],
    "age": [20, 18, 18, 17],
    "grade": [4, 3, 3, 4]
}

sd = pd.DataFrame(students)
print(sd)

print(sd[sd["age"] >= 18])


print(sd.groupby("grade")["age"].mean())