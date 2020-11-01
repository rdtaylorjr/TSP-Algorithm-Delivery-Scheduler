# Name: Russell Taylor  Student ID: 001441098

from sys import maxsize


# A class that controls the delivery of packages using a nearest neighbor algorithm to select the order of deliveries
class Delivery:

    # Initializes the Delivery class
    def __init__(self, display):
        self._display = display
        self._truck = None
        self._current = None
        self._distance = None

    # Calls the individual methods that make up the algorithm. Loops get_location and make_deliveries until all packages are delivered or the end time is reached
    def deliver_packages(self, data, time, truck):
        if self.__end(time):
            return

        self.__load_truck(data, time, truck)

        while len(truck.get_packages()) > 0:
            self.__get_location(data, time)
            if self.__end(time):
                return

            self.__make_deliveries(data, time)
            if self.__end(time):
                return

        self.__return_to_start(data, time)

    # Loads packages onto the truck. Sets the status of packages as 'On Truck' and displays the Truck number, Trip number, and starting location
    def __load_truck(self, data, time, truck):
        self._truck = truck
        self._current = data.get_locations().lookup(0)

        for i in self._truck.get_packages():
            p = data.get_packages().lookup(i)
            p.set_status('On Truck ' + str(self._truck.get_truck()))

        if self._display is True:
            print('------ Deliveries: Truck', str(self._truck.get_truck()) + ', Trip', str(self._truck.get_trip()), '------\n')
            print('Start at', self._current.get_address(), '\n')

        self.__alert(data, time, 'load')

    # Determines the next delivery location. Finds the nearest delivery location and sets it as current, then updates the total mileage and time
    def __get_location(self, data, time):
        self._distance = maxsize
        next_location = 0

        for i in range(len(self._current.get_distances())):
            for p in self._truck.get_packages():
                if i == data.get_packages().lookup(p).get_location() and self._distance > self._current.get_distances()[i]:
                    self._distance = self._current.get_distances()[i]
                    next_location = i

        self._current = data.get_locations().lookup(next_location)

        self._truck.set_miles(self._truck.get_miles() + self._distance)
        time.current += time.to_time(self._distance)

    # Delivers packages at the current location. Sets the status of packages as delivered and displays the package number, address, time, and total truck mileage. Removes delivered packages from the truck
    def __make_deliveries(self, data, time):
        self.__alert(data, time, 'update')

        if self._display is True:
            print('Travel', self._distance, 'miles to', self._current.get_address())

        delivered = [p for p in self._truck.get_packages() if data.get_packages().lookup(p).get_location() == self._current.get_id()]
        for p in delivered:
            if self.__alert(data, time, 'address', p) is False:
                data.get_packages().lookup(p).set_status('Delivered at ' + time.display())
                if self._display is True:
                    print('Package', p, 'has been delivered at', self._current.get_address())

        if self._display is True:
            print('Time:', time.display() + ', Total distance: %.1f miles' % self._truck.get_miles(), '\n')

        self._truck.set_packages([p for p in self._truck.get_packages() if p not in delivered])

    # Returns the truck to the WGU warehouse after all packages have been delivered. Updates the time and truck mileage with the distance to WGU and displays the distance, address, time, and total miles
    def __return_to_start(self, data, time):
        self.__alert(data, time, 'delivery')

        self._distance = self._current.get_distances()[0]
        self._current = data.get_locations().lookup(0)

        if self._display is True:
            print('Travel', self._distance, 'miles to', self._current.get_address())

        self._truck.set_miles(self._truck.get_miles() + self._distance)
        time.current += time.to_time(self._distance)

        if self._display is True:
            print('Time:', time.display() + ', Total distance: %.1f miles' % self._truck.get_miles(), '\n')

    # Displays alerts and performs certain actions when an alert is present. Checks for the alert type and carries out instructions in the alert data file
    def __alert(self, data, time, event, p=None):
        for i in range(data.get_number_of_alerts()):
            a = data.get_alerts().lookup(i)

            if event == 'address':
                if a.get_package() == p and self._truck.get_id() == a.get_route():
                    data.get_packages().lookup(p).set_status(a.get_status())
                    if self._display is True:
                        print('*** Alert ***', a.get_alert())
                    return True

            elif event == a.get_type() == 'update':
                if self._truck.get_id() == a.get_route() and time.current >= time.to_time(hours=a.get_hour(), minutes=a.get_minute()):
                    data.get_packages().lookup(a.get_package()).set_location(a.get_location())
                    data.get_packages().lookup(a.get_package()).set_address(a.get_address())
                    data.get_packages().lookup(a.get_package()).set_city(a.get_city())
                    data.get_packages().lookup(a.get_package()).set_zip(a.get_zip())
                    data.get_packages().lookup(a.get_package()).set_status(a.get_status())
                    if self._display is True:
                        print('*** Alert ***', a.get_alert(), 'at', time.display(), '\n')
                    a.set_route(0)

            elif event == a.get_type() and self._truck.get_id() == a.get_route():
                if self._display is True:
                    print('*** Alert ***', a.get_alert(), 'at', time.display(), '\n')

        return False

    # Stops the simulation when the end time is reached
    def __end(self, time):
        if time.current >= time.end:
            time.current = time.end
            return True
        return False

