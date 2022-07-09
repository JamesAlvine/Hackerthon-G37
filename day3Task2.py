def main():
    fat_grams = input("enter the number of fat grams consumed::")
    fat_calories(fat_grams)
    carb_grams = input("enter the number of carbohydrates grams consumed::")
    carb_calories(carb_grams)


def fat_calories(fat_grams):
    calories_from_fat = fat_grams * 9
    print("The calories from fat are", calories_from_fat)


def carb_calories(carb_grams):
    calories_from_carbs = carb_grams * 4
    print("The calories from carbohydrates are", calories_from_carbs)
main()
