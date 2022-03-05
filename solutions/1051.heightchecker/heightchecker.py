#  https://leetcode.com/problems/height-checker/
def heightChecker(heights: list[int]) -> int:
    # return sum([1 for i in range(len(heights)) if heights[i] != sorted(heights)[i]])
    expected = sorted(heights)
    count = 0
    for i in range(len(heights)):
        if heights[i] != expected[i]:
            count += 1
    return count


heights = [5, 1, 2, 3, 4]
print(heightChecker(heights))
