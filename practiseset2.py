#(1) write a program to find area of triangle.
#base=float(input('enter base value='))
#height=float(input('enter value of height='))
#area=0.5* base * height
#print('the area of triangle:',area)

#(2)write a program to find area of square.
#side=float(input('enter the side'))
#area=side*side
#print('area of square is:',area)

#(3)write a program to find celcius to farenhit.
#celsius=int(input('enter  value of celsius: '))
#farenhit=(celsius*9/5)+32
#print('celcius to ferenheit:',farenhit)

#(4)write a program to convert us dollar to indian rupee.
#dollars=float(input('enter dollars:'))
#rupees=dollars*82
#print(Rupees,rupees)

#(5)write a program to convert litre to mili liter.
litre = float(input('enter the value :'))
print(litre)
milliliters= litre*1000
print(milliliters)



#6. Enter binary, octal and hexadecimal values and convert it into decimal.
#binary to decimal
a=0b10011
print(a)
#19
#octal to decimal
b=0o3156
print(b)
#1646
#hexa to decimal
c=0Xd215
print(c)
d=0xD2156
print(d)




#7. Accept one integer value from the user; convert it to binary, octal and hexadecimal.

#a=int(input('enter value:'))
#binary=bin(a)
#octal=oct(a)
#hexadecimal=hex(a)
#print(binary)
#print(octal)
#print(hexadecimal)

#8. Accept string from the user (‘The Rajkot is a good city to live’), and do the following
#operations: i). Display the first character of the string, ii). Display the first character of the string
#using negative index, iii). Display ‘Rajkot is a good city’. iv). Display the last character.

#b=input('enter a string:')
#print (b)
#print (b[0])
#print(b[:-33])
#print(b[0:25])
#print(b[-1])


#9. Create bytes, enter some values and display all elements.

#a=21
#b=bytes(a)
#print(b)

#10. Create bytearray, enter some values and perform the following: i). Replace the 3rd element with
#7, ii). Display the 5th element.

#a=45
#b=bytearray(a)
#print(b)

#11. Create list and insert values. i).Display all the elements. ii). Display the 3
#rd element,
#iii). Replace the 4th element with ‘Atmiya’, iv). Display elements from 3rd to 7th element.

l=[2,5,7,9,9,6]
print(l)
#print(b[2])
print(b[3]='atmiya')


#a=int(input("enter a number:"))
#print(a)
##b=bytes(a)
#print(b)

#11.
#l=[2,7,8,5,'yashavi','abc']
#print(l)
#print(l[2])
#print(l[3])
#1[4]='atmiya'
#print(l)
#print(l[3:8])

#12.
#t=(1,6,9,'yashavi',89,35)
#print(t)
#t[3]=9
#print(t)
#print(t[5])..

#13.Create a set insert some values. i). Add elements to
#it and display, ii). Remove elements from it and display...

'''s={8,9,6,30}
print(s)
s.update([111])
print(s)
s.remove(8)
print(s)'''

#output
'''{8, 9, 6, 30}
{6, 8, 9, 111, 30}
{6, 9, 111, 30}'''

# 14. Create a set insert some values and convert it to
#frozenset. Try to add and remove some
# elements.

'''a={8,6,7,1,2,6}
print(a)
fs=frozenset(a)
print(fs)
b=frozenset('mca sem 2')
print(b)'''

'''output
{1, 2, 6, 7, 8}
frozenset({1, 2, 6, 7, 8})
frozenset({'e', 'a', '2', 'c', ' ', 's', 'm'})'''

'''15. Create an empty dictionary, Insert some Roll:Name into it.
# i). Retrieve 5th value using key,
# ii).Retrieve all the roll numbers,
# iii). Retrieve all the names,
# iv). Change the name of the student having roll no. 7,
# v). Remove roll no 9,
# vi). Display the dictionary.'''

dic={}
print(dic)
dic[1]='i'
dic[2]='am'
dic[3]='kariya'
dic[4]='yashavi'
dic[5]='.'
dic[6]='i'
dic[7]='am'
dic[8]='mca'
dic[9]='student'
print(dic)
print(dic[5])
print(dic.keys)
print(dic.values)
dic[7]='hii'
print(dic)
del dic[9]
print(dic)

#16.Create a list having names of months.
#i). Check whether December is in list or not,
#ii). Query the list using ‘not in’.

months=['jan','feb','mar','apr','may','jun','july','aug','sep','oct','nov','dec']
print(months)
print('dec' in months)
print('dec' not in months)

17. Take two integer values from the user using split(),
perform basic arithmetic operation on the values.'''

a,b=[int(no) for no in input('enter two number:').split()]
print('the sum of two intege:',a+b)
print('minimize of two integers:',a-b)
print('the multiplication of two integers:',a*b)
print('the division of two numbers:',a/b)









