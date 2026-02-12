# Q10. Movie Ticket Booking (Entertainment Domain)
# Design a MovieTicket class.
# Methods to think about:
# • book seat (object method)
# • cancel booking (object method)
# • calculate ticket price (object method)
# • update ticket price (class method)

import logging

logging.basicConfig(
    filename='movie.log',
    level=logging.INFO,
    format=" %(asctime)s -  %(levelname)s - %(message)s"
)

class MovieTicket:
    theatre_name = "Prasads"
    ticket_price = 200
    premium = 100
    tax = 18
    total_seats = 150
    available_seats = 150

    def __init__(self,movie_name,name,show_time,seat_type):
        self.movie_name=movie_name
        self.name=name
        self.show_time=show_time
        self.seat_type = seat_type
        self.seatno=None
        self.status="Not booked"
        self.price=0

    def book_seat(self):
        if self.status=="Not booked" and MovieTicket.available_seats > 0 :
            MovieTicket.available_seats-=1
            self.status="Booked"
            logging.info("Ticket is booked for %s by %s",self.movie_name,self.name)
        elif self.status=="Booked":
            logging.warning("Ticket already booked by %s", self.name)
        else:
            logging.warning("House full for %s",self.movie_name)

    def cancel_booking(self):
        if self.status=="Booked":
            self.status="Not booked"
            MovieTicket.available_seats+=1
            logging.info("Ticket is cancelled by %s",self.name)
        else:
            logging.warning("Ticket not booked")

    def calculate_ticket_price(self):
        normal_price = MovieTicket.ticket_price

        if self.seat_type == "Premium":
            normal_price += MovieTicket.premium

        tax_amount = (normal_price * MovieTicket.tax) / 100
        self.price = normal_price + tax_amount

        logging.info("Final ticket price for %s is %s",self.name, self.price)

    @classmethod
    def update_t_price(cls, new_price):
        if new_price > 0:
            cls.ticket_price = new_price
            logging.info("Ticket price updated successfully to %s",new_price)
        else:
            logging.warning("Invalid ticket price entered")

m1 = MovieTicket("Pushpa 2", "Manya", "7PM", "Premium")

m1.book_seat()
m1.calculate_ticket_price()

MovieTicket.update_t_price(250)

m3 = MovieTicket("Leo", "Sravani", "4PM", "Premium")
m3.book_seat()
m3.calculate_ticket_price()

