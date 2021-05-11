"""
Darren Bentler 2021 - Using the MTA's GTFS data available online, I plot and draw the NYC subway.
"""
import matplotlib.pyplot as plt

class Station:
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
        while True:
            line = f.readline()
            if not line:
                break
            elif "shape_id" in line:
                pass
            else:
                f_mat = list(line.split(","))
                tmp_stat = Station(f_mat[0], f_mat[1], f_mat[2])
                stations.append(tmp_stat)
        return stations


if __name__ == "__main__":
    stations = parse_data("K:\\!dev\\Python\\nyc_subway2\\NYC-Subway-From-GTFS-Data\\shapes.txt") # You'll need to copy your own path to the shapes.txt file here.
    for obj in stations:
        print(obj.stat_lat, obj.stat_long)

