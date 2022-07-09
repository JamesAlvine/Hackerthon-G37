purchased_books = int(input("Enter the number of books purchased this month: "))

if purchased_books == 0:
    earned_points = 0
    print("Awarded points: ", earned_points)

elif purchased_books == 1:
    earned_points = 6
    print("Awarded points: ", earned_points)

elif purchased_books == 2:
    earned_points = 16
    print("Awarded points: ", earned_points)

elif purchased_books == 3:
    earned_points = 32
    print("Awarded points: ", earned_points)

elif purchased_books == 4:
    earned_points = 60
    print("Awarded points: ", earned_points)
    
else:
    print("out of scope")