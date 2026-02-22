class student:
    def __init__(self,name,marks1,marks2,marks3,marks4,marks5):
        self.name=name
        self.marks=[marks1,marks2,marks3,marks4,marks5]


    def total(self):
       return sum(self.marks)

    def avg(self):
        return sum(self.marks)/5


    def grade(self):
     grades=self.avg()

     if grades>=90:
         return "Grade A"
     elif grades>=75:
         return "Grade B"
     elif grades>=50:
        return "Grade C"
     else:
         return "Grade D"


    def store_details(self):
     with open("student.txt","a") as f:
         f.write(
             f"Name:{self.name}\n "
             f"Total marks:{self.total()}\n"
             f" Average marks:{self.avg()}\n "
             f"Grade:{self.grade()}\n")

def view_details():
    try:
       with open("student.txt","r") as f:
         print("------Student Result Details------")
         print(f.read())
    except FileNotFoundError:
         print("File not found")


def valid_marks_limit(subject_number):
    while True:
        try:
            marks = int(input(f"Enter marks of sub {subject_number}: "))

            if 0 <= marks <= 100:
                return marks
            else:
                print("Invalid marks! Enter between 0 and 100.")
        except ValueError:
            print("Invalid input! Please enter numbers only.")


while True:
    print("-----Student Result Manager-----")
    print("1:-Add Student")
    print("2:-View Student Details")
    print("3:-Quit")
    choice=int(input("Enter your choice:"))
    if choice==1:
        name=input("Enter student name: ")
        marks1=valid_marks_limit(1)
        marks2=valid_marks_limit(2)
        marks3=valid_marks_limit(3)
        marks4=valid_marks_limit(4)
        marks5=valid_marks_limit(5)

        student1=student(name,marks1,marks2,marks3,marks4,marks5)
        print("Total marks:",student1.total(),"/500")
        print("Average marks:",student1.avg(),"/100")
        print("Grade:",student1.grade())
        student1.store_details()
        print("Student Details saved successfully!")

    elif choice==2:
        view_details()


    elif choice==3:
        print("Stopping program!")
        exit()

    else:
        print("Invalid choice!")










