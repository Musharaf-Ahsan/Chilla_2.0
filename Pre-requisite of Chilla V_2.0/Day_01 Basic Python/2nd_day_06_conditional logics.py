#Logical Operators are "TRUE/FALSE", "YES/NO" or "0/1"

# equal to                    ==
# not equal to                !=
# less than                   <
# greater than                >
# less than and equal to      <=
# greater than equal to       >=

#is 4 equal to 4?
# print(4==4)
# print(4!=9)
# print(4>3)
# print(3<6)
# print(3<=5)
# print(5>=4)

#Application of Logical Operators
# ali_age=4
# age_at_school=5
# print(ali_age==age_at_school)

#input Function and Logical Operator
age_at_school=5
student_age=input("How old is student? ")   #INPUT FUNCTION
student_age=int(student_age)                #CONVERTING STRING INTO int DATA TYPE
print (type(student_age))
print(student_age>=age_at_school)           #LOGICAL OPERTAOR