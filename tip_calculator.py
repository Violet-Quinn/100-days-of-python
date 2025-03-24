print("Welcome to the Tip Calculator!")
bill=float(input("What was your total bill? $"))
tip_percent=float(input("How much tip would you like to give? 10%, 12% or 15%?"))
tip=bill*(tip_percent/100)
final_bill=tip+bill
share=int(input("How many people to split the bill?"))
splits=round(final_bill/share)
print(f"Each person should pay ${splits}")

