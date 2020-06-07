
import math

def distance_btwn_points(p1,p2):
    return math.sqrt((p1[0] - p2[0]) *
                     (p1[0] - p2[0]) +
                     (p1[1] - p2[1]) *
                     (p1[1] - p2[1]))

def closest_brute_force(P,n):
    mini_val = float('inf')
    for i in range(n):
        for j in range(i + 1, n):
            if distance_btwn_points(P[i], P[j]) < min_val:
                min_val = distance_btwn_points(P[i], P[j])

    return min_val

def closest_in_strip(strip,size,d):
    mini_val = d
    strip.sort(key=lambda y : y[1])
    for i in range(size):
        j = i + 1
        while j < size and (strip[j][1] -
                            strip[i][1]) < mini:
            mini_val = distance_btwn_points(strip[i], strip[j])
            j += 1

    return min_val

def closest_in_halves(P,n):
    if n <= 3:
        return closest_brute_force(P,n)

    mid = n/2
    middle_value = P[mid]
    dl = closest_in_halves(P[:mid],mid)
    dr = closest_brute_force(P[mid:],n-mid)
    mini = min(dl,dr)
    strip = []
    for i in range(n):
        if abs(P[i][0] - middle_value[0]) < mini:
            strip.append(P[i])

    return min(mini,closest_in_strip(strip,len(strip),mini))

def closest(P,n):
    P.sort(key = lambda x : x[0])
    return closest_in_halves(P,n)

P = [(2, 3),(12, 30),
     (40, 50), (5, 1),
     (12, 10),(3, 4)]
n = len(P)
print("The smallest distance is",
                   closest(P, n))
