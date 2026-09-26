#this python file is to test all functionaly


from modules.student.student import StudentClass
#step 1 : student registration test case



email=input("enter email:")
password=input("enter password:")



s1=StudentClass()
s1.setusernameandpassword(email,password)
