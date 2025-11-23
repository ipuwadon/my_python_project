import pandas as pd
from collections import defaultdict
import xlsxwriter

employees = [
    {"name": "Somchai", "department": "IT", "salary": 55000, "type": "full-time"},
    {"name": "Suda", "department": "HR", "salary": 48000, "type": "full-time"},
    {"name": "Anan", "department": "IT", "salary": 60000, "type": "contract"},
    {"name": "Nok", "department": "Finance", "salary": 52000, "type": "full-time"},
    {"name": "Krit", "department": "HR", "salary": 50000, "type": "contract"},
    {"name": "May", "department": "Finance", "salary": 58000, "type": "full-time"},
]

full_time = [emp for emp in employees if emp["type"] == "full-time"]

grouped = defaultdict(list)
for emp in full_time:
    grouped[emp["department"]].append(emp["salary"])

avg_salary = {
    dept: sum(salaries) / len(salaries)
    for dept, salaries in grouped.items()
}

sorted_avg = sorted(avg_salary.items(), key=lambda x: x[1], reverse=True)

print("📊 Average Salary by Department (Full-Time Only):")
for dept, avg in sorted_avg:
    print(f"- {dept}: {avg:,.2f} THB")

# Pandas #########################################
df = pd.DataFrame(employees)

df_full_time = df[df["type"] == "full-time"]

result = df_full_time.groupby("department")["salary"].mean().sort_values(ascending=False)

print("📊 Average Salary by Department (Full-Time Only):")
for dept, avg in result.items():
    print(f"- {dept}: {avg:,.2f} THB")

summary_df = result.reset_index()
summary_df.columns = ["Department", "Average Salary (THB)"]

summary_df.to_csv("avverage_salary_by_department.csv", index=False)

with pd.ExcelWriter("average_salary_by_department.xlsx", engine="xlsxwriter") as writer:
    summary_df.to_excel(writer, index=False, sheet_name="Summary")

    workbook = writer.book
    worksheet = writer.sheets["Summary"]
    format_currency = workbook.add_format({'num_format': '#,##0.00', 'bold': True})
    worksheet.set_column("B:B", 20, format_currency)




