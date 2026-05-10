class food_item:
    def __init__(self, name, calories, protein, carbohydrates, fat):
        self.name = name
        self.calories = calories
        self.protein = protein
        self.carbohydrates = carbohydrates
        self.fat = fat

def calculate_total_nutrition(food_list):
    total_cal = 0
    total_pro = 0
    total_carbs = 0
    total_fat = 0

    for food in food_list:
        total_cal += food.calories
        total_pro += food.protein
        total_carbs += food.carbohydrates
        total_fat += food.fat

    print("24-hour Total Nutrition Intake:")
    print(f"Total calories: {total_cal} kcal")
    print(f"Total protein: {total_pro} g")
    print(f"Total carbohydrates: {total_carbs} g")
    print(f"Total fat: {total_fat} g")

    # Warnings
    if total_cal > 2500:
        print("Warning: Calorie intake exceeds 2500 kcal!")
    if total_fat > 90:
        print("Warning: Fat intake exceeds 90 g!")
    return total_cal, total_pro, total_carbs, total_fat

# Example usage (required)
print("Nutrition Tracker Example:")
apple = food_item("Apple", 60, 0.3, 15, 0.5)
banana = food_item("Banana", 96, 1.2, 23, 0.3)
rice = food_item("Rice", 130, 2.7, 28, 0.3)
daily_food = [apple, banana, rice]
calculate_total_nutrition(daily_food)