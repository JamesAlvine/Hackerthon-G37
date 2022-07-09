def painting():
    #user inputs of the wall's measurement in square feet and the price of paint per gallon respectively:
    square_feet = int(input("Enter the square feet of the wall to be pinted: "))
    gallon_price = float(input("Enter the price of the gallon of paint: "))

    estimation(square_feet, gallon_price)

def estimation(square_feet, gallon_price):
    number_of_gallons = square_feet/115
    labor_hours = number_of_gallons * 8 
    total_gallon_price = number_of_gallons * gallon_price
    total_labor = labor_hours * 20
    total_price = total_gallon_price + total_labor
    print("The estimated price of the painting is: ", total_price)

#calling the painting function:
painting()