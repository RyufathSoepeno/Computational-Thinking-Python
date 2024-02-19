# Question 1

# Question 2

z = char(input("Press S to convert to capital letter; Press D to convert to lower letter"))

if z == s:
  ab = input("Input your letter")
  ab.upper()
else:
  ab = input("Input your letter")
  ab.lower()

print(ab)

#Question 3

def checkGPA(GPA): #function to check if accepted or not
    instring = GPA
    if GPA > 2: #if above 2.0, accepted
        print("Your application is accepted, welcome to the university")
    else: #if else 2.0, rejected
        print("Your application is denied, sorry")

print("number 3")
inGPA = float(input("input your GPA:")) #input GPA score, use float to allow decimal number in GPA
while inGPA < 0 or inGPA > 4: #to ensure that input is between 0 and 4
    inGPA = float(input("wrong format, input your GPA:"))
checkGPA(inGPA)#call function to check if accepted or not

# Question 4
