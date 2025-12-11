from polygon_to_points import *
from find_circle_in_polygon import *
from find_max_circle_in_circles import *
from get_circumscribed_circle_radius import *

#Отримати круг який можна вписати в бревно
def get_circle_in_polygons(polygons):
    circles_in_polygons = []

    # Отримати круги які входять в фігуру бревно
    for polygon in polygons:
        polygon_points = polygon_to_points(polygon)
        circle_in_polygon = find_circle_in_polygon(polygon_points)
        if circle_in_polygon!=[]:
            circles_in_polygons.append(circle_in_polygon)

    # Всі радіуси та центри вписаних кругів
    circle_in_polygon_radius, circle_in_polygon_center = find_max_circle_in_circles(circles_in_polygons)

    # Отримати радіус та центр круга який можна вписати в круги
    circumscribed_circle_radius = get_circumscribed_circle_radius(polygons, circle_in_polygon_center)

    return circle_in_polygon_radius, circle_in_polygon_center, circumscribed_circle_radius, circles_in_polygons