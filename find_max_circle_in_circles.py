import numpy as np
from shapely.geometry import Point, Polygon
from scipy.optimize import minimize


def find_max_circle_in_circles(circles):
    # Створення кола як полігона
    def circle_to_polygon(center, radius):
        angles = np.linspace(0, 2 * np.pi, 360)
        x = center[0] + radius * np.cos(angles)
        y = center[1] + radius * np.sin(angles)
        return Polygon(np.column_stack((x, y)))

    # Створюємо полігони для всіх кіл
    circles_polygons = [circle_to_polygon(center, radius) for radius, center in circles]

    # Знаходимо область перетину всіх кіл
    intersection_area = circles_polygons[0]
    for circle_polygon in circles_polygons[1:]:
        intersection_area = intersection_area.intersection(circle_polygon)

    # Перевіряємо, чи не порожня область перетину
    if intersection_area.is_empty:
        return 0, (0, 0)

    # Визначаємо обмеження для x та y на основі меж області перетину
    bounds = intersection_area.bounds

    # Початкова точка (центроїд області перетину)
    initial_point = intersection_area.centroid.coords[0]

    # Об'єктивна функція: мінімізуємо негативну мінімальну відстань до межі
    def objective(xy):
        point = Point(xy)
        return -intersection_area.exterior.distance(point)

    def constraint(xy):
        point = Point(xy)
        return -intersection_area.distance(point)


    # Виконуємо оптимізацію
    result = minimize(objective, initial_point, method='SLSQP', bounds=[(bounds[0], bounds[2]), (bounds[1], bounds[3])], constraints={'type': 'ineq', 'fun': constraint})

    # Перевіряємо успішність оптимізації
    if not result.success:
        return 0, (0, 0)

    return -result.fun, result.x