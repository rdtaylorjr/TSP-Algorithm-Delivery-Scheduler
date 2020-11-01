# Name: Russell Taylor  Student ID: 001441098

from access.deliveries import Delivery
from utils.data import Data
from utils.time import Time


# A class that controls the user interface of the program
class Interface:

    # Initializes the Interface class
    def __init__(self):
        self.data = Data()
        self.time = Time()
        self.again = True

    # Displays main menu options to the user
    def show_options(self):
        while self.again is True:
            print('---------- Package Delivery System ----------')
            print('1. Delivery Simulation')
            print('2. Package Status Reports')
            print('3. Look Up Package')
            print('4. Quit')
            self.__get_choice()

    # Prompts the user to choose an option, calls the appropriate function if the user inputs a valid choice, recursively calls itself if the user inputs an invalid choice
    def __get_choice(self):
        self.data = Data()
        self.time = Time()

        choice = input('Choose an option: ')
        if choice == '1':
            self.__run_simulation(True)
        elif choice == '2':
            self.__status_report()
        elif choice == '3':
            self.__lookup_package()
        elif choice == '4':
            self.__quit()
        else:
            print('Please try again')
            self.__get_choice()

    # Runs the package delivery simulation. Calls the deliver_packages method for each route, and tracks the total mileage for all routes
    def __run_simulation(self, display):
        if display is True:
            print('\n---------- Delivery Simulation ----------\n')

        delivery = Delivery(display)

        # Truck 1, Routes 1 & 2
        if self.time.current < self.time.end:
            truck1 = self.data.get_routes().lookup(1)
            delivery.deliver_packages(self.data, self.time, truck1)
            total_miles = truck1.get_miles()

        if self.time.current < self.time.end:
            truck1 = self.data.get_routes().lookup(2)
            delivery.deliver_packages(self.data, self.time, truck1)
            total_miles += truck1.get_miles()

        self.time.reset()

        # Truck 2, Routes 1 & 2
        if self.time.current < self.time.end:
            truck2 = self.data.get_routes().lookup(3)
            delivery.deliver_packages(self.data, self.time, truck2)
            total_miles += truck2.get_miles()

        if self.time.current < self.time.end:
            truck2 = self.data.get_routes().lookup(4)
            delivery.deliver_packages(self.data, self.time, truck2)
            total_miles += truck2.get_miles()

        if display is True:
            print('Total Mileage: %.1f miles\n' % total_miles)

    # Generates and displays package status reports. Prompts the user to input a time, runs the simulation up to that time, then displays the status of all packages at that time
    def __status_report(self):
        print('\n----------- Package Status Reports -----------')

        for i in range(1, self.data.get_number_of_packages() + 1):
            self.data.get_packages().lookup(i).set_status('At Warehouse')

        hours = self.__input('Enter hour (0-23): ', 0, 24)
        minutes = self.__input('Enter minutes (0-59): ', 0, 60)
        time = self.time.to_time(hours=hours, minutes=minutes, seconds=0)

        self.time.end = time
        self.__run_simulation(False)
        self.time.current = time

        print('\nCurrent Time:', self.time.display(), '\n')
        for i in range(1, self.data.get_number_of_packages() + 1):
            p = self.data.get_packages().lookup(i)
            print('Package ID:', p.get_id(), '| Address:', p.get_address(), '| Deadline:', p.get_deadline(), '| City: ', p.get_city(), '| Zip Code:', p.get_zip(), '| Weight:', p.get_weight(), '| Status:', p.get_status())
        print()

    # Looks up package information. Prompts the user to input a package ID and time, runs the simulation up to that time, then displays all information about the given package at that time
    def __lookup_package(self):
        print('\n-------------- Look Up Package --------------')

        i = self.__input('Enter a Package ID (1-40): ', 1, 41)
        p = self.data.get_packages().lookup(i)
        self.data.get_packages().lookup(i).set_status('At Warehouse')

        hours = self.__input('Enter hour (0-23): ', 0, 24)
        minutes = self.__input('Enter minutes (0-59): ', 0, 60)
        time = self.time.to_time(hours=hours, minutes=minutes, seconds=0)

        self.time.end = time
        self.__run_simulation(False)
        self.time.current = time

        print('\nPackage ID:', p.get_id())
        print('Address:', p.get_address())
        print('Deadline:', p.get_deadline())
        print('City:', p.get_city())
        print('Zip Code:', p.get_zip())
        print('Weight:', p.get_weight())
        print('Status at', self.time.display() + ':', p.get_status(), '\n')

    # Prompts the user for input then validates the input for data type and values. Recursely calls itself if the user input is invalid
    def __input(self, string, low, high):
        i = input(string)
        if i in [str(i) for i in range(low, high)] or i in ['0' + str(i) for i in range(low, high)]:
            return int(i)
        else:
            print('Please try again')
            return self.__input(string, low, high)

    # Stops the program by ending the main menu loop
    def __quit(self):
        self.again = False
