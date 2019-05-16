
from prac_08.unreliable_car import UnreliableCar


def main():
    reliable_car = UnreliableCar("Reliable", 100, 90)
    unreliable_car = UnreliableCar("Unreliable", 100, 9)
    for i in range(1, 12):
        print("Attempting to drive {}km:".format(i))
        print("{:12} drove {:2}km".format(reliable_car.name, reliable_car.drive(i)))
        print("{:12} drove {:2}km".format(unreliable_car.name, unreliable_car.drive(i)))
    print(reliable_car)
    print(unreliable_car)


main()
