#### <span class="span-underline">The Why</span>

*"Why would you want to render a map of the NYC subway system when you could just look at it on your phone?"*

Well my friend, the answer is quite simple:

- I've always wanted to work with GTFS in some way, shape, or form.
- I get to practice working with data in Python.
- I like the subway system.

Thankfully, the MTA's GTFS data is quite easy to read and figure out what line is what just from the `shapes.txt`. But before we dive into the *code*, let's talk about GTFS for a second.

#### <span class="span-underline">What is GTFS?</span>

GTFS stands for "General Transit Feed Specificaton". Public transport agencies can format their data to the GTFS standard and publish it for developers and data analysis to crunch and manipulate.

You can read more about GTFS [here](https://developers.google.com/transit/gtfs).

You can access the MTA's GTFS data [on their website](http://web.mta.info/developers/developer-data-terms.html#data). I'm working with static data, so I downloaded the "New York City Transit Subway" data on their page.

#### <span class="span-underline">Requirements</span>

Using this specific data set, we only need a graphing library. I went ahead and used [matplotlib](https://matplotlib.org/), but you can pretty much use any graphing library you're most comfortable with.

#### <span class="span-underline">Data, Data, Data</span>

Since we're only after a very simple render of the subway system, we'll only be accessing one file: `shapes.txt`. When you open up `shapes.txt`, you'll be greeted with the following information:

```python
shape_id,shape_pt_lat,shape_pt_lon,shape_pt_sequence,shape_dist_traveled
1..N03R,40.702068,-74.013664,0,
1..N03R,40.703199,-74.014792,1,
1..N03R,40.703226,-74.014820,2,
1..N03R,40.703253,-74.014846,3,
1..N03R,40.703280,-74.014870,4,
1..N03R,40.703307,-74.014893,5,
...
```

It'll look intimidating at first, but this data is very easy to read. `shape_id` refers to the subway service the station belongs to. In the case of `1..N03r`, we can infer that this station serves the `1` train for one of it's services.

The next two positions, `shape_pt_lat` and `shape_pt_lon` refer to the stations latitude and longitude. The next point, `shape_pt_sequence`, is an index of where the station is for the service. Now how can we store all of this information?

The solution I came out with was by creating a class object "Station":

```python
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
```

The station class is able to store the 3 pieces of information we're after: The `shape_id`, the `shape_pt_lat`, and the `shape_pt_lon`. We can disregard the `shape_pt_sequence` data since we don't really need it.

With the station class done, we now have an object that can tell us what line it belongs to and it's position within the world. So we can work on parsing that data into a `Station` object and storing it into a list:

```python
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
                tmp_stat = Station(f_mat[0], f_mat[1], f_mat[2]) # We already know what information we need from each line since GTFS files follows a set standard.
                stations.append(tmp_stat)
        f.close()
        return stations
```

And in our `if __name__ == "__main__`:

```python
if __name__ == "__main__":
    stations = parse_data("K:\\!dev\\Python\\nyc_subway2\\NYC-Subway-From-GTFS-Data\\nyc\\shapes.txt") # You'll need to copy your own path to the shapes.txt file here.
```

Before we enter this information into `matlib.pyplot`, we'll need to get the correct line color for each station. Lucky for us, our `Station`'s `stat_id` variable already tells us that information.

What better way to switch between variable outputs than a `switch` statement!

*Oh right we're using Python...*

We can get the correct line color by passing the `stat_id` into a function, which will check what group a station belongs to and return the correct line color. While this is not the most optimal way of getting the correct color, it still works pretty quickly since the service indicator (ie, 1, 2, 3, A, C, E) is always the first character in `stat_id`. If you're unfamilar with the NYC subway color scheme, you can find a key [here](http://web.mta.info/developers/resources/line_colors.htm).

```python
def color_stations(station_id):
    """
    Returns station color in accordance of the line it belongs to.
    Station.stat_id --> string
    """
    for char in station_id:
        if char in "123":
            return "red"
        if char in "456":
            return "green"
        if char in "7":
            return "magenta"
        if char in "ACEH":
            return "blue"
        if char in "BDFM":
            return "orange"
        if char in "G":
            return "lime"
        if char in "JZ":
            return "brown"
        if char in "NQR":
            return "yellow"
        if char in "LSI":
            return "gray"
        return "lime"
```

Now that we have that, we can finish off `if __name__ == "__main__"` with the following code:

```python
if __name__ == "__main__":
    stations = parse_data("K:\\!dev\\Python\\nyc_subway2\\NYC-Subway-From-GTFS-Data\\nyc\\shapes.txt") # You'll need to copy your own path to the shapes.txt file here.
    plt.scatter([ float(obj.stat_long) for obj in stations ], [ float(obj.stat_lat) for obj in stations ], color=[ color_stations(obj.stat_id) for obj in stations ])
    plt.show()
```

When we run our code, we get a full map of the network - including the Staten Island Railway!

![NYC Subway Render](/static/img/nyc_subway.png)

#### <span class="span-underline">Conclusion</span>

That's how you make a very simple render of the NYC subway system from MTA GTFS data. The system I built is actually pretty modular. Given any `shapes.txt` file and a properly configured `color_stations()` function, we can render a map of any transit system that publishes its data via GTFS.

We could also go into further into data analysis with the GTFS data, such as generating [heat maps of stops with the most trips](https://dzone.com/articles/gtfs-transit-data-visualization-in-r). But that's a bit out of the scope of this project.

Thank you for reading. You can check out the source code via the button below:

<div class="container center-text spacer-25px">
    <a href="/projects">
        <button type="button" id="back" onclick="" class="btn btn-dark btn-lg">Go Back to Projects</button>
    </a>
    <a href="https://github.com/dbentler/NYC-Subway-From-GTFS-Data">
        <button type="button" id="linkedin" onclick="" class="btn btn-dark btn-lg">Source Code (Github)</button>
    </a>
</div>
