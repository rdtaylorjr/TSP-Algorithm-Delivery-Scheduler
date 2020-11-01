# Name: Russell Taylor  Student ID: 001441098

# A class of Package objects that represent packages
class Package:

    # Initializes the Package class
    def __init__(self, id=0, location=0, address='', deadline='', city='', zip='', weight='', status='At Warehouse'):
        self._id = id
        self._location = location
        self._address = address
        self._deadline = deadline
        self._city = city
        self._zip = zip
        self._weight = weight
        self._status = status

    # Gets the package ID
    def get_id(self):
        return self._id

    # Sets the package ID
    def set_id(self, id):
        self._id = id

    # Sets the delivery location ID
    def get_location(self):
        return self._location

    # Sets the delivery location ID
    def set_location(self, location):
        self._location = location

    # Gets the delivery address
    def get_address(self):
        return self._address

    # Sets the delivery address
    def set_address(self, address):
        self._address = address

    # Gets the delivery deadline
    def get_deadline(self):
        return self._deadline

    # Sets the delivery deadline
    def set_deadline(self, deadline):
        self._deadline = deadline

    # Gets the delivery city
    def get_city(self):
        return self._city

    # Sets the delivery city
    def set_city(self, city):
        self._city = city

    # Gets the delivery zip code
    def get_zip(self):
        return self._zip

    # Sets the delivery zip code
    def set_zip(self, zip):
        self._zip = zip

    # Gets the package weight
    def get_weight(self):
        return self._weight

    # Sets the package weight
    def set_weight(self, weight):
        self._weight = weight

    # Gets the delivery status
    def get_status(self):
        return self._status

    # Sets the delivery status
    def set_status(self, status):
        self._status = status
