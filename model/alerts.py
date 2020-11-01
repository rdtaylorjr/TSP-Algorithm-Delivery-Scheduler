# Name: Russell Taylor  Student ID: 001441098

# A class of Alert objects that represent delivery, package, and address alerts
class Alert:

    # Initializes the Alert class
    def __init__(self, id=0, route=0, type='', alert='', package=0, status='', location=0, address='', city='', zip='', hour=0, minute=0):
        self._id = id
        self._route = route
        self._type = type
        self._alert = alert
        self._package = package
        self._status = status
        self._location = location
        self._address = address
        self._city = city
        self._zip = zip
        self._hour = hour
        self._minute = minute

    # Gets the alert ID
    def get_id(self):
        return self._id

    # Gets the route ID
    def get_route(self):
        return self._route

    # Sets the route ID
    def set_route(self, route):
        self._route = route

    # Gets the alert type
    def get_type(self):
        return self._type

    # Gets the alert message to display
    def get_alert(self):
        return self._alert

    # Gets the package ID for address and update alerts
    def get_package(self):
        return self._package

    # Gets the new package status for address and update alerts
    def get_status(self):
        return self._status

    # Gets the new delivery location for update alerts
    def get_location(self):
        return self._location

    # Gets the new delivery address for update alerts
    def get_address(self):
        return self._address

    # Gets the new delivery city for update alerts
    def get_city(self):
        return self._city

    # Gets the new delivery zip code for update alerts
    def get_zip(self):
        return self._zip

    # Gets the update time hour for update alerts
    def get_hour(self):
        return self._hour

    # Gets the update time minutes for update alerts
    def get_minute(self):
        return self._minute
