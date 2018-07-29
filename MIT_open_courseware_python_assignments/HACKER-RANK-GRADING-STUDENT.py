def gradingstudent(grades):
    final_grades =[]
    for grade in grades:
        if grade > 37:
            if (grade % 10) <= 5:
                diff = 5 - (grade % 10)
                if diff < 3:
                    grade = grade + diff
            elif(grade % 10) > 5:
                diff = 10 - grade % 10
                if diff < 3:
                    grade = grade + diff
            final_grades.append(grade)
        else:
            final_grades.append(grade)
    print "final_grade",final_grades

grades = [73,67,38,33]
gradingstudent(grades)
