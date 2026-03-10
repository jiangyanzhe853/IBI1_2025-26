year = float(input("your age（years):"))
weight = float(input("your weight (kg):"))
gender = input("your gender:")
cr = float(input("your cr (µmol/l):"))

# 2. create a list to include every possible invalid input
error_messages = []

# 3. check every invalid input and feedback all the mistakes
if year >= 100:
    error_messages.append("Age error: must be less than 100 years")
if weight <= 20 or weight >= 80:
    error_messages.append("Weight error: must be between 20 and 80 kg")
if cr <= 0 or cr >= 100:
    error_messages.append("Cr error: must be between 0 and 100 µmol/l")
if gender not in ["male","female"]:
    error_messages.append("Gender error: must be 'male' or 'female'")

# 4. check the error_messages list to find out whether there is a mistake：if exits feedback mistaked; else feedback Crcl
if not error_messages:  # no mistakes
    if gender == "male": #male
        Crcl = (((140 - year) * weight) / (72 * cr)) * 1
    else:  # female
        Crcl = (((140 - year) * weight) / (72 * cr)) * 0.85
    print(f"your clearance: {Crcl:.2f}")
else:  # list all the mistakes
    print("Invalid input(s):")
    for error in error_messages:
        print(error)