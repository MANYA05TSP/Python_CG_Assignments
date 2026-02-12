# Q3. Library Book System (Education Domain)
# Design a LibraryBook class.
# Methods to think about:
# • issue book (object method)
# • return book (object method)
# • calculate fine (object method)
# • update fine per day (class method)

class LibraryBook:
    libname="Granthalay"
    fine_per_day=20
    loc="Granthasthal"
    due_days=30
    
    def __init__(self,book_name,author,book_no,book_cost):
        self.book_name=book_name
        self.author=author
        self.book_no=book_no
        self.book_cost=book_cost
        self.issued=False

    def issue_book(self):
        if self.issued == False:
            self.issued=True
            print("Book issued")
        else:
            print("Book is in the Library itself")

    def return_book(self):
        if self.issued:
            self.issued=False
            print("Book returned")
        else:
            print("Book is still not returned")

    def total_fine(self,days_kept,lost=False):

        if lost:
            return self.book_cost
        
        if days_kept<=LibraryBook.due_days:
            print("No fine imposed")
            return 0
        
        late_days=days_kept-LibraryBook.due_days
        fine=late_days*LibraryBook.fine_per_day
        months_late=late_days//30
        extra_charge=months_late*50
        total=fine+extra_charge

        print("Fine to be paid is : ",total)

    def display(self):
        print(self.book_name,self.author,self.book_no,self.book_cost)


    @classmethod
    def update_fine(cls,new_fine):
        if new_fine>0:
            cls.fine_per_day=new_fine
            print("New fine ")
        else:
            print("Old fine")

s1=LibraryBook("Logic Gates","Anand Kumar","12345",350)
s2=LibraryBook("Magic","Anonymous","45678",225)
s1.issue_book()
s1.total_fine(31)

s1.display()



            