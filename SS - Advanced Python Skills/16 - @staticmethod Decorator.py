#Bound to class not object lide classmethods 
#Useful to group utility function to a class

import time

class Hour:
    def __init__(self, secs) -> None:
        self.seconds = secs

    @staticmethod
    def secs_to_hours(seconds):
        return time.strftime("%H:%M:%S", time.gmtime(seconds))

    def display_hour(self):
        hour = self.secs_to_hours(self.seconds)
        print("The hour is", hour)

#Using class normally 
h = Hour(65)
h.display_hour()

#Using it as static method
a = Hour.secs_to_hours(65)
print(a)

#NOTES 
#   -Can use without creating object
#   -Static method knows nothing about the class - Just paramerters 