
from prac_08.silver_taxi import SilverTaxi


def main():
    taxi = SilverTaxi("Silver Taxi", 100, 2)
    taxi.drive(18)
    print(taxi)
    print("Fare is ${}".format(taxi.get_fare()))


main()
