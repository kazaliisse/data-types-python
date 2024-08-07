#string data types
#literal Assignments
first = "noor"
last = "isse"

print(type(first))


#concatination
fullname = first + " " + last
print(fullname)

fullname += "!"
print(fullname)

# casting a number to a string

age = str(24)
print(type(age))
print(age)

statement = "noor's age is" + age + " " "years old"
print(statement)

#multiline
multiline = '''

hey, how are you?

i was just checking in.
                             i'm good
'''
print(multiline)

#string methods
print(first)
print(first.lower())
print(first.upper())
print(first)

print(multiline.title)
print(multiline.replace("good", "ok"))