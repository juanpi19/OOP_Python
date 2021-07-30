import datetime

class BikeRental:
    def __init__(self, stock=0):
        self.stock = stock

    def displaystock(self):
        print(f"We currently have {self.stock} available for rent!")

    def rentBikeOnHourlyBasis(self, num_bikes):
        PRICE_PER_HOUR = 5
        if self.stock < 0:
            print(f"Cannot rent a bike since we have {self.stock} bikes availabe for rent")

        elif self.stock < num_bikes:
            print(f"Cannot rent a bike since we have {self.stock} bikes availabe for rent")

        else:
            now = datetime.datetime.now()
            print(f"{now} you have rented {num_bikes} bikes, our hourly price is ${PRICE_PER_HOUR} per hour")
            self.stock -= num_bikes
            return now

    def rentBikeOnDailyBasis(self, num_bikes):
        PRICE_PER_DAY = 20
        if self.stock < 0:
            print(f"Cannot rent a bike since we have {self.stock} bikes availabe for rent")

        elif self.stock < num_bikes:
            print(f"Cannot rent a bike since we have {self.stock} bikes availabe for rent")

        else:
            now = datetime.datetime.now()
            print(f"{now} you have rented {num_bikes} bikes, our hourly price is ${PRICE_PER_DAY} per hour")
            self.stock -= num_bikes
            return now

    def rentBikeOnWeeklyBasis(self, num_bikes):
        PRICE_PER_WEEK = 60
        if self.stock < 0:
            print(f"Cannot rent a bike since we have {self.stock} bikes available for rent")

        elif self.stock < num_bikes:
            print(f"Cannot rent a bike since we have {self.stock} bikes available for rent")

        else:
            now = datetime.datetime.now()
            print(f"{now} you have rented {num_bikes} bikes, our hourly price is ${PRICE_PER_WEEK} per hour")
            self.stock -= num_bikes
            return now

    def familyRental(self, num_bikes):
        if self.stock < 0:
            print(f"Cannot rent a bike since we have {self.stock} bikes available for rent")

        elif self.stock < num_bikes:
            print(f"Cannot rent a bike since we have {self.stock} bikes available for rent")

        elif n < 3 and n > 5:
            print(f"Promotion is only available for 3 to  5 bikes and you have {num_bikes}")

        else:
            now = datetime.datetime.now()
            print(f"{now} you have rented {num_bikes} bikes, our hourly price is ${50} per hour")
            self.stock -= num_bikes
            return now

    def returnBike(self, request):
        # request should be a tuple that includes Rental Time, Rental Basis and Num of bikes

        rentalTime, rentalBasis, num_bikes = request
        bill = 0

        if rentalTime and rentalBasis and num_bikes:
            self.stock += num_bikes
            now = datetime.datetime.now()

            # Hourly basis
            if rentalBasis == 1:
                bill = rentalTime * 5 * num_bikes
                print(f"Your total bill is ${bill}")

            # Daily basis
            elif rentalBasis == 2:
                bill = rentalTime * 20 * num_bikes
                print(f"Your total bills is ${bill}")

            # Weekly basis
            elif rentalBasis == 3:
                bill = rentalTime * 60 * num_bikes
                print(f"Your total bills is ${bill}")

            else:
                pass


            if num_bikes >= 3 and num_bikes <= 5:
                print("You are available for a family discount!")
                bill = bill * 0.7
                print(f"Your new price is ${int(bill)}")

        else:
            print("Did you rent with us?, you must put the rental time, rental basis and number of bikes rented")


class customer:
    def __init__(self):
        self.bikes = 0
        self.rentalBasis = 0
        self.rentalTime = 0
        self.bill = 0

    def requestBike(self):
        bikes = input("How many bikes would you like to rent? ")
        try:
            self.bikes = bikes
        except ValueError:
            print("Tha't not a positive integer")
            return -1

        if 1 < bikes:
            print("Invalid. The number of bikes must be greater than 0")
            return -1

        else:
            self.bikes = bikes
            return self.bikes

    def returnBike(self):
        if self.bikes and self.rentalTime and self.rentalBasis:
            return self.bikes, self.rentalTime, self.rentalBasis

        else:
            return 0,0,0






bike1 = BikeRental(10)
bike1.rentBikeOnHourlyBasis(5)
bike1.returnBike((2, 2, 5))

# LEARNING TO USE GIT
