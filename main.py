import pandas as pd
import numpy as np
import os

# ==========================================
# STEP 1: Prepare the Dataset
# ==========================================
def create_sample_dataset(filename="student_data.csv"):
    """Creates a sample CSV dataset with 20 student records."""
    data = {
        "Student_ID": [f"S1{i:02d}" for i in range(1, 21)],
        "Name": ["Alice", "Bob", "Charlie", "David", "Eva", "Frank", "Grace", "Hannah", "Ian", "Jack",
                 "Karen", "Leo", "Mona", "Nina", "Oscar", "Paul", "Quinn", "Rachel", "Sam", "Tina"],
        "Department": ["Computer Science"] * 10 + ["Information Tech"] * 10,
        "Math": [85, 45, 92, 78, 88, 32, 95, 67, 74, 89, 91, 55, 82, 79, 41, 98, 84, 76, 60, 93],
        "Physics": [80, 50, 89, 75, 90, 40, 96, 70, 72, 85, 92, 60, 80, 85, 38, 95, 82, 78, 65, 88],
        "Chemistry": [78, 55, 94, 82, 85, 45, 91, 65, 76, 88, 89, 58, 83, 80, 42, 97, 85, 74, 62, 90],
        "Attendance": [85, 70, 95, 80, 90, 60, 98, 82, 78, 88, 92, 74, 85, 86, 65, 96, 89, 79, 75, 94]
    }
    df = pd.DataFrame(data)
    df.to_csv(filename, index=False)
    print(f"[Info] Dataset '{filename}' created successfully.\n")

# ==========================================
# REUSABLE FUNCTIONS (Fulfilling Requirement C)
# ==========================================
def calculate_grade(average):
    """Assigns grades based on predefined rules."""
    if average >= 90:
        return 'A'
    elif average >= 80:
        return 'B'
    elif average >= 70:
        return 'C'
    elif average >= 60:
        return 'D'
    else:
        return 'F'

def check_pass_fail(row, subjects):
    """
    Conditions for passing: 
    1. Score >= 40 in ALL subjects
    2. Attendance >= 75%
    """
    # Loop over subjects to check failing marks (Fulfilling Requirement D)
    for subj in subjects:
        if row[subj] < 40:
            return 'Fail'
    
    if row['Attendance'] < 75:
        return 'Fail'
        
    return 'Pass'

# ==========================================
# MAIN EXECUTION
# ==========================================
def main():
    file_name = "student_data.csv"
    subjects = ['Math', 'Physics', 'Chemistry']
    
    # 1. Prepare Data
    if not os.path.exists(file_name):
        create_sample_dataset(file_name)

    # 2. Read the Data (Pandas)
    print("--- STEP 2: Data Loading ---")
    df = pd.read_csv(file_name)
    print(f"Total records loaded: {len(df)}")
    print("Columns:", ", ".join(df.columns))
    print("\nPreview of first 3 rows:")
    print(df.head(3).to_string())
    print("-" * 50 + "\n")

    # 3. Process the Data (NumPy, Loops, and Functions)
    print("--- STEP 3: Processing Data ---")
    
    # Using NumPy to calculate Total and Average (Fulfilling Requirement B)
    subject_marks_array = df[subjects].to_numpy()
    df['Total_Marks'] = np.sum(subject_marks_array, axis=1)
    df['Average'] = np.mean(subject_marks_array, axis=1)

    # Using loops to iterate through rows and apply custom functions 
    grades = []
    statuses = []
    
    for index, row in df.iterrows():
        grades.append(calculate_grade(row['Average']))
        statuses.append(check_pass_fail(row, subjects))

    df['Grade'] = grades
    df['Status'] = statuses

    print("Calculations complete (Totals, Averages, Grades, Pass/Fail).")
    print("Processed Dataset Preview:")
    print(df[['Name', 'Total_Marks', 'Average', 'Grade', 'Status']].head())
    print("-" * 50 + "\n")

    # 4 & 5. Perform Analysis and Final Output
    print("--- STEP 4 & 5: Performance Analysis Results ---\n")

    # Overall Class Performance
    class_average = np.mean(df['Average'])
    highest_avg = np.max(df['Average'])
    lowest_avg = np.min(df['Average'])
    
    print(f"1. OVERALL CLASS METRICS:")
    print(f"   - Class Average: {class_average:.2f}%")
    print(f"   - Highest Average: {highest_avg:.2f}%")
    print(f"   - Lowest Average: {lowest_avg:.2f}%\n")

    # Pass/Fail Statistics
    pass_count = (df['Status'] == 'Pass').sum()
    fail_count = (df['Status'] == 'Fail').sum()
    print(f"2. PASS/FAIL STATISTICS:")
    print(f"   - Passed: {pass_count} students")
    print(f"   - Failed: {fail_count} students\n")

    # Top Performers
    print("3. TOP 3 PERFORMING STUDENTS:")
    top_students = df.sort_values(by='Average', ascending=False).head(3)
    for i, row in top_students.iterrows():
        print(f"   - {row['Name']} ({row['Department']}) | Score: {row['Average']:.2f} | Grade: {row['Grade']}")
    print("\n")

    # Subject-Wise Analysis
    print("4. SUBJECT-WISE PERFORMANCE:")
    subject_averages = {}
    
    for subj in subjects:
        subj_avg = np.mean(df[subj])
        subj_max = np.max(df[subj])
        subj_min = np.min(df[subj])
        subject_averages[subj] = subj_avg
        print(f"   - {subj:10}: Avg = {subj_avg:.2f}, High = {subj_max}, Low = {subj_min}")

    # Best Subject
    best_subject = max(subject_averages, key=subject_averages.get)
    print(f"\n5. HIGHEST SCORING SUBJECT:")
    print(f"   - {best_subject} with an average of {subject_averages[best_subject]:.2f}")

    print("\n" + "=" * 50)
    print("End of Analytics Report")
    print("=" * 50)

if __name__ == "__main__":
    main()