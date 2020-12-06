names = {'alperen' : 'demirkol',     
         'ömer' : 'cengiz'}

courses = ['MAT103', 'FIZ101', 'KIM101', 'KON101', 'KON111']

def error():
    print("You have already choosen this course!")

def error2():
    print("You did not choose this course, please type one of the courses you have just chosen ")

def error3():
    print("Invalid value, try again")
 
print("Please enter your name")
name = input()
print("You entered your name as {}.".format(name))
print("Please enter your surname")
surname = input()
print("You entered your surname as {}.".format(surname))

if name in names and surname == names[name]:
    print("          \WELCOME/")
else:        
    print("Invalid id! You have 2 chance")
    name2 = input("Please enter your name   ")
    print("You entered your name as {}.".format(name2))
    surname2 = input("Please enter your surname   ")
    print("You entered your surname as {}.".format(surname2))

    if name2 in names and surname == names[name2]:
        print("Welcome")
    else:
        print("Invalid id! It is your last chance")
        name3 = input("Please enter your name   ")
        print("You entered your name as {}.".format(name3))
        surname3 = input("Please enter your surname   ")
        print("You entered your surname as {}.".format(surname3))

        if name3 in names and surname3 == names[name3]:
            print("Welcome")
        else:
            print("Please try again later")

print("Courses: Mathematics(0), Physiscs(1), Chemistry(2), Engineering Ethics(3), Introduction to Control Engineering(4)")
print("You must write values which are given in phranteses for course selection")
print("You have to select at least 3 courses")


select1 = int(input("Please selecet your course_1 --> "))
print("You selected your first course as {}.".format(courses[select1]))

select2 = int(input("Please selecet your course_2 --> "))
while select2 == select1 :
    error()
    if select2 != select1 :
        select2 = int(input())
    else:
        select2 = int(input("Please selecet your course_2 --> "))
print("You selected your second course as {}.".format(courses[select2]))

select3 = int(input("Please selecet your course_3 --> "))
while select3 == select2 or select3 == select1 :
    error()
    if select3 != select2 and select3 != select1 :
        select3 = int(input())
    else:
        select3 = int(input("Please selecet your course_3 --> "))
print("You selected your third course as {}.".format(courses[select3]))


print("If you want to finish course selection please type 'end' , or you can continue selection")

select4 = input("Please selecet your course_4 --> ")

if select4 == "end" :
    print("You finished course selection succesfully")
    selected = [select1, select2, select3]
    lesson = int(input("Please enter a course name for grade (type number like previos ones) -->"))
    while lesson not in selected :
        error2()
        if lesson in selected :
            print("You chosed {}." .format(courses[lesson]))
        else:
            lesson = int(input("Please enter a course name for grade (type number like previos ones) -->"))
else:
    while select4 == select3 or select4 == select2 or select4 == select1 :
        error()
        if select4 != select3 and select4 != select2 and select4 != select1 :
            select4 = int(input())
        else:
            select4 = int(input("Please selecet your course_4 --> "))
    print("You selected your fourth course as {}.".format(courses[int(select4)]))
    print("If you want to finish course selection please type 'end' , or you can continue selection")
    select5 = input("Please selecet your course_5 --> ")
    if select5 == "end":
        print("You finished course selection succesfully")
        selected = [select1, select2, select3, select4]
        print("Selected courses:",selected)
        lesson = int(input("Please enter a course name for grade (type number like previos ones) -->"))
        while lesson not in selected :
            if str(lesson) == select4:
                break
            error2()
            lesson = int(input("Please enter a course name for grade (type number like previos ones) -->"))
            if lesson in selected :
                print("You chosed {}." .format(courses[lesson]))
            
    else:
        while int(select5) == select4 or int(select5) == select3 or int(select5) == select2 or int(select5) == select1 :
            error()
            if select5 != select4 and select5 != select3 and select5 != select2 and select5 != select1 :
                select5 = int(input())
            else:
                select5 = int(input("Please selecet your course_5 --> "))
        print("You selected your fifth course as {}.".format(courses[int(select5)]))
        selected = [select1, select2, select3, select4, select5]
        print("Selected courses:",selected)
        lesson = int(input("Please enter a course name for grade (type number like previos ones) -->"))

print("You chosed {}." .format(courses[lesson]))

mid = int(input("Please type your midterm grade "))
while mid > 100 or mid < 0 :
    error3()
    if mid <= 100 or mid >= 0 :
        mid = int(input())
    else:
        mid = int(input("Please type your midterm grade "))
print("Your midterm grade is {}." .format(mid))

fin = int(input("Please type your final grade "))
while fin > 100 or fin < 0 :
    error3()
    if fin <= 100 or fin >= 0 :
        fin = int(input())
    else:
        fin = int(input("Please type your midterm grade "))
print("Your final grade is {}." .format(fin))

pro = int(input("Please type your project grade "))
while pro > 100 or pro < 0 :
    error3()
    if pro <= 100 or pro >= 0 :
        pro = int(input())
    else:
        pro = int(input("Please type your midterm grade "))
print("Your project grade is {}." .format(pro))

grades = {"midterm" : mid, "final" : fin, "project" : pro}

print("Your {} grades are: {};{};{}" .format(courses[lesson],grades["midterm"],grades["final"],grades["project"]))
grade = ((mid*30)+(fin*50)+(pro*20))/100
print("Your {} success score is: {}" .format(courses[lesson],grade))

if grade >= 90 :
    print("Wow! You got AA. Congratulations")
elif grade >= 70 :
    print("You got BB. Congratulations")
elif grade >= 50 :
    print("You got CC. It is good eneough:)")
elif grade >= 30 :
    print("You got DD. Maybe you should work harder:(")
else :
    print("You got FF. LOOOOOSERRRR")   #:D

input("You can push enter for exit to program")
