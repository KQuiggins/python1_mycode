import pickle

# Kenneth Quiggins
# Program #5
# CIT 144

class Students(object):

    def __init__(self, sid, name, midterm, final):
        self._id = sid
        self._name = name
        self._midterm = midterm
        self._final = final


    def calcGrade(self):
        
        grade = (self._midterm + self._final) / 2

        if 90 <= grade <= 100:
            grade = "A"
        elif 80 <= grade <= 89:
            grade = "B"
        elif 70 <= grade <= 79:
            grade = "C"
        elif 65 <= grade <= 69:
            grade = "D"
        elif grade <= 65:
            grade = "F"

        return grade


    def getStudentInfo(self):
        grade = self.calcGrade()
        return "%-4s %-10s %-8d %-8d %3s" % (self._id, self._name, self._midterm, self._final, grade)


def addStudent(f):
    try:
        student_id = input("Please enter the students ID number: ")
        name = input("Please enter the students name: ")
        midterm = int(input("Please enter the students midterm exam score: "))
        final = int(input("Please enter the students score for the final exam: "))
        f[student_id] = Students(student_id, name, midterm, final)

    except ValueError:
        print("Some data entered is invalid, please try again.")

    return f

def displayData(scores):
    if len(scores) > 0:
        print()
        print("%-4s %-8s %-9s %-9s %-6s" % ("ID", "Name", "Midterm", "Final", "Grade"))

        for f in scores:
            print(scores[f].getStudentInfo())

    else:
        print()
        print("Sorry no student info available")



def readData(fHand):

    
    try:
        f = open(fHand, "rb")
        d = pickle.load(f)
        f.close()

    except IOError:
        d = {}

    return d


def storeData(fHand, f):
    fH = open(fHand, "wb")
    pickle.dump(f, fH)
    fH.close()


def deleteStudent(s, student_id):
    try:
        del s[student_id]
        print("Student deleted")

    except:
        print("Student ID not valid")

    return s



def main():

    fHand = 'Grades.txt'
    scores = readData(fHand)

    while True:

        print("""
        Menu options. Choose 1, 2, 3, 4, or 5
           1. Display all students
           2. Add a student
           3. Student look-up
           4. Delete a student
           5. Save and exit
           """)

        option = input("Please enter a choice (1-5): ")

        if option == "1":
            displayData(scores)

        elif option == "2":
            addStudent(scores)

        elif option == "3":
            print()
            student_id = input("Please enter a student's id number to look-up: ")
            print("%-4s %-8s %-9s %-9s %-6s" % ("ID", "Name", "Midterm", "Final", "Grade"))

            print(scores[student_id].getStudentInfo())

        elif option == "4":
            print()
            student_id = input("Please enter a student ID to delete: ")
            student = deleteStudent(scores, student_id)

        elif option == "5":
            storeData(fHand, scores)
            print("Goodbye")
            print()
            break

        else:
            print("Invalid entry, please try again")
            print()

main()

