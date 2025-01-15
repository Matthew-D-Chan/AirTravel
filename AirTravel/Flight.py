"""
******************************
CS 1026 - Assignment 4 - Air Travel
Code by: Matthew Chan
Student ID: mchan654
File Created: November 26, 2024
******************************
This file contains the class Flight. The main info it contains is
the flights specific number the flights origin location, destination
location (given by their respective airport code), and the duration
of the flight. String method is used as well, to print out all the above
info. Constructor used to initialize all the above values as instance variables
"""
from Airport import *

class Flight:

    # Constructor method that initialises variables IF origin and destination are from the Airport class
    # Origin & destination are variables of the Airport class.
    # Ex. Origin = A1 = Airport("YYZ", "Toronto", "Canada")
    def __init__ (self, flight_no, origin, dest, dur):
        if isinstance(origin, Airport) == False or isinstance(dest, Airport) == False:
            raise TypeError("The origin and destination must be Airport objects")
        self._flight_no = flight_no
        self._origin = origin
        self._destination = dest
        self._duration = dur



    # String method created, so when the class is printed, it prints what is in this method, not a memory location
    # When printed: origin_city to dest_city (dur) [domestic/international]
    # Return line:
    # | Since origin & destination are Airport objects, we convert them to strings.
    # | We also round the duration so it has no decimal value (.0), then convert to an int to get
    # | rid of the decimals completely, then convert to string to prevent error
    def __str__ (self):
        if self.is_domestic() == True:
            domestic_value = "domestic"
        else:
            domestic_value = "international"
        return str(self._origin.get_city()) + " to " + str(self._destination.get_city()) + " (" + str(int(round(self._duration, 0))) + "h) [" + domestic_value + "]"



    # If the flights are the same (same origin and destination) it returns True
    # We also check to make sure the 'other' (second) flight is from the flight class
    def __eq__ (self, other):
        if isinstance(other, Flight) == False:
            return False
        if self._origin == other._origin and self._destination == other._destination:
            return True



    # If the whole airport (XYZ,City,Ctry) destination is equal to the airport of the connecting flight, you can add them together
    # Both are airports; they are objects of the airport function (The whole thing)
    # We also check to make sure that the connecting flight is from the flight class
    def __add__ (self, conn_flight):
        if isinstance(conn_flight, Flight) == False:
            raise TypeError("The connecting_flight must be a Flight object")
        if not self._destination == conn_flight._origin:
            raise ValueError("These flights cannot be combined")
        else:
            return Flight(self._flight_no, self._origin, conn_flight._destination, self._duration + conn_flight._duration)



    # All the get functions; return specifically the flight_no, origin, destination, or duration
    def get_flight_no(self):
        return self._flight_no

    def get_origin(self):
        return self._origin

    def get_destination(self):
        return self._destination

    def get_duration(self):
        return self._duration



    # Checks the country of the origin & the country of the destination
    # If the same, it sets the method to True, and if not, to false (which triggers International)
    def is_domestic(self):
        if self._origin.get_country() == self._destination.get_country():
            return True
        else:
            return False



    # All the set functions; allows to change the origin or destination, which are airport classes
    def set_origin(self, origin):
        self._origin = origin

    def set_destination(self, destination):
        self._destination = destination

