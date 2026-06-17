import csv

import csv

already_marked = False

with open("attendance.csv", "r") as file:
    reader = csv.reader(file)

    next(reader)  # Skip header
    
    for row in reader:
        if row[0] == name and row[1] == date:
            already_marked = True

        if not already_marked:
            with open("attendance.csv", "a", newline="") as file:
                writer = csv.writer(file)
                writer.writerow([name, date, time])

            print("Attendance Marked")
