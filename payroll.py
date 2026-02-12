# Q6. Employee Payroll System (Corporate Domain)
# Design an Employee class.
# Methods to think about:
# • calculate salary (object method)
# • apply leave deduction (object method)
# • display payslip (object method)
# • update hra percentage (class method)


import logging

logging.basicConfig(
    filename='payroll.log',
    level=logging.INFO,
    format=" %(asctime)s -  %(levelname)s - %(message)s"
)

class Employee:
    comp_name='Capgemini'
    hra_percent=20
    pf=12
    tax=5
    currency='Rupee'

    def __init__(self,emp_id,emp_name,emp_sal):
        self.emp_id=emp_id
        self.emp_name=emp_name
        self.emp_sal=emp_sal
        self.leave = 0
        self.after_sal = 0

    def salary(self):
        hra_pay=(self.emp_sal*Employee.hra_percent)/100
        pf_cut=(self.emp_sal*Employee.pf)/100
        tax_cut=(self.emp_sal*Employee.tax)/100


        self.after_sal=self.emp_sal+hra_pay-pf_cut-tax_cut
        logging.info("Salary calculated | Employee: %s | Net salary: %s",self.emp_name,self.after_sal)
        
    def deduct_leave(self, leave_days):
        if leave_days > 0:
            if self.after_sal > 0:
                self.leave = leave_days
                deduction = (self.emp_sal / 30) * leave_days
                self.after_sal -= deduction
                logging.info("Leave Deducted | Employee: %s | Days: %s | Deduction: %s | New Salary: %s",self.emp_name,leave_days,deduction,self.after_sal)
                
            else:
                logging.warning("Leave before salary | Emp: %s", self.emp_name)
                
        else:
            logging.warning("Invalid leave | %s", self.emp_name)
            


    def display(self):
        return f"""
    -------- PAYSLIP --------
    Company        : {Employee.comp_name}
    Employee ID    : {self.emp_id}
    Employee Name  : {self.emp_name}
    Basic Salary   : {self.emp_sal}
    HRA %          : {Employee.hra_percent}
    PF %           : {Employee.pf}
    Tax %          : {Employee.tax}
    Leaves Taken   : {self.leave}
    Net Salary     : {self.after_sal} {Employee.currency}
    --------------------------
    """

    @classmethod
    def update_hra(cls,new_hra):
        if new_hra>0:
            cls.hra_percent=new_hra
            logging.info("HRA Updated | New HRA Percentage: %s",new_hra)
            
        else:
            logging.warning("Invalid attempt to update | Value: %s",new_hra)
            

e1 = Employee(1001, "Chota Bheem", 75000)

e1.salary()          
e1.deduct_leave(2)   
print(e1.display()) 

Employee.update_hra(25)


e1.salary()
print(e1.display())
