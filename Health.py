# Q2. Hospital Patient Management (Healthcare Domain)
# Design a Patient class.
# Methods to think about:
# • admit patient (object method)
# • discharge patient (object method)
# • calculate bill (object method)
# • update consultation fee (class method)

class Patient:
    hname='Kims'
    consultation_fee=750
    room_fee=2500
    ambulance_no=108

    def __init__(self,pname,age,gender,disease,blood_group,admitted_days):
        self.pname=pname
        self.age=age
        self.gender=gender
        self.disease=disease
        self.blood_group=blood_group
        self.admitted_days=admitted_days
        self.admitted=False

    def admit_patient(self):
        if self.admitted==False:
            self.admitted=True
            print("Patient Admitted")
        else:
            print("Patient not admitted")
        
    def discharge_patient(self):
        if self.admitted:
            self.admitted=False
            print("Patient Discharged")
        else:
            print("Patient under treatment")

    def total_bill(self):
        if self.admitted:
            bill=(Patient.room_fee*self.admitted_days) + Patient.consultation_fee
            print("To be paid: ",bill)
        else:
            print("Nothing to pay")

    def display(self):
        print(self.pname,self.age,self.gender,self.disease,self.blood_group,self.admitted_days)

    @classmethod
    def update_con_fee(cls,new_fee):
        if new_fee>0:
            cls.consultation_fee=new_fee
            print("Updation done")
        else:
            print("Invalid updation")

        

p1=Patient("Manyasri","21","F","Dengue","O+",7)
p2=Patient("Deeksha","17","F","Jaundice","AB-",12)

p1.display()
p1.admit_patient()
p1.total_bill()

Patient.update_con_fee(1000)

p2.admit_patient()
p2.total_bill()
p2.discharge_patient()
