grades = [[5, 3, 3, 5, 4], [2, 2, 2, 3], [4, 5, 5, 2], [4, 4, 3], [5, 5, 5, 4, 5]]
students = {'Johnny', 'Bilbo', 'Steve', 'Khendrik', 'Aaron'}
Aaron = sum(grades[0])/len(grades[0])
Bilbo = sum(grades[1])/len(grades[1])
Johnny = sum(grades[2])/len(grades[2])
Khendrik = sum(grades[3])/len(grades[3])
Steve = sum(grades[4])/len(grades[4])
grades_students = {'Aaron':Aaron, 'Bilbo':Bilbo, 'Johny':Johnny, 'Khendrik':Khendrik, 'Steve':Steve}
print(grades_students)