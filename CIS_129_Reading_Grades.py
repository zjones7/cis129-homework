# Initialize variables
grades = []


# Open the file in read mode
with open("grades.txt", "r") as file:
    for line in file:
        try:
            grade = float(line.strip())
            grades.append(grade)
        except ValueError:
            print(f"Invalid grade found in file and skipped: {line.strip()}")


# Display results
if grades:
    total = sum(grades)
    count = len(grades)
    average = total / count


    print("Grades:")
    for g in grades:
        print(g)


    print(f"\nTotal: {total}")
    print(f"Count: {count}")
    print(f"Average: {average:.2f}")
else:
    print("No valid grades found in the file.")