# Render the NYC Subway System via GTFS Data!

Through this project, I render the NYC subway system with data provided by the MTA through GTFS.

The program, `main.py` reads through `stops.txt` and parses the data into three components:

- The line ID (1, 2, 3, A, C, E, etc).
- The station's latitude.
- The station's longitude.

It then creates a "Station" object that only knows what line it belongs to and where it's located.

Then, using matplotlib, I plot those stations on the map and color them according to their line number.

# What about other transit systems?

The best part is that the system I currently have set up is fully modular. All you'll need to do is create a color lookup function and assign the correct color depending on the station id.

Enjoy!

# Dependencies
matplotlib

You can also run `pip install requirements.txt`.