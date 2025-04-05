"""
Write a Python program that:
	1.	Asks the user how many students they want to enter.
	2.	Collects student names and their scores (out of 100).
	3.	Calculates and displays the letter grade for each student using this scale:
	•	90 - 100 → A
	•	80 - 89 → B
	•	70 - 79 → C
	•	60 - 69 → D
	•	Below 60 → F
	4.	Stores the student names and grades in a dictionary.
	5.	Prints all student names with their grades.

Example output:

Enter the number of students: 3

Enter student name: Jeff
Enter Jeff's score: 85
Enter student name: Diego
Enter Diego's score: 92
Enter student name: Swiper
Enter Swiper's score: 58

--- Student Grades ---
Jeff: B
Diego: A
Swiper: F

"""

student_score = {}

num_students = int(input("Enter the amount of students: "))

for i in range (num_students):
        name = (input("Enter the name of the student: "))
        score = float(input(f"Enter the score of {name} 1 - 100: "))
        
        if name not in student_score:
                student_score[name] = []

        student_score[name].append(score)

print(student_score)

