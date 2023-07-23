'''THIS PART OF CODE WAS CREATED BY Teja Swaroop, Jagdeesh Naidu and Atharv Jaju together'''
import RUNTIMETERROR_ModuleOfFunctionsUsed as AF

''' importing all the functions from the All_Functions module as AF '''

print("STARTING YOUR PERSONALIZED PARKING LOT...")

for i in range(0, 30000000):
    if i % 10000000 ==0:
        print("🙂", end= " ")
print()

print("ENTERING 'MANAGER MODE'", end=" ")

print()
print()
print()
print()

''' asking the owner about the plot of parking place '''

''' asking them about the number of floors for parking for car '''

while True:
    print("Enter number of FLOORS for CARS")
    floors_for_c = input(">>> ")
    if floors_for_c.isdigit():
        floors_for_cars = int(floors_for_c)
        break
    else:
        print("*****Invalid Input*****")
        print("RE - ENTER: ")

''' asking them about the number of columns at each floor for car'''

while True:
    print("Enter number of COLUMNS at each floor for CARS")
    columns_for_c = input(">>> ")
    if columns_for_c.isdigit():
        columns_for_cars = int(columns_for_c)
        break
    else:
        print("*****Invalid Input*****")
        print("RE - ENTER: ")

''' asking them about the number of rows at each floor for car'''

while True:
    print("Enter number of ROWS in each column for CARS")
    rows_for_c = input(">>> ")
    if rows_for_c.isdigit():
        rows_for_cars = int(rows_for_c)
        break
    else:
        print("*****Invalid Input*****")
        print("RE - ENTER: ")

print()
print()
print()

''' asking them about the number of floors for parking for bike '''

while True:
    print("Enter number of FLOORS for BIKES")
    floors_for_b = input(">>> ")
    if floors_for_b.isdigit():
        floors_for_bikes = int(floors_for_b)
        break
    else:
        print("*****Invalid Input*****")
        print("RE - ENTER: ")

''' asking them about the number of columns at each floor for bike '''

while True:
    print("Enter number of COLUMNS at each floor for BIKES")
    columns_for_b = input(">>> ")
    if columns_for_b.isdigit():
        columns_for_bikes = int(columns_for_b)
        break
    else:
        print("*****Invalid Input*****")
        print("RE - ENTER: ")

''' asking them about the number of rows at each floor for bike '''

while True:
    print("Enter number of ROWS in each column for BIKES")
    rows_for_b = input(">>> ")
    if rows_for_b.isdigit():
        rows_for_bikes = int(rows_for_b)
        break
    else:
        print("*****Invalid Input*****")
        print("RE - ENTER: ")

''' preparing a 4D - list to store data '''

pl_for_cars = [[[["0" for i in range(0, 2)] for j in range(0, rows_for_cars)] for k in range(0, columns_for_cars)] for l in range(0, floors_for_cars)]
pl_for_bikes = [[[["0" for i in range(0, 2)] for j in range(0, rows_for_bikes)] for k in range(0, columns_for_bikes)]
                for l in range(0, floors_for_bikes)]

vehicle_type = ""

print()
print()
print()





print()
print()
print()
''' confirming if there are any unavailable lot due to any technical issues '''

while True:
    print("Are any lots NOT available in the CAR PARKING LOT ?")
    print("Enter YES/NO ")
    car_park_un = input(">>> ")
    ''' if yes asking them to enter the unavailable lot in a specific format'''

    if car_park_un.lstrip().upper() == "YES":

        print("Enter unavailable lots in the format: floor number,column number,row number: ")
        print("Example: '1,1,1' ")

        print("Please avoid any spaces and enter the commas too")
        un_lot = input(">>> ")
        pl_for_cars = AF.unavailable_lots_for_cars(un_lot, pl_for_cars, floors_for_cars, columns_for_cars, rows_for_cars)
    elif car_park_un.lstrip().upper() == "NO":
        break
    else:
        print()
        print()
        print("-----*****INVALID INPUT*****------")
        pass

    '''again confirming if there are any other unavailable lots'''

    print()
    print()
    print()

    if car_park_un.lstrip().upper() == "NO":
        break

print()
print()
print()


print()
print()
print()
''' confirming if there are any unavailable lot due to any technical issues '''

while True:
    print("Are any lots NOT available in the BIKE PARKING LOT ?")
    print("Enter YES/NO ")
    bike_park_un = input(">>> ")

    ''' if yes asking them to enter the unavailable lot in a specific format'''

    if bike_park_un.lstrip().upper() == "YES":

        print("Enter unavailable lots in the format: floor number,column number,row number: ")
        print("Example: '1,1,1' ")

        print("Please avoid any spaces and enter the commas too")
        un_lot = input(">>> ")
        pl_for_bikes = AF.unavailable_lots_for_bikes(un_lot, pl_for_bikes, floors_for_bikes, columns_for_bikes, rows_for_bikes)
    elif bike_park_un.lstrip().upper() == "NO":
        break
    else:
        print()
        print()
        print("-----*****INVALID INPUT*****------")
        pass

    '''again confirming if there are any other unavailable lots'''

    print()
    print()
    print()

    if bike_park_un.lstrip().upper() == "NO":
        break

print()
print()
print()


'''print(pl_for_cars)
print(pl_for_bikes)'''

while True:

    '''if manager enters something wrong he can type "x" to come BACK to the beginning'''
    print()
    print()
    print()
    print("***ENTERING INPUT 'x' (small alphabet x) at anytime will redirect you here***")
    for i in range(0, 30000000):
        if i % 10000000 == 0:
            print("🙂", end=" ")
    print()
    print()
    print("Enter Vehicle Type, that is, CAR/ BIKE")

    ''' taking type of vehicle as input '''
    print()
    vt = input(">>> ")

    print()
    print()
    print()
    if vt == "x":
        pass
    else:

        if AF.is_car_or_bike(vt.lstrip()):
            vehicle_type = "CAR"
        else:
            vehicle_type = "BIKE"

        if vehicle_type == "CAR":
            print("Are you parking the car IN or moving OUT?")

            print("Enter IN/  OUT")
            print()

            '''taking going in or coming out as input'''

            in_or_out = input(">>> ")

            print()
            print()
            print()

            if in_or_out.lstrip() == "x":
                pass
            else:
                if AF.is_in_or_out(in_or_out):
                    print("WELCOME to RUNTIME PARKING! ")
                    for i in range(0, 30000000):
                        if i % 10000000 == 0:
                            print("🙂", end=" ")
                    print()
                    print()
                    print("ENTER CAR NUMBER: ")
                    print("EXAMPLE => 'MH 15 CC 7459'")

                    print()
                    print("Please enter spaces as shown in above example")

                    '''writing down the Licence plate from the vehicle'''

                    car_number = input(">>> ")

                    print()
                    print()
                    print()
                    if car_number.lstrip() == "x":
                        pass
                    else:

                        while True:

                            if car_number.lstrip() == "x":
                                break

                            flag_valid = 0
                            flag_dup = 0
                            print("Checking the validity of your car number", end=" ")
                            for i in range(0, 40000000):
                                if i % 10000000 == 0:
                                    print(".", end=" ")
                            print()
                            print()
                            print()
                            print()

                            '''checking if the entered car number is valid or not'''

                            if AF.validity_of_licence(car_number):
                                flag_valid = 1

                            else:
                                print("-----***** INVALID VEHICLE NUMBER *****-----")
                                print()
                                print()
                                print()

                            '''checking if there is a vehicle with same licence plate parked inside, if there is a duplicate number plate we will call police'''

                            if AF.found_duplicate(car_number, floors_for_bikes, columns_for_bikes, rows_for_bikes,
                                                  floors_for_cars, columns_for_cars, rows_for_cars, pl_for_cars,
                                                  pl_for_bikes):
                                print("-----***** DUPLICATE CAR NUMBER *****-----")
                                print("🚨🚨🚨 DIALING 911 🚨🚨🚨 ")
                                for i in range(150000000):
                                    pass
                                print()
                                print()
                                print()
                                # negative for
                                flag_dup = 1

                            else:
                                flag_dup = 0

                            if flag_dup == 0 and flag_valid == 1:
                                print("VALID car number")
                                break
                            else:

                                '''if entered car number is not valid we ask to re enter'''

                                print("RE-ENTER CAR NUMBER: ")
                                car_number = input(">>> ")
                                print()
                                print()

                        if car_number.lstrip() == "x":
                            pass
                        else:
                            print("SEARCHING for BEST (most comfortable) PLACE TO PARK ", end=" ")
                            for i in range(0, 40000000):
                                if i % 10000000 == 0:
                                    print(".", end=" ")
                            print()
                            print()
                            '''searches a parking lot for comfortable parking, i.e, no cars around you 
                            if possible so you can easily park as well as open doors without hitting other cars'''

                            pl_for_cars = AF.car_park(car_number, floors_for_cars, columns_for_cars, rows_for_cars,
                                                      pl_for_cars)
                            '''for i in range(0, floors_for_cars):
                                print(pl_for_cars[i])'''

                else:

                    '''if the vehicle is going out'''

                    print("EXITING PARKING LOT", end="")
                    for i in range(0, 40000000):
                        if i % 10000000 == 0:
                            print(".", end=" ")
                    print()
                    print()
                    print()
                    print("ENTER CAR NUMBER: ")
                    print(" EXAMPLE => 'MH 15 CC 7459'")
                    print("Please enter spaces as shown in above example, enter 'x' in case you did not want to exit")
                    car_number = input(">>> ")
                    print()
                    print()
                    print()
                    if car_number.lstrip() == "x":
                        pass
                    else:
                        while True:
                            flag_dup1 = 0
                            flag_valid1 = 0
                            print("Checking the validity of your car number", end="")
                            for i in range(0, 40000000):
                                if i % 10000000 == 0:
                                    print(".", end=" ")
                            print()
                            print()
                            print()
                            '''checking if the entered car number is valid or not'''

                            if AF.validity_of_licence(car_number):
                                flag_valid1 = 1
                            else:
                                print("-----*****INVALID VEHICLE NUMBER*****-----")
                                print()
                                print()
                                print()

                            '''entering the car number again to verify if it is parked in our parking'''

                            if AF.found_duplicate_car(car_number, floors_for_bikes, columns_for_bikes, rows_for_bikes,
                                                      floors_for_cars, columns_for_cars, rows_for_cars, pl_for_cars,
                                                      pl_for_bikes):
                                flag_dup1 = 1
                            else:
                                print("CAR NOT FOUND IN THE PARKING")
                                print()
                                print()

                            if flag_dup1 == 1 and flag_valid1 == 1:
                                print("VALID car number")
                                print()
                                print()
                                break
                            else:
                                print("RE-ENTER CAR NUMBER: ")
                                car_number = input(">>> ")
                                print()
                                print()
                                print()
                                if car_number.lstrip() == "x":
                                    break

                        if car_number.lstrip() == "x":
                            pass
                        else:

                            '''generating the file log and removing the car'''

                            pl_for_cars = AF.car_remove(car_number, floors_for_cars, columns_for_cars, rows_for_cars, pl_for_cars)
                            print("THANK YOU FOR CHOOSING RUNTIME PARKING !")
                            for i in range(0, 120000000):
                                if i % 10000000 == 0:
                                    visit_again = "VISIT AGAIN!"
                                    print(visit_again[int(i / 10000000)], end="")
                            print()

                            print("------------------------------------------------------------")
                            print()
                            print()
                            print()

                            '''for i in range(0, floors_for_cars):
                                print(pl_for_cars[i])'''

        elif vehicle_type == "BIKE":
            print("Are you parking the bike IN or moving OUT?")
            print("Enter IN/  OUT")
            print()

            '''taking going in or coming out as input'''

            in_or_out = input(">>> ")

            print()
            print()
            print()

            if in_or_out.lstrip() == "x":
                pass
            else:
                if AF.is_in_or_out(in_or_out):
                    print("WELCOME to RUNTIME PARKING! ")
                    for i in range(0, 30000000):
                        if i % 10000000 == 0:
                            print("🙂", end=" ")
                    print()
                    print()
                    print("ENTER BIKE NUMBER: ")
                    print("EXAMPLE => 'MH 15 CC 7459'")

                    print()
                    print("Please enter spaces as shown in above example")

                    '''writing down the Licence plate from the vehicle'''

                    bike_number = input(">>> ")

                    print()
                    print()
                    print()
                    if bike_number.lstrip() == "x":
                        pass
                    else:

                        while True:

                            if bike_number.lstrip() == "x":
                                break

                            flag_valid = 0
                            flag_dup = 0
                            print("Checking the validity of your bike number", end=" ")
                            for i in range(0, 40000000):
                                if i % 10000000 == 0:
                                    print(".", end=" ")
                            print()
                            print()
                            print()
                            print()

                            '''checking if the entered bike number is valid or not'''

                            if AF.validity_of_licence(bike_number):
                                flag_valid = 1

                            else:
                                print("-----***** INVALID VEHICLE NUMBER *****-----")
                                print()
                                print()
                                print()

                            '''checking if there is a vehicle with same licence plate parked inside, if there is a duplicate number plate we will call police'''

                            if AF.found_duplicate(bike_number, floors_for_bikes, columns_for_bikes, rows_for_bikes,
                                                  floors_for_cars, columns_for_cars, rows_for_cars, pl_for_cars,
                                                  pl_for_bikes):
                                print("-----***** DUPLICATE BIKE NUMBER *****-----")
                                print("🚨🚨🚨 DIALING 911 🚨🚨🚨 ")
                                for i in range(150000000):
                                    pass
                                print()
                                print()
                                print()

                                flag_dup = 1

                            else:
                                flag_dup = 0

                            if flag_dup == 0 and flag_valid == 1:
                                print("VALID bike number")
                                break
                            else:

                                '''if entered bike number is not valid we ask to re enter'''

                                print("RE-ENTER BIKE NUMBER: ")
                                bike_number = input(">>> ")
                                print()
                                print()

                        if bike_number.lstrip() == "x":
                            pass
                        else:
                            print("SEARCHING for BEST (most comfortable) PLACE TO PARK ", end=" ")
                            for i in range(0, 40000000):
                                if i % 10000000 == 0:
                                    print(".", end=" ")
                            print()
                            print()

                            '''searches a parking lot for comfortable parking, i.e, no bikes around you if possible'''
                            pl_for_bikes = AF.bike_park(bike_number, floors_for_bikes, columns_for_bikes,
                                                        rows_for_bikes, pl_for_bikes)
                            '''for i in range(0, floors_for_bikes):
                                print(pl_for_bikes[i])'''

                else:

                    '''if the vehicle is going out'''
                    print("EXITING PARKING LOT", end="")
                    for i in range(0, 40000000):
                        if i % 10000000 == 0:
                            print(".", end=" ")

                    print()
                    print()
                    print()
                    print("ENTER BIKE NUMBER: ")
                    print(" EXAMPLE => 'MH 15 CC 7459'")
                    print("Please enter spaces as shown in above example, enter 'x' in case you did not want to exit")
                    bike_number = input(">>> ")
                    print()
                    print()
                    print()

                    if bike_number.lstrip() == "x":
                        pass

                    else:
                        while True:

                            flag_dup1 = 0
                            flag_valid1 = 0
                            print("Checking the validity of your bike number", end="")
                            for i in range(0, 40000000):

                                if i % 10000000 == 0:
                                    print(".", end=" ")
                            print()
                            print()
                            print()

                            '''checking if the entered bike number is valid or not'''

                            if AF.validity_of_licence(bike_number):
                                flag_valid1 = 1
                            else:
                                print("-----*****INVALID VEHICLE NUMBER*****-----")
                                print()
                                print()
                                print()

                            '''entering the bike number again to verify if it is parked in our parking'''

                            if AF.found_duplicate_bike(bike_number, floors_for_bikes, columns_for_bikes, rows_for_bikes,
                                                       floors_for_cars, columns_for_cars, rows_for_cars, pl_for_cars,
                                                       pl_for_bikes):
                                flag_dup1 = 1
                            else:
                                print("BIKE NOT FOUND IN THE PARKING")
                                print()
                                print()

                            if flag_dup1 == 1 and flag_valid1 == 1:

                                print("VALID bike number")
                                print()
                                print()
                                break
                            else:
                                print("RE-ENTER BIKE NUMBER: ")
                                bike_number = input(">>> ")
                                print()
                                print()
                                print()

                                if bike_number.lstrip() == "x":
                                    break

                        if bike_number.lstrip() == "x":

                            pass

                        else:

                            '''generating the file log and removing the car'''

                            pl_for_bikes = AF.bike_remove(bike_number, floors_for_bikes, columns_for_bikes,
                                                          rows_for_bikes, pl_for_bikes)

                            print("THANK YOU FOR CHOOSING RUNTIME PARKING !")

                            for i in range(0, 120000000):

                                if i % 10000000 == 0:
                                    visit_again = "VISIT AGAIN!"

                                    print(visit_again[int(i / 10000000)], end="")

                            print()
                            print("------------------------------------------------------------")
                            print()
                            print()
                            print()

                            '''for i in range(0, floors_for_bikes):
                                print(pl_for_bikes[i])'''

