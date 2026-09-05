#Take a student's marks in 5 subjects and calculate: total + average + percentage


student_name=input("Enter the name of the Student: ")
sub1=float(input("Maths subject Marks: "))
sub2=float(input("Biology subject Marks: "))
sub3=float(input("physics subject Marks: "))
sub4=float(input("Chemistry subject Marks: "))
sub5=float(input("Social subject Marks: "))

total=sub1+sub2+sub3+sub4+sub5
average=total/5


print(f"Student name: {student_name}\nTotal: {total}\nAverage: {average}\nPercentage: {average}% ")