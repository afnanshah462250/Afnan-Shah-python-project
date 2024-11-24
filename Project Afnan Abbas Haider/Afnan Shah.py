import pandas as pd
import matplotlib.pyplot as plt

# Step 1: Function to map grades to grade points
def grade_to_points(grade):
    grade_points = {
        "A": 4.0,
        "B": 3.0,
        "C": 2.0,
        "D": 1.0,
        "F": 0.0
    }
    return grade_points.get(grade.upper(), 0.0)

# Step 2: Get user input for courses
def get_user_data():
    courses = []
    grades = []
    credits = []

    print("Enter course data (type 'done' to finish):")
    while True:
        course = input("Course Name (or 'done' to finish): ").strip()
        if course.lower() == 'done':
            break
        grade = input(f"Grade for {course} (A/B/C/D/F): ").strip().upper()
        credits_value = input(f"Credits for {course}: ").strip()

        # Validate inputs
        try:
            credits_value = int(credits_value)
            if grade not in ['A', 'B', 'C', 'D', 'F']:
                print("Invalid grade. Please enter a valid grade (A/B/C/D/F).")
                continue
        except ValueError:
            print("Invalid credit value. Please enter a number.")
            continue

        # Add data to lists
        courses.append(course)
        grades.append(grade)
        credits.append(credits_value)

    return pd.DataFrame({"Course": courses, "Grade": grades, "Credits": credits})

# Step 3: Calculate GPA
def calculate_gpa(df):
    # Add Grade Points and Quality Points
    df['Grade Points'] = df['Grade'].apply(grade_to_points)
    df['Quality Points'] = df['Grade Points'] * df['Credits']

    # Total quality points and credits
    total_quality_points = df['Quality Points'].sum()
    total_credits = df['Credits'].sum()

    # Calculate GPA
    gpa = total_quality_points / total_credits if total_credits > 0 else 0.0
    return gpa, total_credits, total_quality_points

# Step 4: Plot a graph
def plot_graph(df):
    plt.figure(figsize=(10, 6))
    plt.bar(df['Course'], df['Quality Points'], color='skyblue', edgecolor='black')
    plt.title('Quality Points by Course', fontsize=16)
    plt.xlabel('Courses', fontsize=12)
    plt.ylabel('Quality Points', fontsize=12)
    plt.xticks(rotation=45, fontsize=10)
    plt.yticks(fontsize=10)
    plt.grid(axis='y', linestyle='--', alpha=0.7)
    plt.tight_layout()
    plt.show()

# Main Program

# Get user input
df = get_user_data()

# Calculate GPA
gpa, total_credits, total_quality_points = calculate_gpa(df)

# Display results
print("\nCourse Data:")
print(df)
print("\nTotal Credits:", total_credits)
print("Total Quality Points:", total_quality_points)
print(f"GPA: {gpa:.2f}")

# Plot the graph
plot_graph(df)