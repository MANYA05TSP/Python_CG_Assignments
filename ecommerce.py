# E-Commerce Order System (Retail Domain)
# Design an Order class.
# Methods to think about:
# • place order (object method)
# • cancel order (object method)
# • calculate total price (object method)
# • update tax percentage (class method)

class Order:
    app='AJIO'
    delivery_charge=45
    tax_percent=22
    currency='Rupee'

    def __init__(self,order_id,cust_name,pincode,total_cost):
        self.order_id=order_id
        self.cust_name=cust_name
        self.pincode=pincode
        self.total_cost=total_cost
        self.placed=False
        self.cancel=False

    def place_order(self):
        if not self.placed:
            self.placed=True
            print("Order placed successfully")
        else:
            print("Order not placed.Try again")

    def cancel_order(self):
        if self.placed and not self.cancel:
            self.cancel=True
            print("Order cancelled")
        else:
            print("Order not cancelled")

    def total_price(self):
        if self.placed:
            tax_money=(Order.tax_percent*self.total_cost)/100
            price_to_pay=tax_money+self.total_cost+Order.delivery_charge
            print("Total Bill: ",price_to_pay)
        else:
            print("Go & Buy products first")

    @classmethod
    def update_tax(cls,new_tax):
        if new_tax>0:
            cls.tax_percent=new_tax
            print("Update successful")
        else:
            print("Invalid")

o1 = Order(2911, "Molu", 500090, 2500)

o1.place_order()
o1.total_price()

Order.update_tax(18)

o1.total_price()
