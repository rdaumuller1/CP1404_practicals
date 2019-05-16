
from prac_06.car import Car
from prac_08.taxi import Taxi
from prac_08.silver_taxi import SilverTaxi

MENU = "q)uit, c)hoose taxi, d)rive"


def main():

    total_bill = 0
    taxis = [Taxi("Prius", 100), SilverTaxi("Limo", 100, 2),
             SilverTaxi("Hummer", 200, 4)]

    print("Let's drive!")
    print(MENU)
    choice = input(">>> ").lower()
    while choice != "q":
        if choice == "c":
            print("Taxis available: ")
            display_taxis(taxis)
            taxi_choice = int(input("Choose taxi: "))
            chosen_taxi = taxis[taxi_choice]
        elif choice == "d":
            chosen_taxi.start_fare()
            distance_to_drive = float(input("Drive how far? "))
            chosen_taxi.drive(distance_to_drive)
            trip_cost = chosen_taxi.get_fare()
            print("Your {} trip cost you ${}".format(chosen_taxi.name, trip_cost))
            total_bill += trip_cost
        else:
            print("Invalid option")
        print("Bill to date: ${}".format(total_bill))
        print(MENU)
        choice = input(">>> ").lower()

    print("Total trip cost: ${}".format(total_bill))
    print("Taxis are now:")
    display_taxis(taxis)


def display_taxis(taxis):
    for i, taxi in enumerate(taxis):
        print("{} - {}".format(i, str(taxi)))


main()
