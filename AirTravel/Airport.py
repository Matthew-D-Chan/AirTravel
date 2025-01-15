"""
******************************
CS 1026 - Assignment 4 - Air Travel
Code by: Matthew Chan
Student ID: mchan654
File Created: November 26, 2024
******************************
This file contains the class Airport. The main info it contains is
an airports specific code (ex. YYZ), city, and country, getter and
setter methods are added as well so these values can be changed or
used. String method used as well, and constructor initialised all
the instance variables
"""
class Airport:

    # Constructor method to initiate all variables
    def __init__(self, code, city, country):
        self._code = code
        self._city = city
        self._country = country



    # String method created, so when the class is printed, it prints what is in this method, not a memory location
    def __str__(self):
        return self._code + " (" + self._city + ", " + self._country + ")"



    # Equals method compares the instance attributes. which are the same.
    # Prevents the comparison of memory locations, which would output False even if the values were the same
    def __eq__(self, other):
        if self._code == other._code: # Compares the instance variables
            return True
        if isinstance(other, Airport) == False:
            return False



    # Getter methods used to get info without changing it
    def get_code(self):
        return self._code

    def get_city(self):
        return self._city

    def get_country(self):
        return self._country



    # Setter methods used to change the value in an object
    def set_city(self, city):
        self._city = city

    def set_country(self, country):
        self._country = country
