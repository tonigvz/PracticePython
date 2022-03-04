#  https://leetcode.com/problems/kids-with-the-greatest-number-of-candies/
def kidsWithCandies(candies: list[int], extraCandies: int) -> list[bool]:
    return [True if i + extraCandies >= max(candies) else False for i in candies]


candies = [2, 3, 5, 1, 3]
extraCandies = 3
print(kidsWithCandies(candies, extraCandies))
