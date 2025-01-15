"""
******************************
CS 1026 - Assignment 4 - Air Travel
Code by: Matthew Chan
Student ID: mchan654
File Created: November 26, 2024
******************************
Assign4 contains the main functions of this program. Loads in all the data
from the files, has a method that returns the airport of a given airport code,
has a method that finds all flights with a given city as the origin or destination,
has a method that returns all fights with a given country as the origin or
destination, has a method to determine flights with connecting flights,has a method
to find the shortest flight from a given airport, and a method to find a return flight
for a given flight.
"""
# You must create the Flight.py and Airport.py files.
from Flight import *
from Airport import *

# Define your collections for all_airports and all_flights here.
all_airports = []
all_flights = {}



def load_data(airport_file, flight_file):
    try:
        # Opens airport file, reads from it, strips, splits into code, city country
        # Puts all the airports into the all_airports list
        in_airport_file = open(airport_file, "r")
        for line in in_airport_file:
            line = line.strip()
            line = line.split("-")
            airport_obj = Airport(line[0].strip(), line[2].strip(), line[1].strip())
            all_airports.append(airport_obj)

        # Creating a dict for airports to access codes easier
        # Key is the code (YYZ), value is the whole thing (code, city, country)
        # Makes the next step of finding origin and destination airports easy
        airport_dict = {}
        for airport in all_airports:
            airport_code = airport.get_code()
            airport_dict[airport_code] = airport

        # Opens flight file, reads from it, strips, splits into flight no, origin, dest, dur
        # We get origin and destination by taking the current code (ex. YYZ) and looking up its specific value from the dict
        # The specified value is the respective airport object of that code
        # line[3] changed to float so it can be rounded
        # Add a new list to the all_flights dict if it is a new code. Then Add the flight to that code key
        # Except statement added to catch any errors
        in_flight_file = open(flight_file, "r")
        for line in in_flight_file:
            line = line.strip()
            line = line.rsplit("-", 3)
            origin = airport_dict.get(line[1].strip())
            destination = airport_dict.get(line[2].strip())
            flight_obj = Flight(line[0].strip(), origin, destination, float(line[3].strip())) # "error origin & destination must be airport objects. Literally the whole thing"
            #print(flight_obj)
            if line[1] not in all_flights:
                all_flights[line[1]] = []
            all_flights[line[1]].append(flight_obj)
        in_airport_file.close()
        in_flight_file.close()
        return True
    except Exception as e:
        print("Error:", e)
        return False




# Return the airport object based off the given 3 letter code
# Raise a value error if no airport found for that code
def get_airport_by_code(code):
    for airport in all_airports:
        if airport.get_code() == code:
            return airport
    raise ValueError("No airport with the given code: ", code)




# For loop going through all the flights per code
# Another for loop going through each flight in that list of flights per code
# Checks the inputted city to the city in the destination & origin of each flight
def find_all_city_flights(city):
    city_list = []
    for flights in all_flights.values():
        for flight in flights:
            if flight.get_origin().get_city() == city or flight.get_destination().get_city() == city:
                city_list.append(flight)
    return city_list




# Exact same as above but now doing it for countries
def find_all_country_flights(country):
    country_list = []
    for flights in all_flights.values():
        for flight in flights:
            if flight.get_origin().get_country() == country or flight.get_destination().get_country() == country:
                country_list.append(flight)
    return country_list




def find_flight_between(orig_airport, dest_airport):
    # Check if there is a direct flight (orig goes straight to dest)
    # Go through all_flights if the flight origin == oring airport and the fight destination == dest airport then it is direct
    for flights in all_flights.values():
        for flight in flights:
            if flight.get_origin() == orig_airport and flight.get_destination() == dest_airport:
                return f"Direct Flight: {orig_airport.get_code()} to {dest_airport.get_code()}"

    # If no direct flight, check for a singly connecting flight
    dest_origin = set() # Will contain all destinations of the origin airport
    origin_dest = set() # Will contain all the origins of the destination airport

    # This will put all the destinations of the origin_airport into a set
    # Uses the codes
    for flights in all_flights.values():
        for flight in flights:
            if flight.get_origin() == orig_airport:
                dest_origin.add(flight.get_destination().get_code()) # this is a whole airport. Maybe have to change to a city??

    # This will put all the origins of the destination_airport into a set
    # Uses the codes
    for flights in all_flights.values():
        for flight in flights:
            if flight.get_destination() == dest_airport:
                origin_dest.add(flight.get_origin().get_code())

    # Intersect both sets, this will give all possible connecting flights
    # Add the if statement so that the set will only be returned if there actually is codes in the set
    connecting_airports = dest_origin.intersection(origin_dest)
    if connecting_airports:
        return connecting_airports

    # Value error is raised if the other two are returned; that means no direct or single-hop flights
    raise ValueError(f"There are no direct or single-hop connecting flights from {orig_airport.get_code()} to {dest_airport.get_code()}")




def shortest_flight_from(orig_airport):
    # Loop through all flights until you find a flight that has the orig_airport as its origin
    # Find the direct flight that has the shortest duration
    # Compare all the duration times in a loop to find smallest one
    # If we find another smallest flight, update nothing
    shortest_dur = 100.0
    shortest_flight = ""
    for flights in all_flights.values():
        for flight in flights:
            if flight.get_origin() == orig_airport:
                if flight.get_duration() < shortest_dur:
                    shortest_dur = flight.get_duration()
                    shortest_flight = flight
                elif flight.get_duration() == shortest_dur:
                    continue
    return shortest_flight




def find_return_flight(first_flight):
    # given the flight object, locate its origin and destination
    # Find a flight that has its origin as the destination of first_flight
    # and a destination as the origin of the first_flight
    return_destination = first_flight.get_origin()
    return_origin = first_flight.get_destination()
    for flights in all_flights.values():
        for flight in flights:
            if return_origin == flight.get_origin() and return_destination == flight.get_destination():
                return_flight = flight
                return return_flight
    raise ValueError (f"There is no flight from {return_origin.get_code()} to {return_destination.get_code()}")


if __name__ == "__main__":
    # Add any of your own tests on your functions here.
    # Make sure you don't have any testing or debugging code outside of this block!

    # For load_data
    airport_file = "airports.txt"
    flight_file = "flights.txt"
    load_data(airport_file, flight_file)

    # For get_airport_by_code
    test_code = "YYZ"
    get_airport_by_code(test_code)

    # For find_all_city_flights
    test_city = "Toronto"
    print(find_all_city_flights(test_city))

    # For find_all_country_flights(country)
    test_country = "Canada"
    find_all_country_flights(test_country)

    # For find_flight_between(orig_airport, dest_airport)
    test_orig_airport = Airport("YYZ", "Toronto", "Canada")
    test_dest_airport = Airport("YUL", "Montreal", "Canada")
    print(find_flight_between(test_orig_airport, test_dest_airport))
