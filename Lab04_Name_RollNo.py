import pandas as pd


# ==========================================================
# TASK 1 - Student Performance Investigation
# ==========================================================
print("\n========== TASK 1: Student Performance Investigation ==========")

students = {
    "Student_ID": [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12],
    "Name": ["Ali", "Sara", "Ahmed", "Hina", "Usman", "Ayesha",
             "Hamza", "Zara", "Bilal", "Fatima", "Omar", "Maryam"],
    "Age": [20, 21, 19, 22, 20, 21, 23, 19, 22, 20, 21, 19],
    "Gender": ["M", "F", "M", "F", "M", "F", "M", "F", "M", "F", "M", "F"],
    "Department": ["CS", "SE", "CS", "IT", "SE", "CS", "IT", "SE", "CS", "IT", "SE", "CS"],
    "Marks": [78, 91, 67, 85, 73, 95, 59, 88, 81, 64, 70, 83],
    "Attendance": [82, 95, 70, 89, 76, 98, 65, 92, 87, 72, 80, 91]
}

df = pd.DataFrame(students)
print(df)

# 1. Student with the highest marks
# idxmax() gives the row index where the max value is
top_student = df.loc[df["Marks"].idxmax()]
print("\nHighest marks:", top_student["Name"], "_", top_student["Marks"])

# 2. Student with the lowest attendance
low_att_student = df.loc[df["Attendance"].idxmin()]
print("Lowest attendance:", low_att_student["Name"], "_", low_att_student["Attendance"], "%")

# 3. Average marks
avg_marks = df["Marks"].mean()
print("Average marks:", round(avg_marks, 2))

# 4. Number of students with marks above average
above_avg = df[df["Marks"] > avg_marks]
print("Students above average:", len(above_avg))

# 5. Number of students with attendance below 75%
below_75 = df[df["Attendance"] < 75]
print("Students with attendance below 75%:", len(below_75))


# ==========================================================
# TASK 2 - Multi-Condition Filtering
# ==========================================================
print("\n========== TASK 2: Multi-Condition Filtering ==========")

# AND condition: all three must be true
and_result = df[(df["Marks"] >= 80) & (df["Attendance"] >= 85) & (df["Age"] < 22)]
print("Marks >= 80 AND Attendance >= 85 AND Age < 22:")
print(and_result[["Name", "Department", "Marks", "Attendance"]])

# OR condition: any one can be true
or_result = df[(df["Marks"] >= 80) | (df["Attendance"] >= 90)]
print("\nMarks >= 80 OR Attendance >= 90:")
print(or_result[["Name", "Department", "Marks", "Attendance"]])

print("\nAND result has", len(and_result), "students, OR result has", len(or_result), "students.")
print("AND is strict (all conditions), so it gives fewer rows. OR is relaxed, so it gives more.")


# ==========================================================
# TASK 3 - Detect Problems in a Dataset
# ==========================================================
print("\n========== TASK 3: Detect Problems in a Dataset ==========")

# This data has problems on purpose:
# - Rows of Ali and Hina are repeated (2 duplicates)
# - Usman's Age and Zara's Marks are missing (None)
# - Hamza's Age is 150 (impossible)
# - Bilal's Marks are -10 (negative)
messy = {
    "Name": ["Ali", "Sara", "Ahmed", "Hina", "Usman", "Ayesha", "Hamza", "Zara",
             "Bilal", "Fatima", "Omar", "Maryam", "Danish", "Ali", "Hina"],
    "Age": [20, 21, 19, 22, None, 21, 150, 19, 22, 20, 21, 19, 23, 20, 22],
    "Marks": [78, 91, 67, 85, 73, 95, 59, None, -10, 64, 70, 83, 76, 78, 85]
}

messy_df = pd.DataFrame(messy)
print(messy_df)

# 1. Duplicate records
print("\nNumber of duplicate rows:", messy_df.duplicated().sum())
print(messy_df[messy_df.duplicated()])

# 2. Missing values
print("\nMissing values in each column:")
print(messy_df.isnull().sum())
print(messy_df[messy_df.isnull().any(axis=1)])

# 3. Invalid ages (a university student should be roughly 15 to 60)
invalid_age = messy_df[(messy_df["Age"] < 15) | (messy_df["Age"] > 60)]
print("\nInvalid ages:")
print(invalid_age)

# 4. Invalid marks (marks must be between 0 and 100)
invalid_marks = messy_df[(messy_df["Marks"] < 0) | (messy_df["Marks"] > 100)]
print("\nInvalid marks:")
print(invalid_marks)


# ==========================================================
# TASK 4 - Dataset Detective
# ==========================================================
print("\n========== TASK 4: Dataset Detective ==========")

data = pd.read_csv("dataset.csv")

print("Number of rows:", data.shape[0])
print("Number of columns:", data.shape[1])
print("Column names:", list(data.columns))
print("\nData types:")
print(data.dtypes)
print("\nMissing values per column:")
print(data.isnull().sum())
print("\nNumber of duplicate rows:", data.duplicated().sum())
print("\nUnique values in each column:")
print(data.nunique())

# Find the column with the most missing values automatically
worst_column = data.isnull().sum().idxmax()
print("\nColumn that needs the most cleaning:", worst_column,
      "(it has", data[worst_column].isnull().sum(), "missing values)")


# ==========================================================
# TASK 5 - Hidden Data Problem
# ==========================================================
print("\n========== TASK 5: Hidden Data Problem ==========")

data5 = {
    "Name": ["Ali", "Sara", "Ahmed", "Hina", "Usman"],
    "Marks": ["78", "91", "67", "85", "73"]
}
df5 = pd.DataFrame(data5)

# 1 & 2. Check the problem: Marks are stored as text (object), not numbers
print("Datatype of Marks before:", df5["Marks"].dtype)

# If we try to take the mean of text, Python complains
try:
    print(df5["Marks"].mean())
except TypeError:
    print("Error: cannot calculate average because Marks are strings.")

# 3. Convert Marks to numbers
df5["Marks"] = pd.to_numeric(df5["Marks"])
print("Datatype of Marks after:", df5["Marks"].dtype)

# 4. Now the average works
avg5 = df5["Marks"].mean()
print("Average marks:", avg5)

# 5. Students above average
print("Students above average:")
print(df5[df5["Marks"] > avg5])


# ==========================================================
# TASK 6 - Department Analysis
# ==========================================================
print("\n========== TASK 6: Department Analysis ==========")

# Using the same student DataFrame from Task 1.
# groupby() finds the departments itself, so new departments work automatically.

# 1. Number of students in each department
print("Students in each department:")
print(df["Department"].value_counts())

# 2. Average marks for each department
dept_marks = df.groupby("Department")["Marks"].mean()
print("\nAverage marks per department:")
print(dept_marks.round(2))

# 3. Department with highest average marks
print("\nHighest average marks:", dept_marks.idxmax())

# 4. Department with lowest average attendance
dept_att = df.groupby("Department")["Attendance"].mean()
print("Lowest average attendance:", dept_att.idxmin())


# ==========================================================
# TASK 7 - Build Your Own Dataset Loader
# ==========================================================
print("\n========== TASK 7: Build Your Own Dataset Loader ==========")

path = input("Enter CSV file name/path (press Enter for dataset.csv): ").strip()
if path == "":
    path = "dataset.csv"

try:
    loaded = pd.read_csv(path)
    print("\nDataset successfully loaded.")
    print("\nRows:", loaded.shape[0])
    print("Columns:", loaded.shape[1])
    print("\nColumn Names:", list(loaded.columns))
    print("\nMissing Values:")
    print(loaded.isnull().sum())
    print("\nDuplicate Rows:", loaded.duplicated().sum())
    print("\nData Types:")
    print(loaded.dtypes)
except FileNotFoundError:
    print("File not found. Please check the name or path.")


# ==========================================================
# TASK 8 - Data Analyst Challenge
# ==========================================================
print("\n========== TASK 8: Data Analyst Challenge ==========")

# Marks distribution: Quiz /10, Assignment /10, Midterm /30, Final /50  -> Total /100
result_data = {
    "Student_ID": [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12],
    "Name": ["Ali", "Sara", "Ahmed", "Hina", "Usman", "Ayesha",
             "Hamza", "Zara", "Bilal", "Fatima", "Omar", "Maryam"],
    "Age": [20, 21, 19, 22, 20, 21, 23, 19, 22, 20, 21, 19],
    "Department": ["CS", "SE", "CS", "IT", "SE", "CS", "IT", "SE", "CS", "IT", "SE", "CS"],
    "Quiz": [8, 9, 6, 7, 5, 10, 4, 9, 9, 3, 6, 8],
    "Assignment": [9, 10, 7, 8, 6, 9, 5, 8, 9, 4, 7, 9],
    "Midterm": [24, 27, 18, 22, 15, 28, 12, 25, 26, 14, 19, 23],
    "Final": [40, 45, 30, 38, 25, 47, 20, 42, 44, 22, 33, 41],
    "Attendance": [82, 95, 70, 89, 92, 98, 65, 72, 68, 94, 80, 91]
}
df8 = pd.DataFrame(result_data)

# New column: Total
df8["Total"] = df8["Quiz"] + df8["Assignment"] + df8["Midterm"] + df8["Final"]
print(df8[["Name", "Department", "Total", "Attendance"]])

# 1. Top 5 students by Total
print("\nTop 5 students:")
print(df8.sort_values("Total", ascending=False).head(5)[["Name", "Total"]])

# 2. Attendance below 75%
print("\nAttendance below 75%:")
print(df8[df8["Attendance"] < 75][["Name", "Attendance"]])

# 3. Total > 80 but attendance < 75  (good marks, poor attendance)
high_marks_low_att = df8[(df8["Total"] > 80) & (df8["Attendance"] < 75)]
print("\nTotal > 80 but attendance < 75:")
print(high_marks_low_att[["Name", "Total", "Attendance"]])

# 4. Attendance > 90 but Total < 60  (regular in class, but low marks)
high_att_low_marks = df8[(df8["Attendance"] > 90) & (df8["Total"] < 60)]
print("\nAttendance > 90 but Total < 60:")
print(high_att_low_marks[["Name", "Total", "Attendance"]])

# 5. Average Total for each department
print("\nAverage Total per department:")
print(df8.groupby("Department")["Total"].mean().round(2))


# ==========================================================
# BONUS - Classify Students (50+ students)
# ==========================================================
print("\n========== BONUS: Student Classification ==========")

bonus = pd.read_csv("dataset.csv")

# Clean first: remove duplicate rows and rows without marks
bonus = bonus.drop_duplicates()
bonus = bonus.dropna(subset=["Marks"])
print("Students used for classification:", len(bonus))

# My criteria:
# Excellent -> 85 and above
# Good      -> 70 to 84
# Average   -> 50 to 69
# At Risk   -> below 50
def classify(marks):
    if marks >= 85:
        return "Excellent"
    elif marks >= 70:
        return "Good"
    elif marks >= 50:
        return "Average"
    else:
        return "At Risk"

bonus["Category"] = bonus["Marks"].apply(classify)

print(bonus[["Name", "Marks", "Category"]].head(10))
print("\nStudents in each category:")
print(bonus["Category"].value_counts())
