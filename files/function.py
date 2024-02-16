from files.flat import Bill, Flatmates

from reports import PdfReport,FileSharer

amount=float((input("hey user, enter the bill amount?: ")))
period=input("what is the bill period?: E.g. March 2024 ")

name1=input("What is your name?: ")
days_in_house1=int(input(f"how may days did {name1} stay in the house during bill period?: "))

name2=input("What is other flatmate's name?: ")
days_in_house2=int(input(f"how may days did {name2} stay in the house during bill period?: "))

the_bill= Bill(amount, period)
flatmate1= Flatmates(name1, days_in_house1)
flatmate2= Flatmates(name2, days_in_house2)

print(f"{flatmate1.name} pays ", flatmate1.pays(the_bill,flatmate2))
print(f"{flatmate2.name} pays ", flatmate2.pays(the_bill,flatmate1))

pdfreport= PdfReport(filename=f"{the_bill.period}.pdf")
pdfreport.generate(flatmate1,flatmate2,bill=the_bill)

file_share= FileSharer(filepath=f"{the_bill.period}.pdf")
print(file_share.share())