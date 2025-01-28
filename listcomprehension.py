student = [20,57,59,70,57,78,80,84,76]

#passed_students = [i for i in student if i>60 ]
#print(passed_students)

failed_students = list(filter(lambda x: x<60,student))
print(failed_students)

passed_students = ["passed" if i>60 else "failed" for i in student]
print(passed_students)





   

