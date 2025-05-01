# Open the file in write mode
with open("grades.txt", "w") as file:
    print("Enter grades one by one. Type 'done' when finished.")


    while True:
        grade_input = input("Enter grade (or 'done' to finish): ")
        if grade_input.lower() == 'done':
            break
        try:
            # Convert input to float to validate it's a number
            grade = float(grade_input)
            file.write(f"{grade}\n")
        except ValueError:
            print("Invalid input. Please enter a number or 'done'.")