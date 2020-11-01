# Name: Russell Taylor  Student ID: 001441098

from datetime import timedelta


# A utility class that handles time tracking, conversions, and display
class Time:

    # Initializes the Time class
    def __init__(self, current=timedelta(hours=8), end=timedelta(hours=24)):
        self.current = current
        self.end = end

    # Converts an integer representing miles to a timedelta, assuming an average speed of 18mph
    # Converts integers representing hours, minutes, and seconds to a timedelta
    @staticmethod
    def to_time(miles=1, hours=0, minutes=3, seconds=20):
        return timedelta(hours=hours, minutes=minutes, seconds=seconds) * miles

    # Resets the current time to 8:00:00 AM when the program starts processing the path of a new truck
    def reset(self):
        self.current = timedelta(hours=8)

    # Displays the current time as a formatted string
    def display(self):
        if self.current < timedelta(hours=12):
            return str(self.current) + ' AM'
        elif self.current >= timedelta(hours=13):
            return str(self.current - timedelta(hours=12)) + ' PM'
        else:
            return str(self.current) + ' PM'
