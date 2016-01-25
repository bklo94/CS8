# lab06.py
# Brandon Lo and Ryan Meek, 5/12/15
# grade-point functions using a dictionary and a list

# useful constants: a dictionary to look up points
# for a given grade, and a list of grades in the
# order one would print them (since the dictionary
# will store them in a seemingly random order
points = {'A+':4.0, 'A':4.0, 'A-':3.7,
          'B+':3.3, 'B':3.0, 'B-':2.7,
          'C+':2.3, 'C':2.0, 'C-':1.7,
          'D+':1.3, 'D':1.0, 'D-':0.7,
          'F':0.0}
order = ['A+', 'A', 'A-', 'B+', 'B', 'B-',
         'C+', 'C', 'C-', 'D+', 'D', 'D-', 'F']


def printTable(points):
    print("grade ","points")
    for item in order:
        print (item, "\t", points[item])

#test printTable
printTable(points)

def gpa(gradeList):
    acc = 0
    for item in gradeList:
         grade = ( points[item])
         acc = acc + grade
    a = acc
    b = len(gradeList)
    c = a / b
    print (c)


#test myGrades
myGrades = ['B+','A-','B', 'A']
gpa(myGrades)

myGrades = ['A-','A-','A-', 'A-']
gpa(myGrades)

