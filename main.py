"""
Darren Bentler 2021 - Using the MTA's GTFS data available online, I plot and draw the NYC subway.
"""

class Station:
    stat_id = ""
    stat_lat = 0.0
    stat_long = 0.0
    def __init__(self, stat_id, stat_lat, stat_long):
        self.stat_id = stat_id
        self.stat_lat = stat_lat
        self.stat_long = stat_long

    def __repr__(self):
        return f"{self.stat_id}, {self.stat_lat}, {self.stat_long}"

if __name__ == "__main__":
    print("Hello World")
    test_station = Station("A", -40.0, -71.00)
    print(test_station)
