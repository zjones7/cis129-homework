import csv

# Open the file in write mode (use "a" instead of "w" to append without overwriting)
with open("grades.csv", mode="w", newline="") as file:
    writer = csv.writer(file)
    
    print("Enter student records. Type 'done' as the first name to finish.")
    
    while True:
        first = input("First name: ")
        if first.lower() == 'done':
            break
        
        last = input("Last name: ")
        
        try:
            exam1 = int(input("Exam 1 grade: "))
            exam2 = int(input("Exam 2 grade: "))
            exam3 = int(input("Exam 3 grade: "))
        except ValueError:
            print("Invalid input. Please enter integer grades.")
            continue
        
        # Write the student record
        writer.writerow([first, last, exam1, exam2, exam3])
        print("Record saved.\n")