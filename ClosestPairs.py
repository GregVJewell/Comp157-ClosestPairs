import math

#ALGORITHM BruteForceClosestPair(P)
# Finds distance between two closest points in the plane by brute force
# Input: A list P of n (n ≥ 2) points p1(x1, y1), . . . , pn(xn, yn)
# Output: The distance between the closest pair of points
# d←∞
# for i ←1 to n − 1 do
#   for j ←i + 1 to n do
#       d ←min(d, sqrt((xi − xj )**2 + (yi − yj )**2)) # sqrt is square root
# return d

def BruteForceClosestPair(P):
    d = math.inf
    n = len(P)
    i = 1; j = i
    closest_pair = [(), ()]

    print("-----START------")
    if n >= 2:
        for i in range(n):
            for j in range(i + 1, n):
                print(P[i], P[j])
                sqrt = math.sqrt(((P[i][0] - P[j][0]) ** 2) + ((P[i][1] - P[j][1]) ** 2))
                if d > sqrt:
                    closest_pair[0] = P[i]; closest_pair[1] = P[j]
                d = min(d, sqrt)
                print(sqrt)
        print("Shortest Distance is: %f2" % d, closest_pair)
        return d, closest_pair
    else:
        print("Not a valid list, exiting")
        return -1, closest_pair


def main():
    pairs = [(1, 3), (8, 20), (0, 4), (12, 5)]
    BruteForceClosestPair(pairs)

    pairs = [(1, 0)]
    BruteForceClosestPair(pairs)

    pairs = [(0, 20), (2, 5), (3, 8), (12, 1), (17, 16)]
    BruteForceClosestPair(pairs)

main()
