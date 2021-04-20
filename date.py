from datetime import date

today = date.today()
# Month abbreviation, day and year
d4 = today.strftime("%y-%m-%d")
print("d4 =", d4)