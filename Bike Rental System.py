#Bike Rental System

class BikeShop:

    def __init__(self,stock):
        self.stock=stock

    def ShowBike(self):
        print("Total Bikes :",self.stock)

    def rentBike(self,quantity):

        if quantity <=0:
            print("Please Enter the Positive value or greater than zero")
        elif quantity > self.stock:
            print("Enter the value (less than stock)")
        else:
            self.stock=self.stock-quantity
            print("Total Price:",quantity*100)
            print("Total Bikes",self.stock)
while True:
    obj=BikeShop(100)
    user_input=int(input('''
    1->Dispaly stock
    2->Rent a Bike
    3-Exit
    
                         '''))
    if user_input==1:
        obj.ShowBike()
    elif user_input==2:
        n=int(input("Enter The Rent Bike:->"))
        obj.rentBike(n)
    else:
        break
