# Q4. Online Exam System (EdTech Domain)
# Design an Exam class.
# Methods to think about:
# • start exam (object method)
# • submit exam (object method)
# • calculate score (object method)
# • update pass marks (class method)

class Exam:
    p_name = "Imocha"
    pass_marks = 60
    total_marks = 100

    def __init__(self, sname):
        self.sname = sname
        self.score = 0
        self.is_started = False
        self.is_submitted = False

    def start_exam(self):
        if not self.is_started:
            self.is_started = True
            print("Exam started")
        else:
            print("Exam already started")

    def submit_exam(self, score):
        if self.is_started:
            if score <= Exam.total_marks:
                self.score = score
                self.is_submitted = True
                print("Exam submitted")
            else:
                print("Score cannot exceed total marks")
        else:
            print("Start the exam first")

    def calc_score(self):
        if self.is_submitted:
            print("Marks scored:", self.score)

            if self.score >= Exam.pass_marks:
                print("PASS")
            else:
                print("FAIL")
        else:
            print("Exam yet to be submitted")

    

    @classmethod
    def update_pass(cls, new_pass):
        if new_pass > 0:
            cls.pass_marks = new_pass
            print("Pass marks updated successfully")
        else:
            print("Enter valid pass marks")


s1=Exam("Dolu")
s1.start_exam()
s1.submit_exam(65)
s1.calc_score()

Exam.update_pass(50)

s1.submit_exam(42)
s1.calc_score()
