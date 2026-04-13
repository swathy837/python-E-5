class ElectricityBill:
    def __init__(self, units):
        self.units = units
        self.bill = 0.0

    def calculate_bill(self):
        if self.units <= 100:
            self.bill = 0
        elif self.units <= 200:
            self.bill = ((self.units - 100) * 1.50)
        elif self.units <= 300:
            self.bill =  (100 * 1.50) + ((self.units - 200) * 2.50)
        elif self.units <= 400:
            self.bill = (100* 1.50) + (200*2.50)+((self.units - 300) * 4.00)
        elif self.units >= 401:
            self.bill =((self.units - 400) * 5.00)+(100*1.5)+(200+2.5)+(100*4)
        return self.bill


units_consumed = float(input("Enter units consumed: "))
customer = ElectricityBill(units_consumed)
print("Total Bill:", (customer.calculate_bill()))
