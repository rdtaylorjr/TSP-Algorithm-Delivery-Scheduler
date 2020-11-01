# Name: Russell Taylor  Student ID: 001441098

# A class of Route objects that represent routes taken by the trucks
class Route:

    # Initializes the Route class
    def __init__(self, id=0, truck=0, trip=0, miles=0.0, packages=None):
        self._id = id
        self._truck = truck
        self._trip = trip
        self._miles = miles
        self._packages = packages

    # Gets the route ID
    def get_id(self):
        return self._id

    # Sets the route ID
    def set_id(self, id):
        self._id = id

    # Gets the truck number
    def get_truck(self):
        return self._truck

    # Sets the truck number
    def set_truck(self, truck):
        self._truck = truck

    # Gets the trip number for the truck
    def get_trip(self):
        return self._trip

    # Sets the trip number for the truck
    def set_trip(self, trip):
        self._trip = trip

    # Gets the number of miles traveled by the truck
    def get_miles(self):
        return self._miles

    # Sets the number of miles traveled by the truck
    def set_miles(self, miles):
        self._miles = miles

    # Gets the list of package IDs for packages on the truck
    def get_packages(self):
        return self._packages

    # Sets the list of package IDs for packages on the truck
    def set_packages(self, packages):
        self._packages = packages
