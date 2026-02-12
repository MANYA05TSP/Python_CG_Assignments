# Q7. Railway Ticket Booking (Transport Domain)
# Design a Ticket class.
# Methods to think about:
# • book ticket (object method)
# • cancel ticket (object method)
# • calculate fare (object method)
# • update base fare (class method)

import logging

logging.basicConfig(
    filename='ticket.log',
    level=logging.INFO,
    format=" %(asctime)s -  %(levelname)s - %(message)s"
)

class Ticket:
    base_fare=5
    reservation=50
    cancellation=100

    def __init__(self,passenger_name,age,start,end,dist,coach):
        self.passenger_name=passenger_name
        self.age=age
        self.start=start
        self.end=end
        self.dist=dist
        self.coach=coach
        self.booking_status="Not booked"
        self.fare=0

    def book_ticket(self):
        if self.booking_status=="Not booked":
            self.booking_status="Booked"
            logging.info("Ticket is booked successfully for %s",self.passenger_name)
        else:
            logging.warning("Ticket is already booked for %s",self.passenger_name)

    def cancel_ticket(self):
        if self.booking_status=="Booked":
            refund=self.fare-Ticket.cancellation
            if refund<0:
                refund=0
            self.booking_status="Cancelled"
            logging.info("Ticket cancelled by %s. Refund amount: %s",self.passenger_name, refund)
        else:
            logging.warning("Cancellation failed . Ticket not booked by %s to cancel.",self.passenger_name)

    def calc_fare(self):
        if self.booking_status=="Booked":
            self.fare=(self.dist*Ticket.base_fare) + Ticket.reservation
            logging.info("The total fare for %s is %s ",self.passenger_name,self.fare)
        else:
            logging.warning("Ticket not booked by %s",self.passenger_name)

    @classmethod
    def update_basefare(cls,new_fare):
        if new_fare>0:
            cls.base_fare=new_fare
            logging.info("The new fare is updated successfully")
        else:
            logging.warning("Invalid")

t1 = Ticket("Manya", 20, "Hyderabad", "Chennai", 600, "Sleeper")

t1.book_ticket()
t1.calc_fare()
t1.cancel_ticket()

t2 = Ticket("Navi", 28, "Pune", "Goa", 500, "AC")
t2.cancel_ticket()

t3 = Ticket("Sravani", 22, "Hyderabad", "Vijayawada", 300, "Sleeper")

t3.book_ticket()
t3.calc_fare()
t3.cancel_ticket()
