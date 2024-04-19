#2. Get the marks of 5 subjects at the command line and display the total of marks, and percentage.
'''import sys
mark1=int(sys.argv[1])
mark2=int(sys.argv[2])
mark3=int(sys.argv[3])
mark4=int(sys.argv[4])
mark5=int(sys.argv[5])
T_mark=mark1+mark2+mark3+mark4+mark5
print(T_mark)
percentage=(T_mark*5)/100
print(percentage)'''

'''3. Rajkot Corporation wants to make simple application to calculate Water Bill of Rajkotians. Water
is being delivered by the Corporation on per litre charges as below:
Upto 90 litres – Rs. 0/ltr
Upto 150 litres – Rs. 2/ltr
Upto 250 litres – Rs. 5/ltr
More than 250 – Rs. 10/ltr
Accept unit consumption from consumer and display the bill amount.


4. A tuition class owner wants to make a simple application to allocate grade to the students on
the basis of marks student have scored. Accept marks from the students.
Marks more than 90 – A1 grade
Marks 80 or less than or equal 90 – A grade
Marks 70 or less than or equal 80 – B1
Marks 60 or less than or equal 70 – B
Marks 50 or less than or equal 60 – Can do Better!
Marks <50 – Need to work hard.'''

'''mark=int(input('Enter your marks:'))
if(mark<50):
	print('Need to work hard.')
elif(mark>=50 or mark<60):
	print('Can do better!')
elif(mark<=60 or mark<70):
	print('You got B grade.')
elif(mark<=70 or mark<80):
	print('You got B1 grade.')
elif(mark<=80 or mark<90):
	print('You got higest grade A')
elif(mark<=90):
	print('Hurry! You got highest grade A+')'''


'''5.Income Tax department wants to make an application that calculates tax on the basis of the
income. Accept yearly income earned by the taxpayer as an input and calculate tax to be paid.
The tax slab is as below:
Income up to 8 lakhs – No tax
Income more than 8 lakh and less than 10 lakhs – 15% of income
Income more than 10 lakhs and less than 20 lakhs – 20% of income
Income more than 20 lakhs – 30% of income'''

income=int(input('Enter your income:'))
if(income<8):
	print('You do not pay tax.')
elif(income>=8 and income<10):
	print('income*15/100')
elif(income>=10 and income<20):
	print('income*20/100')
elif(income<=20):
	print('income*30/100')			






