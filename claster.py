import math

def set_k(points):
    lst_x, lst_y = zip(*points)
    myltiply_sum = sum(a[0] * a[1] for a in points)
    sum_x = sum(lst_x)
    sum_y = sum(lst_y)
    square_x_sum = sum([x ** 2 for x in lst_x])
    return (len(lst_x) * myltiply_sum - sum_x * sum_y) / (len(points) * square_x_sum - sum_x ** 2)
def set_b(points, a):
    lst_x, lst_y = zip(*points)
    sum_x = sum(lst_x)
    sum_y = sum(lst_y)
    return (sum_y - a * sum_x) / len(points)
def set_bisector_k(a1, a2):
    grd1 = math.atan(a1)
    grad2 = math.atan(a2)
    grad_bisector = (grd1 + grad2) / 2
    return math.tan(grad_bisector)
def set_bisector_b(b1, b2):
    return (b1 + b2) / 2

points1 = [ (1, 5), (2, 2), (4, 4), (2.5, 3) ]
points2 = [ (5, 1), (4, 0), (4, -2), (8, -3) ]

a1 = set_k(points1)
b1 = set_b(points1, a1)
print(f'прямая для первого массива точек: y = {a1: .3f}x + {b1: .3f}')
a2 = set_k(points2)
b2 = set_b(points2, a2)
print(f'прямая для второго массива точек: y = {a2: .3f}x + {b2: .3f}')
a_bisector = set_bisector_k(a1, a2)
b_bisector = set_bisector_b(b1, b2)

print(F"коэф K разделяющей прямой равен {a_bisector: .3f}, коэф b равен {b_bisector: .3f}")
print(f'итоговая разделяющая прямая: y = {a_bisector: .3f}x + {b_bisector: .3f}')
