std_marks = {'hari':52,'ram':60,'rambhai':32,'shyambhai':29,'ranjit':90}
passed_students = {key : value for (key,value) in std_marks.items() if value>=32}
for key,value in  passed_students.items():
    print(key+ ":", value)



