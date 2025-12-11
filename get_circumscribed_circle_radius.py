import math
from polygon_to_points import *

def get_circumscribed_circle_radius(polygons, center_point):
    polygons_points = []
    for polygon in polygons:
        polygon_points = polygon_to_points(polygon)
        polygons_points.extend(polygon_points)
    
    max_radius = 0
    for point in polygons_points:
        distance = math.sqrt( (point[0]-center_point[0])**2 + (point[1]-center_point[1])**2 )
        if distance > max_radius:
            max_radius = distance

    return max_radius