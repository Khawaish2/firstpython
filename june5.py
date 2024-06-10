
print("hello"[1])

lista = [1,2,3,6]
print(lista)

tup1 = (1,2,4,5,6)
print(tup1)

# strings , lists , tuples ----> sequence -----> there is position attached to them
# set , dictionary ---> collection

# mutable types ----> number , strings , tuples
# immutable types ----> dictionaries , lists, sets

str1 = 'hello welcome to day3'
print(str1)

str2 = " hello guys"
print(str2)
# these are single line strings
str3 = ("hello"
        "you"
        "all"
        "guys "
        "all")
print(str3)
# these are multi line strings instead of black lash brackets .....
str5 = "hello"
print(str5[::-2])
str7 = "pine apple"
print(str7[1:5])
print(str7[::-1])
# string comparison
# > ,< == ------------------->>> to check for equality
str8 = "apple"
str9 = "APPLE"
print(str8 == str9)
print(str8 > str9)
str12 = "mango"
print(str12*3)
print(str12 + str8 + str9)
print( " the number of character in string 12 is : ", len(str12))
str13 = " mango is my favourite fruit ^^"
print('^^^' not in str13)
# operators used here are in and not in
# string methods in python
str14 = "you can "
print(str14.upper())
print(str14)
str16 = " good is the new better"
new_str = str16.replace('better','best')
print(new_str)
str18 = "everything is else where"
print(str18.find('are'))

# to slice or split or cut the string
str20 = " everything is good "
print(str20.split())

print(str20.split('g'))\











