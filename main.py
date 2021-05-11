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

def parse_data(file):
    """
    Parses through stops.txt and grabs all of the necessary data about a route's stops.
    Returns a list of Stations.
    string --> list(Station)
    """
    with open(file, "r") as f:
        stations = []
        for line in file:
            line = f.readline()
            if "shape_id" in line: # Passes the first line in shapes.txt, which is not needed.
                pass
            else:
                f_mat = line.split(",")
                stations.append(Station(f_mat[0], f_mat[1], f_mat[2])) # We already know from shapes.txt that the format is "Shape ID", "Shape Point Latitude", "Shape point Longitude"
        return stations


if __name__ == "__main__":
    stations = parse_data("K:\\!dev\\Python\\nyc_subway2\\NYC-Subway-From-GTFS-Data\\shapes.txt") # You'll need to copy your own path to the shapes.txt file here.
    print(stations)

