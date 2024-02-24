import classes

Student1 = classes.Student(1,"jose","ISI")
Student2 = classes.Student(2,"MARIA","derecho")
Student3 = classes.Student(3,"marco","isi")

Students = []

Students.append(Student1)
Students.append(Student2)
Students.append(Student3)

#MOSTRAR LISTA 
for stu in Students:
    print(stu)
