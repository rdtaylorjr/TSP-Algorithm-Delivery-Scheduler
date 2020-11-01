# Name: Russell Taylor  Student ID: 001441098

# A data structure class that stores and retrieves data in a hash table
class HashTable:

    # Initializes the HashTable class
    def __init__(self, size=101):
        self._table = [None] * size
        self._size = size

    # Inserts a key, value pair to the hash table. Uses separate chaining to resolve collisions
    def insert(self, key, value):
        index = self.__hash(key)
        key_value_pair = [key, value]

        # If no bucket is present at the table index, create a bucket and place the key/value pair in it
        if self._table[index] is None:
            self._table[index] = list([key_value_pair])
            return

        # Iterate through the bucket to find the key. If the key is present, update the value
        for pair in self._table[index]:
            if pair[0] == key:
                pair[1] = value
                return

        # If the key is not present in the bucket, add the key/value pair to the bucket
        self._table[index].append(key_value_pair)

    # Looks up the value associated with a given key from the hash table
    def lookup(self, key):
        index = self.__hash(key)

        # If no bucket is present at the table index, return None
        if self._table[index] is None:
            return None

        # Iterate through the bucket to find the key. If the key is present, return the value
        for pair in self._table[index]:
            if pair[0] == key:
                return pair[1]

        # If the key is not present in the bucket, return None
        return None

    # Hashes the key and returns an index in the hash table
    def __hash(self, key):
        hash = 0
        for char in str(key):
            hash += ord(char)
        return hash % self._size
