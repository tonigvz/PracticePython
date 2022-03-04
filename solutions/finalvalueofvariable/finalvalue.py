#  https://leetcode.com/problems/final-value-of-variable-after-performing-operations/
def finalValueAfterOperations(operations: list[str]) -> int:
    return sum([-1 if i in "--XX--" else 1 for i in operations])


operations = ["++X", "++X", "X++"]
print(finalValueAfterOperations(operations))
