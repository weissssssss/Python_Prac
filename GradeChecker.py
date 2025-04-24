# Function to convert number grade to letter grade
def get_letter_grade(score):
    if score >= 90:
        return "A+"
    elif score >= 80:
        return "A"
    elif score >= 70:
        return "B+"
    elif score >= 60:
        return "B"
    elif score >= 50:
        return "C+"
    elif score >= 40:
        return "D"
    else:
        return "F"

# Dictionary to store subject and numeric grades
grades = {}

num_subjects = int(input("How many subjects do you want to enter?:  "))

for i in range(num_subjects):
    subject = input(f"Enter name of subject {i+1}: ")
    while True:
        try:
            grade = float(input(f"Enter your grade for {subject}: "))
            break
        except ValueError:
            print("Invalid input! Please enter a number.")
    grades[subject] = grade

# Calculate average
average = sum(grades.values()) / len(grades)

# Display results with letter grades
print("\n--- Report Card ---")
for subject, grade in grades.items():
    letter = get_letter_grade(grade)
    print(f"{subject}: {grade} → {letter}")

print(f"\nAverage Grade: {average:.2f}")

# Determine pass or fail
if average >= 50:
    print("Result: Pass!")
else:
    print("Result: Fail!")
