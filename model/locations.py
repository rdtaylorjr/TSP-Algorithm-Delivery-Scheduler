# Name: Russell Taylor  Student ID: 001441098

# A class of Location objects that represent delivery locations
class Location:

    # Initializes the Location class
    def __init__(self, id=0, address='', distances=None):
        self._id = id
        self._address = address
        self._distances = distances

    # Gets the location ID
    def get_id(self):
        return self._id

    # Gets the location address
    def get_address(self):
        return self._address

    # Gets an adjacency list of distances between the location and each other location
    def get_distances(self):
        return self._distances
