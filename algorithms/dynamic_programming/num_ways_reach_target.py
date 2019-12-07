"""
Let’s try the same for one more problem: counting the number of ways to reach a given score in a game
Consider a game where a player can score 3 or 5 or 10 points at a time. Given a total score n, find the
number of ways to reach the given score. The order of scoring does not matter.

eg : sum = 20
     points = {3, 5, 10}
expected output -> 4
number of ways to reach -> (10, 10) (5, 5, 10) (5, 5, 5, 5) (3, 3, 3, 3, 3, 5)
"""


# Approach 1 -> recursion without memoization
def num_ways(points, total, num_combinations):
    for point in points:
        temp_total = total
        temp_total -= point
        print("temp total for pick {} is {}".format(point, temp_total))
        if temp_total == 0:
            print("found zero for point", point)
            return 1
        if temp_total < 0:
            return 0
        if temp_total > 0:
            num_combinations += num_ways(points, temp_total, num_combinations)

    return num_combinations

# Approach 2 -> recursion with memoization
