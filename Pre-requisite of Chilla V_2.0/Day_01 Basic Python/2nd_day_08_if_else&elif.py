student_age=input("How old is student? ")
student_age=int(student_age)
required_age_at_school=5
if student_age==required_age_at_school:
    print("Congrats sudent can join tha school.")
elif student_age > required_age_at_school:
    print("student should join Higher secondary school.")
elif student_age <= 2:
    print("you shoul take care of student he/she is a still baby")
else:
    print("student can't join the school.")

