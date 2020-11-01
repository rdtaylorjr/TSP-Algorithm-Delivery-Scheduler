# Name: Russell Taylor  Student ID: 001441098

import csv
from model.alerts import Alert
from model.locations import Location
from model.packages import Package
from model.routes import Route
from utils.hashtable import HashTable


# A utility class that handles importing data and making it available to the program
class Data:

    # Initializes the Data class, calls the 'read' methods
    def __init__(self):
        self._locations = HashTable()
        self._packages = HashTable()
        self._routes = HashTable()
        self._alerts = HashTable()

        self._number_of_locations = 0
        self._number_of_packages = 0
        self._number_of_alerts = 0

        self.__read_locations()
        self.__read_packages()
        self.__read_routes()
        self.__read_alerts()

    # Creates a Location object for each location in the imported csv file, then stores the Location objects in a hash table. Each Location object includes an adjacency list containing distances to each other location
    def __read_locations(self):
        with open('data/locations.csv') as locations_csv:
            read_data = csv.reader(locations_csv, delimiter='\t')

            for row in read_data:
                id = int(row[0])
                address = row[1]
                distances = [float(row[col]) for col in range(2, 29)]

                location = Location(id=id, address=address, distances=distances)
                self._locations.insert(int(id), location)
                self._number_of_locations += 1

            # print('Locations')
            # for i in range(0, self.number_of_locations):
            #     l = self.locations.get(i)
            #     print(l.get_id(), l.get_address(), end=' ')
            #     for d in l.get_distances():
            #         print(d, end=' ')
            #     print()

    # Gets the hash table of Location objects
    def get_locations(self):
        return self._locations

    # Gets the number of Location objects
    def get_number_of_locations(self):
        return self._number_of_locations

    # Creates a Package object for each package in the imported csv file, then stores the Package objects in a hash table
    def __read_packages(self):
        with open('data/packages.csv') as packages_csv:
            read_data = csv.reader(packages_csv, delimiter='\t')

            for row in read_data:
                id = int(row[0])
                location = 0
                address = row[1]
                deadline = row[5]
                city = row[2] + ', ' + row[3]
                zip = row[4]
                weight = row[6]

                for i in range(0, self._number_of_locations):
                    loc = self._locations.lookup(i)
                    if address + ', ' + city + ' ' + zip == loc.get_address():
                        location = loc.get_id()
                        break

                package = Package(id=id, location=location, address=address, deadline=deadline, city=city, zip=zip, weight=weight)
                self._packages.insert(int(id), package)
                self._number_of_packages += 1

            # print('Packages')
            # for i in range(1, self.number_of_packages + 1):
            #     p = self.packages.get(i)
            #     print(p.get_id(), p.get_location(), p.get_address())

    # Gets the hash table of Package objects
    def get_packages(self):
        return self._packages

    # Gets the number of Package objects
    def get_number_of_packages(self):
        return self._number_of_packages

    # Creates a Route object for each route in the imported csv file, then stores the Route objects in a hash table
    def __read_routes(self):
        with open('data/routes.csv') as routes_csv:
            read_data = csv.reader(routes_csv, delimiter='\t')

            for row in read_data:
                id = int(row[0])
                truck = row[1]
                trip = row[2]
                packages = [int(x) for x in row[3].split(',')]

                route = Route(id=id, truck=truck, trip=trip, packages=packages)
                self._routes.insert(int(id), route)

            # print('Routes')
            # for i in range(1, 5):
            #     r = self._routes.get(i)
            #     print(r.get_id(), r.get_truck(), r.get_trip(), r.get_packages())

    # Gets the hash table of Route objects
    def get_routes(self):
        return self._routes

    # Creates an Alert object for each alert in the imported csv file, then stores the Alert objects in a hash table
    def __read_alerts(self):
        with open('data/alerts.csv') as alerts_csv:
            read_data = csv.reader(alerts_csv, delimiter='\t')

            for row in read_data:
                id = int(row[0])
                route = int(row[1])
                type = row[2]
                alert = row[3]
                package = 0
                status = ''
                location = 0
                address = ''
                city = ''
                zip = ''
                hour = 0
                minute = 0

                if type == 'address' or type == 'update':
                    package = int(row[4])
                    status = row[5]

                if type == 'update':
                    location = int(row[6])
                    address = row[7]
                    city = row[8]
                    zip = row[9]
                    hour = int(row[10])
                    minute = int(row[11])

                a = Alert(id=id, route=route, type=type, alert=alert, package=package, status=status, location=location, address=address, city=city, zip=zip, hour=hour, minute=minute)
                self._alerts.insert(int(id), a)
                self._number_of_alerts += 1

            # print('Alerts')
            # for i in range(self._number_of_alerts):
            #     a = self._alerts.get(i)
            #     print(a.get_id(), a.get_type(), a.get_alert(), a.get_package(), a.get_status(), a.get_location())

    # Gets the hash table of Alert objects
    def get_alerts(self):
        return self._alerts

    # Gets the number of Alert objects
    def get_number_of_alerts(self):
        return self._number_of_alerts
