grades = [[5, 3, 3, 5, 4], [2, 2, 2, 3], [4, 5, 5, 2], [4, 4, 3], [5, 5, 5, 4, 5]]
students = {'Johnny', 'Bilbo', 'Steve', 'Khendrik', 'Aaron'}
grades1 = [sum(grades[0]) / len(grades[0]), sum(grades[1]) / len(grades[1]),
           sum(grades[2]) / len(grades[2]), sum(grades[3]) / len(grades[3]),
           sum(grades[4]) / len(grades[4])]
students1 = sorted(students)
dictionary = {students1[0]: grades1[0], students1[1]: grades1[1],
              students1[2]: grades1[2], students1[3]: grades1[3],
              students1[4]: grades1[4]}
print(dictionary)
