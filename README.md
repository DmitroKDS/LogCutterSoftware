# LogCutterSoftware

I developed software for ukrainian log cutting company - that helps optimize how logs are cut on industrial machines.

The machines use laser sensors to scan each log and detect its exact shape. Based on these laser points, 
I implemented a Delaunay triangulation algorithm to calculate:
the largest possible cylinder that can be inscribed inside the log, the optimal center and the maximum radius.

# Results
This allows the company to cut logs with less material waste and to produce a larger, more efficient cylinder from every piece of wood.

# Use

### Installation
`pip install -r requirements.txt`

### Run
`python main.py`
