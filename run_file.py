from flight_trip import *
from passenger import *
import sys
from staff import *

# new_flight = Flight_trip(destination='rome', duration='1:00', origin='geneva', passenger_list=['Monica', 'Leo'])

# print(new_flight.destination, new_flight.duration, new_flight.origin, new_flight.passenger_list)


destination1 = Flight_trip(destination='rome', duration='1:00', origin='geneva')
passengers1 = Passengers(name='', passport_number='')

# Adding the passengers and appending the list using a dictionary

while destination1.add_passenger != 'exit':

    destination1.add_passenger(new_passenger=input('please enter the passenger name '))
    passengers1.set_passport_number(new_passport_number=input('please enter passport number '))
    (destination1.get_passenger())
    (passengers1.get_passport_number())

    dictionary = dict(zip(destination1.passenger_list, passengers1.passport_list))
    print(dictionary)



    # add passenger as an object
    # new_flight.add_passenger_list(new_passenger)
    # print(new_passenger)

    # add a passenger to the new_flight
    user_input = input('add passenger to flight: ')
    new_flight.add_passenger_list(user_input)
    print(new_flight.destination, new_flight.duration, new_flight.origin, new_flight.passenger_list)

    # add a second passenger to the new_flight
    user_input2 = input('add passenger to flight: ')
    new_flight.add_passenger_list(user_input2)
    print(new_flight.passenger_list)


    # add a passport number to the new_flight
    flight_passport = input('add passport number to flight: ')
    new_flight.add_passport_list(flight_passport)
    print(new_flight.passport_list)

    # add a second passport number to new_flight
    flight_passport2 = input('add passport number to flight: ')
    new_flight.add_passport_list(flight_passport2)
    print(new_flight.passport_list)


    # get the list of passengers
    print(new_flight.get_list_of_passengers())

    # get list of passengers and passport numbers for flight
    print(new_flight.passenger_list, new_flight.passport_list)

    # create a dictionary
    dictionary = dict(zip(new_flight.passenger_list, new_flight.passport_list))
    print(dictionary)

    # change plane to flight_trip
    for flight in flight_trip:
        new_flight
# for passenger in new_flight.passenger_list:
#     print(passenger.get_name())