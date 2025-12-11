import math

# Координати з угла та відстані
def get_coordinates(angle: int, distance: int):
    angle = angle % 360
    shot_x = distance * math.cos(math.radians(90 - angle))
    shot_y = distance * math.sin(math.radians(90 - angle))
    return int(shot_x), int(shot_y)

# Фігура в координати
def polygon_to_points(polygon):
    polygon_points = [get_coordinates(angle, distance) for angle, distance in polygon.items()]

    return polygon_points