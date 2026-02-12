# Q8. Hostel Management System (Accommodation Domain)
# Design a HostelRoom class.
# Methods to think about:
# • allocate room (object method)
# • vacate room (object method)
# • calculate monthly fee (object method)
# • update room rent (class method)

import logging

logging.basicConfig(
    filename='hostel.log',
    level=logging.INFO,
    format=" %(asctime)s -  %(levelname)s - %(message)s"
)

class HostelRoom:
    hostel_name="Sarawathi"
    room_rent=4500
    food_charge=3000
    maintenance=500
    laundry=300
    total_rooms=25
    available=25

    def __init__(self,roll_no,stu_name,stay_months):
        self.roll_no=roll_no
        self.stu_name=stu_name
        self.stay_months=stay_months
        self.month_fee=0
        self.room_status="Vacant"

    def allocate_room(self):
        if HostelRoom.available <= 0:
            logging.warning("No rooms available to allocate for %s", self.stu_name)
        elif self.room_status == "Occupied":
            logging.warning("Room already occupied for %s", self.stu_name)
        else:
            self.room_status="Occupied"
            HostelRoom.available-=1
            logging.info("The room is allocated for %s",self.stu_name)

    def vacate_room(self):
        if self.room_status=="Occupied":
            self.room_status="Vacant"
            HostelRoom.available+=1
            logging.info("Room is vacated by %s",self.stu_name)
        else:
            logging.warning("Room already vacant for %s", self.stu_name)

    def monthly_fee(self):
        if self.room_status=="Occupied":
            self.month_fee=HostelRoom.room_rent+HostelRoom.maintenance+HostelRoom.food_charge+HostelRoom.laundry
            logging.info("The total to pay is %s for %s",self.month_fee,self.stu_name)
        else:
            logging.warning("Fee cannot be calculated. Room not occupied for %s",self.stu_name)

    @classmethod
    def update_room_rent(cls,new_rent):
        if new_rent>0:
            cls.room_rent=new_rent
            logging.info("The new room rent is updated successfully to %s",new_rent)
        else:
            logging.warning("The room rent cannot be updated")

h1 = HostelRoom(101, "Manya", 3)

h1.allocate_room()
h1.monthly_fee()

h1.allocate_room()

h1.vacate_room()
h1.vacate_room()

HostelRoom.update_room_rent(5000)

h2 = HostelRoom(202, "Navi", 2)
h2.allocate_room()
h2.monthly_fee()
