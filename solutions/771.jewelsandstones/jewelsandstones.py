#  https://leetcode.com/problems/jewels-and-stones/
def numJewelsInStones(jewels: str, stones: str) -> int:
    return sum([1 for i in stones if i in jewels])


jewels = "aA"
stones = "aAAbbbb"
print(numJewelsInStones(jewels, stones))
