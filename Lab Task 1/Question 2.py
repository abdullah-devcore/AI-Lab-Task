class Student:
    def __init__(self, marks, documents, attendence, assignment):
        self.marks = marks
        self.docs = documents
        self.attendence = attendence
        self.assignment = assignment

    def result(self):
        if self.marks >= 70 and self.documents == "Yes" and self.attendence >= 75 and self.assignment == "Yes":
            return "Pass"
        else:
            return "Fail"

    def final_result(self, expected):
        student_result = self.result()

        print("Input:", self.marks, self.documents, self.attendence, self.assignment)
        print("Expected:", expected)
        print("Actual:", student_result)

  
        if student_result == "Pass":
            print("Reason: All conditions are satisfied.")
        elif self.marks < 70:
            print("Reason: Score is below 70.")
        elif self.documents != "Yes":
            print("Reason: Document is not complete.")
        elif self.attendence < 75:
            print("Reason: Attendance is below 75%.")
        elif self.assignment != "Yes":
            print("Reason: Assignment is not submitted.")
        


# test cases
s1 = Student(80, "Yes", 80, "Yes")
s1.final_result("Pass")

s2 = Student(80, "Yes", 60, "Yes")
s2.final_result("Fail")

s3 = Student(80, "Yes", 80, "No")
s3.final_result("Fail")

s4 = Student(70, "Yes", 75, "Yes")
s4.final_result("Pass")