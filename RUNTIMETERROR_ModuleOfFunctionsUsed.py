import time
from datetime import datetime,tzinfo,timedelta


''' Importing date and time '''
'''Created by Jagdish Naidu'''

class Zone(tzinfo):

    def __init__(self,offset,isdst,name):
        self.offset = offset
        self.isdst = isdst
        self.name = name

    def utcoffset(self, dt):
        return timedelta(hours=self.offset)

    def dst(self, dt):
        return timedelta(hours=1) if self.isdst else timedelta(0)

    def tzname(self, dt):
        return self.name


''' Converting from GMT to IST '''
# GMT = Zone(0,False,'GMT')

IST = Zone(+5.5, False, 'IST')

''' To check if the Vehicle is a car or bike'''

'''Created by Atharv Jaju'''
def is_car_or_bike(vehicletype):
    if vehicletype.upper().lstrip() == "CAR":
        return True

    elif vehicletype.upper().lstrip() == "BIKE":
        return False

    else:
        print("*****------INVALID INPUT-----*****")
        print("Please Re-Enter CAR/ BIKE : ")
        return is_car_or_bike(input(">>> "))


''' To check if the vehicle is entering or exiting '''
'''Created by Atharv Jaju'''


def is_in_or_out(inorout):
    if inorout.upper().lstrip() == "IN":
        return True
    elif inorout.upper().lstrip() == "OUT":
        return False
    else:
        print("*****------INVALID INPUT-----*****")
        print("Please Re-Enter IN/OUT : ")
        inorout = input(">>> ")
        print()
        print()
        print()
        return is_in_or_out(inorout)


''' To search the best parking lot for the car and to generate an entry ticket file '''
'''Created by Atharv Jaju'''

def car_park(carnumber, floors_for_car, columns_for_car, rows_for_car, parkinglot_for_car):

    gotparking_for_car =0
    carnumber = carnumber.upper().lstrip()
    flag_start_filling_in_between_for_car = 0

    for floor_for_car in range(0, floors_for_car):
        if columns_for_car > 2:
            if (columns_for_car - 1)%2 ==0:
                if parkinglot_for_car[floor_for_car][columns_for_car - 1][rows_for_car - 1][0] != "0":
                    flag_start_filling_in_between_for_car = 1
                else:
                    flag_start_filling_in_between_for_car = 0
            else:
                if parkinglot_for_car[floor_for_car][columns_for_car - 2][rows_for_car - 1][0] != "0":
                    flag_start_filling_in_between_for_car = 1
                else:
                    flag_start_filling_in_between_for_car = 0
        else:
            flag_start_filling_in_between_for_car = 1

        for col_for_car in range(0, columns_for_car):

            for row_for_car in range(0, rows_for_car):

                if gotparking_for_car == 0:
                    if flag_start_filling_in_between_for_car == 0:

                        if col_for_car >= 1:

                            if parkinglot_for_car[floor_for_car][col_for_car - 1][row_for_car][0] == "0":

                                if parkinglot_for_car[floor_for_car][col_for_car][row_for_car][0] == "0":
                                    parkinglot_for_car[floor_for_car][col_for_car][row_for_car][0] = carnumber
                                    intime = datetime.now(IST).strftime('%d/%m/%Y %H:%M:%S %Z')
                                    parkinglot_for_car[floor_for_car][col_for_car][row_for_car][1] = str(time.time())
                                    print("PARKING AVAILABLE at: ")
                                    print(f"FLOOR: {floor_for_car + 1}")
                                    print(f"COLUMN: {col_for_car + 1}")
                                    print(f"ROW: {row_for_car + 1}")
                                    for i in range(0, 70000000):
                                        pass
                                    gotparking_for_car = 1
                                    print_bill_in(carnumber, intime, floor_for_car + 1, col_for_car + 1, row_for_car + 1, "Car")
                                    return parkinglot_for_car
                                else:
                                    pass
                            else:
                                pass

                        elif col_for_car == 0:

                            if parkinglot_for_car[floor_for_car][col_for_car][row_for_car][0] == "0":
                                parkinglot_for_car[floor_for_car][col_for_car][row_for_car][0] = carnumber
                                intime = datetime.now(IST).strftime('%d/%m/%Y %H:%M:%S %Z')
                                parkinglot_for_car[floor_for_car][col_for_car][row_for_car][1] = str(time.time())
                                print("PARKING AVAILABLE at: ")
                                print(f"FLOOR: {floor_for_car + 1}")
                                print(f"COLUMN: {col_for_car + 1}")
                                print(f"ROW: {row_for_car + 1}")
                                for i in range(0, 70000000):
                                    pass
                                gotparking_for_car = 1
                                print_bill_in(carnumber, intime, floor_for_car + 1, col_for_car + 1, row_for_car + 1, "Car")
                                return parkinglot_for_car
                            else:
                                pass

                    elif flag_start_filling_in_between_for_car == 1:

                        if parkinglot_for_car[floor_for_car][col_for_car][row_for_car][0] == "0":
                            parkinglot_for_car[floor_for_car][col_for_car][row_for_car][0] = carnumber
                            intime = datetime.now(IST).strftime('%d/%m/%Y %H:%M:%S %Z')
                            parkinglot_for_car[floor_for_car][col_for_car][row_for_car][1] = str(time.time())
                            print("PARKING AVAILABLE at: ")
                            print(f"FLOOR: {floor_for_car + 1}")
                            print(f"COLUMN: {col_for_car + 1}")
                            print(f"ROW: {row_for_car + 1}")
                            for i in range(0, 70000000):
                                pass
                            gotparking_for_car = 1
                            print_bill_in(carnumber, intime, floor_for_car + 1, col_for_car + 1, row_for_car + 1, "Car")
                            return parkinglot_for_car
                        else:
                            pass

    if gotparking_for_car == 0:
        print("PARKING FULL! Sorry! Pls. Visit Again!")
        for i in range(0, 70000000):
            pass
        return parkinglot_for_car




''' To search the best parking lot for the bike and to generate an entry ticket file '''
'''Created by Atharv Jaju'''

def bike_park(bikenumber, floors_for_bike, columns_for_bike, rows_for_bike, parkinglot_for_bike):

    bikenumber = bikenumber.upper().lstrip()
    gotparking_for_bike =0
    flag_start_filling_in_between_for_bike = 0

    for floor_for_bike in range(0, floors_for_bike):
        if columns_for_bike > 2:
            if (columns_for_bike -1)%2 ==0:
                if parkinglot_for_bike[floor_for_bike][columns_for_bike-1][rows_for_bike-1][0] != "0":
                    flag_start_filling_in_between_for_bike = 1
                else:
                    flag_start_filling_in_between_for_bike = 0
            else:
                if parkinglot_for_bike[floor_for_bike][columns_for_bike-2][rows_for_bike-1][0] != "0":
                    flag_start_filling_in_between_for_bike = 1
                else:
                    flag_start_filling_in_between_for_bike = 0
        else:
            flag_start_filling_in_between_for_bike = 1

        for col_for_bike in range(0, columns_for_bike):

            for row_for_bike in range(0, rows_for_bike):

                if gotparking_for_bike == 0:
                    if flag_start_filling_in_between_for_bike == 0:

                        if col_for_bike >= 1:

                            if parkinglot_for_bike[floor_for_bike][col_for_bike - 1][row_for_bike][0] == "0":

                                if parkinglot_for_bike[floor_for_bike][col_for_bike][row_for_bike][0] == "0":
                                    parkinglot_for_bike[floor_for_bike][col_for_bike][row_for_bike][0] = bikenumber
                                    intime = datetime.now(IST).strftime('%d/%m/%Y %H:%M:%S %Z')
                                    parkinglot_for_bike[floor_for_bike][col_for_bike][row_for_bike][1] = str(time.time())
                                    print("PARKING AVAILABLE at: ")
                                    print(f"FLOOR: {floor_for_bike + 1}")
                                    print(f"COLUMN: {col_for_bike + 1}")
                                    print(f"ROW: {row_for_bike + 1}")
                                    for i in range(0, 70000000):
                                        pass
                                    gotparking_for_bike = 1
                                    print_bill_in(bikenumber, intime, floor_for_bike + 1, col_for_bike + 1, row_for_bike + 1, "Bike")
                                    return parkinglot_for_bike
                                else:
                                    pass
                            else:
                                pass

                        elif col_for_bike == 0:

                            if parkinglot_for_bike[floor_for_bike][col_for_bike][row_for_bike][0] == "0":
                                parkinglot_for_bike[floor_for_bike][col_for_bike][row_for_bike][0] = bikenumber
                                intime = datetime.now(IST).strftime('%d/%m/%Y %H:%M:%S %Z')
                                parkinglot_for_bike[floor_for_bike][col_for_bike][row_for_bike][1] = str(time.time())
                                print("PARKING AVAILABLE at: ")
                                print(f"FLOOR: {floor_for_bike+1}")
                                print(f"COLUMN: {col_for_bike+1}")
                                print(f"ROW: {row_for_bike+1}")
                                for i in range(0, 70000000):
                                    pass
                                gotparking_for_bike = 1
                                print_bill_in(bikenumber, intime, floor_for_bike + 1, col_for_bike + 1, row_for_bike + 1, "Bike")
                                return parkinglot_for_bike
                            else:
                                pass

                    elif flag_start_filling_in_between_for_bike == 1:

                        if parkinglot_for_bike[floor_for_bike][col_for_bike][row_for_bike][0] == "0":
                            parkinglot_for_bike[floor_for_bike][col_for_bike][row_for_bike][0] = bikenumber
                            intime = datetime.now(IST).strftime('%d/%m/%Y %H:%M:%S %Z')
                            parkinglot_for_bike[floor_for_bike][col_for_bike][row_for_bike][1] = str(time.time())
                            print("PARKING AVAILABLE at: ")
                            print(f"FLOOR: {floor_for_bike+1}")
                            print(f"COLUMN: {col_for_bike+1}")
                            print(f"ROW: {row_for_bike+1}")
                            for i in range(0, 70000000):
                                pass
                            gotparking_for_bike = 1
                            print_bill_in(bikenumber, intime, floor_for_bike + 1, col_for_bike + 1, row_for_bike + 1, "Bike")
                            return parkinglot_for_bike
                        else:
                            pass

    if gotparking_for_bike == 0:
        print("PARKING FULL! Sorry! Pls. Visit Again!")
        for i in range(0, 70000000):
            pass
        return parkinglot_for_bike

''' To remove the car, mark that slot as 'available' again, appending the entry ticket file with exit ticket details'''

'''Created by Jagdish Naidu'''
def car_remove(carnumber, floors_for_car, columns_for_car, rows_for_car, parkinglot_for_car):

    timedifference = 0

    for floor_for_car in range(0, floors_for_car):
        for col_for_car in range(0, columns_for_car):
            for row_for_car in range(0, rows_for_car):

                if parkinglot_for_car[floor_for_car][col_for_car][row_for_car][0] == carnumber.upper().lstrip():
                    outtime = datetime.now(IST).strftime('%d/%m/%Y %H:%M:%S %Z')
                    intime = float(parkinglot_for_car[floor_for_car][col_for_car][row_for_car][1])
                    timedifference = time.time() - intime
                    bill = print_bill_out(carnumber, outtime, timedifference, "CAR")
                    print(f"YOUR BILL IS Rs. {bill}")
                    print(f"PICK YOUR CAR FROM: Floor: {floor_for_car+1}, Column: {col_for_car+1}, Row: {row_for_car+1}")
                    parkinglot_for_car[floor_for_car][col_for_car][row_for_car][0] = "0"
                    parkinglot_for_car[floor_for_car][col_for_car][row_for_car][1] = "0"
                    return parkinglot_for_car


''' To remove the bike, mark that slot as 'available' again, 
appending the entry ticket file with exit ticket details '''
'''Created by Jagdish Naidu'''


def bike_remove(bikenumber, floors_for_bike, columns_for_bike, rows_for_bike, parkinglot_for_bike):
    flag = 0
    timedifferenceforbike = 0

    for floor_for_bike in range(0, floors_for_bike):
        for col_for_bike in range(0, columns_for_bike):
            for row_for_bike in range(0, rows_for_bike):

                if parkinglot_for_bike[floor_for_bike][col_for_bike][row_for_bike][0] == bikenumber.upper().lstrip():
                    outtime = datetime.now(IST).strftime('%d/%m/%Y %H:%M:%S %Z')
                    intime = float(parkinglot_for_bike[floor_for_bike][col_for_bike][row_for_bike][1])
                    timedifference = time.time() - intime
                    print_bill_out(bikenumber, outtime, timedifference, "BIKE")
                    print(f"PICK UP YOUR BIKE FROM: Floor: {floor_for_bike}, Column: {col_for_bike}, Row: {row_for_bike}")
                    flag = 1
                    parkinglot_for_bike[floor_for_bike][col_for_bike][row_for_bike][0] = "0"
                    parkinglot_for_bike[floor_for_bike][col_for_bike][row_for_bike][1] = "0"
                    return parkinglot_for_bike


''' To check the validity of lots that are marked unavailable by the manager for cars '''
'''Created by Teja Swaroop'''


def validity_of_lots_cars(particular_lot, floors_for_cars, columns_for_cars, rows_for_cars):
    particular_lot += ','
    j = -1
    x = []
    i = 0
    while i < len(particular_lot):
        if particular_lot[i] != ',':
            pass
        elif particular_lot[i] == ',':
            if particular_lot[j + 1:i].isdigit():
                x.append(int(particular_lot[j + 1:i]))
                j = i
            else:
                return False

        i += 1
    if len(x) == 3 and 1 <= x[0] <= floors_for_cars and 1 <= x[1] <= columns_for_cars and 1 <= x[2] <= rows_for_cars:
        return True
    else:
        return False


'''  To mark the unavailable lots for cars as 'Filled forever'  if the lot entered exists'''
'''Created by Teja Swaroop'''


def unavailable_lots_for_cars(unavailablelot, parkinglot_for_cars, floors_for_cars, columns_for_cars, rows_for_cars):

    if validity_of_lots_cars(unavailablelot, floors_for_cars, columns_for_cars, rows_for_cars):
        j = -1
        unavailablelot += ','
        x = []
        i = 0
        while i < len(unavailablelot):
            if unavailablelot[i] != ',':
                pass
            elif unavailablelot[i] == ',':
                x.append(int(unavailablelot[j + 1:i]))
                j = i
            i += 1

        parkinglot_for_cars[x[0] - 1][x[1] - 1][x[2] - 1][0] = 'Filled forever'
        print("Successfully marked this lot unavailable")
        return parkinglot_for_cars
    else:
        print("-----*****INVALID number of floors/columns/rows*****-----")
        print("Highest number of floors is ", floors_for_cars, ",", "Highest number of columns is ", columns_for_cars,
              ",Highest number of rows is ", rows_for_cars)
        print("Please check again and make sure to type in specified format")
        print("RE-ENTER the NOT AVAILABLE LOT: ")
        un_lot = input(">>> ")
        unavailable_lots_for_cars(un_lot, parkinglot_for_cars, floors_for_cars, columns_for_cars, rows_for_cars)


''' To check the validity of lots that are marked unavailable by the manager for bikes '''
'''Created by Teja Swaroop'''


def validity_of_lots_bikes(particular_lot, floors_for_bikes, columns_for_bikes, rows_for_bikes):
    particular_lot += ','
    j = -1
    x = []
    i = 0
    while i < len(particular_lot):
        if particular_lot[i] != ',':
            pass
        elif particular_lot[i] == ',':
            if particular_lot[j + 1:i].isdigit():
                x.append(int(particular_lot[j + 1:i]))
                j = i
        i += 1
    if len(x) == 3 and 1 <= x[0] <= floors_for_bikes and 1 <= x[1] <= columns_for_bikes and 1 <= x[2] <= rows_for_bikes:
        return True
    else:
        return False


'''  To mark the unavailable lots for bikes as 'Filled forever' if entered lot exists '''
'''Created by Teja Swaroop'''


def unavailable_lots_for_bikes(unavailablelot, parkinglot_for_bikes, floors_for_bikes, columns_for_bikes, rows_for_bikes):

    if validity_of_lots_bikes(unavailablelot,floors_for_bikes, columns_for_bikes, rows_for_bikes):
        j = -1
        unavailablelot += ','
        x = []
        i = 0
        while i < len(unavailablelot):
            if unavailablelot[i] != ',':
                pass
            elif unavailablelot[i] == ',':
                x.append(int(unavailablelot[j + 1:i]))
                j = i
            i += 1
        parkinglot_for_bikes[x[0] - 1][x[1] - 1][x[2] - 1][0] = 'Filled forever'
        print("Successfully marked this lot unavailable")
        return parkinglot_for_bikes
    else:
        print("-----*****INVALID number of floors/columns/rows*****-----")
        print("Highest number of floors is ", floors_for_bikes, ",", "Highest number of columns is ", columns_for_bikes,
              ",Highest number of rows is ", rows_for_bikes)
        print("Please check again and make sure to type in specified format")
        print("RE-ENTER the NOT AVAILABLE LOT: ")
        un_lot = input(">>> ")
        unavailable_lots_for_bikes(un_lot, parkinglot_for_bikes, floors_for_bikes, columns_for_bikes, rows_for_bikes)


''' Checking if the vehicle entering has a valid licence number '''
'''Created by Teja Swaroop'''


def validity_of_licence(lic_number):
    carnum = lic_number.lstrip()

    if carnum[0:2].isalpha() and carnum[3:5].isdigit() and carnum[6:8].isalpha() and carnum[9:].isdigit():
        return True
    else:
        return False


''' Search for vehicle with same licence number parked 
in the parking lot, if licence number of the 
entering vehicle matches with the vehicle which is 
already parked inside, we report this to the police '''
'''Created by Jagdish Naidu'''


def found_duplicate(lic_number, floors_for_bike, columns_for_bike, rows_for_bike, floors_for_car, columns_for_car, rows_for_car, parkinglot_for_car, parkinglot_for_bike):

    flag_duplicate = 0

    for floor_for_bike in range(0, floors_for_bike):
        for col_for_bike in range(0, columns_for_bike):
            for row_for_bike in range(0, rows_for_bike):

                if parkinglot_for_bike[floor_for_bike][col_for_bike][row_for_bike][0] == lic_number.upper().lstrip():
                    flag_duplicate = 1

    for floor_for_car in range(0, floors_for_car):
        for col_for_car in range(0, columns_for_car):
            for row_for_car in range(0, rows_for_car):

                if parkinglot_for_car[floor_for_car][col_for_car][row_for_car][0] == lic_number.upper().lstrip():
                    flag_duplicate =1

    if flag_duplicate == 1:
        return True
    else:
        return False


''' To generate a bill for entering vehicle '''
'''Created by Jagdish Naidu'''

def print_bill_in(carnumber, intime, floor, col, row, vehicletype):
    bill_in = open(carnumber.upper(), 'a')
    bill_in.write("-------------------------------------------------------Welcome To RUNTIME PARKING-------------------------------------------------------" + "\n")
    bill_in.write("\n")
    bill_in.write("Type of vehicle: " + str(vehicletype) + "\n")
    bill_in.write("Entered date and time is: " + str(intime) + "\n")
    bill_in.write("Your " + str(vehicletype)+ " is parked at  Floor number: " + str(floor) + ", Column number: " + str(col) + ", Row number: " + str(row) + "\n")
    bill_in.write("\n")
    bill_in.write("----------------------------------------------------------------------------------" + "\n")
    bill_in.close()


''' To append entry bill with exit details and calculate the bill '''
'''Created by Jagdish Naidu'''


def print_bill_out(number_plate, out_time, period, vehicletype):

    timein_minutes = int(period) / 60

    if 0 <= timein_minutes <= 1:
        bill = 1

    elif 1 < timein_minutes <= 2:
        bill = (timein_minutes - 1) * 0.7 + 1

    elif 2 < timein_minutes <= 3:
        bill = (timein_minutes - 2) * 0.6 + 0.7 + 1

    else:
        bill = (timein_minutes - 3) * 0.5 + 0.6 + 0.7 + 1

    bill = float(str(bill)[0:str(bill).find(".")+3])

    print("Amount to be paid is: Rs ", bill)
    timein_minutes = str(timein_minutes)
    timein_minutes = timein_minutes[0 : (timein_minutes.find(".") + 3)]
    print("Total time your ", vehicletype, " is parked is ", timein_minutes, " minutes")
    bill_out = open(number_plate.upper(), 'a')
    bill_out.write("\n")
    bill_out.write("Exit Date and Time is " + str(out_time) + "\n")
    bill_out.write("Total Time Car Parked is " + str(timein_minutes) + "minutes" + "\n")
    bill_out.write("Bill For Parking is Rs. " + str(bill) + "\n")
    bill_out.write("\n")
    bill_out.write("----------------------------------------------------- ***** THANK YOU for visiting ***** -----------------------------------------------------" + "\n")
    bill_out.write("----------------------------------------------------------- ***** VISIT AGAIN ***** ----------------------------------------------------------" + "\n")
    bill_out.write("\n")
    bill_out.write("\n")
    bill_out.write("\n")
    bill_out.close()

    return bill


''' To check if the licence number entered is of a car that is parked in the parking lot. 
Only if it is parked then we pass the value to the car remove function'''
'''Created by Teja Swaroop'''


def found_duplicate_car(lic_number, floors_for_bike, columns_for_bike, rows_for_bike, floors_for_car, columns_for_car, rows_for_car, parkinglot_for_car, parkinglot_for_bike):

    flag_duplicate = 0

    for floor_for_car in range(0, floors_for_car):
        for col_for_car in range(0, columns_for_car):
            for row_for_car in range(0, rows_for_car):

                if parkinglot_for_car[floor_for_car][col_for_car][row_for_car][0] == lic_number.upper().lstrip():
                    flag_duplicate =1

    if flag_duplicate == 1:
        return True
    else:
        return False


''' To check if the licence number entered is of a bike that is parked in the parking lot. 
Only if it is parked then we pass the value to the car remove function'''
'''Created by Atharv Jaju'''


def found_duplicate_bike(lic_number, floors_for_bike, columns_for_bike, rows_for_bike, floors_for_car, columns_for_car, rows_for_car, parkinglot_for_car, parkinglot_for_bike):

    flag_duplicate = 0

    for floor_for_bike in range(0, floors_for_bike):
        for col_for_bike in range(0, columns_for_bike):
            for row_for_bike in range(0, rows_for_bike):

                if parkinglot_for_bike[floor_for_bike][col_for_bike][row_for_bike][0] == lic_number.upper().lstrip():
                    flag_duplicate = 1

    if flag_duplicate == 1:
        return True
    else:
        return False


''' END OF PROGRAM '''
