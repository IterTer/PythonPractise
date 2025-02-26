from apartment import Bill, Flatmate
from reports import PdfReport

amount = float(input("Hey, enter the billing amount: "))
period = input("What is the billing period (E.g. December 2024): ")

name1 = input("What is your name? ")
days_in_house1 = int(input(f"How many days did {name1} stay in the apartment during {period}: "))
name2 = input("What is the name of the other flatmate? ")
days_in_house2 = int(input(f"How many days did {name2} stay in the apartment during {period}: "))

the_bill = Bill(amount, period)
flatmate1 = Flatmate(name1, days_in_house1)
flatmate2 = Flatmate(name2, days_in_house2)

print(f"{name1}:", flatmate1.pays(the_bill, flatmate2))
print(f"{name2}:", flatmate2.pays(the_bill, flatmate1))

pdf_report = PdfReport(filename=f"{the_bill.period}.pdf")
pdf_report.generate(flatmate1, flatmate2, the_bill)