from passenger import *
from flight_trip import *
from test_run_file import *

seats = destination1
number_of_seats = ('20')
new_seats = 0


def add_seats():
    destination1.add_passenger(new_passenger=input('please enter the passenger name '))
    while destination1.add_passenger() == 'exit':
        break
    for item in destination1.add_passenger() > 1:
        if new_seats.count:
            new_seats.append(item)
        return number_of_seats


print(add_seats())
