import math
from scipy.spatial import Delaunay
from matplotlib.path import Path
import numpy as np

# Знайти вписаний круг в трикутник
def get_circum_info(polygon_points, triangle):
    side_1, side_2, side_3 = polygon_points[triangle]

    side_4 = 2 * (side_1[0] * (side_2[1] - side_3[1]) + side_2[0] * (side_3[1] - side_1[1]) + side_3[0] * (side_1[1] - side_2[1]))

    vector_x = ( 
        (side_1[0] ** 2 + side_1[1] ** 2) * (side_2[1] - side_3[1]) + 
        (side_2[0] ** 2 + side_2[1] ** 2) * (side_3[1] - side_1[1]) + 
        (side_3[0] ** 2 + side_3[1] ** 2) * (side_1[1] - side_2[1]) 
    ) / side_4

    vector_y = ( 
        (side_1[0] ** 2 + side_1[1] ** 2) * (side_3[0] - side_2[0]) + 
        (side_2[0] ** 2 + side_2[1] ** 2) * (side_1[0] - side_3[0]) + 
        (side_3[0] ** 2 + side_3[1] ** 2) * (side_2[0] - side_1[0]) 
    ) / side_4

    circumcenter = np.array([vector_x, vector_y])

    radius = math.sqrt((circumcenter[0]-side_1[0])**2 + (circumcenter[1]-side_1[1])**2)

    return circumcenter, radius


# Знайти вписаний круг в фігуру
def find_circle_in_polygon(polygon_points):
    polygon_points = np.array(polygon_points)
    polygon_path = Path(polygon_points)

    # Для визначення точок вписаного круга в фігурі застосується Delaunay triangulation
    polygon_delaunay_triangulation = Delaunay(polygon_points)

    # Знайти точки вписаного круга в кожному треугольнику триангуляці
    triangles_circumcenteres = []
    triangles_circumradiuses = []

    for triangle in polygon_delaunay_triangulation.simplices:
        triangle_circumcenter, triangle_circumradius = get_circum_info(polygon_points, triangle)

        triangles_circumcenteres.append(triangle_circumcenter)
        triangles_circumradiuses.append(triangle_circumradius)

    triangles_circumcenteres = np.array(triangles_circumcenteres)
    triangles_circumradiuses = np.array(triangles_circumradiuses)

    circumcenters_inside_polygon = polygon_path.contains_points(triangles_circumcenteres)

    # Знайти центр та радіус круга в фігурі
    if np.any(circumcenters_inside_polygon):
        circumradiuses_inside_polygon =triangles_circumradiuses[circumcenters_inside_polygon]
        max_circumradius = np.max(circumradiuses_inside_polygon)
        max_circumcenter = list(triangles_circumcenteres[circumcenters_inside_polygon][np.argmax(circumradiuses_inside_polygon)])
        
        return [max_circumradius, max_circumcenter]
    
    return []