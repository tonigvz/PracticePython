#   https://leetcode.com/problems/goal-parser-interpretation/
from click import command


def interpret(command: str) -> str:
    res = command.replace("()", "o")
    res2 = res.replace("(al)", "al")
    return res2


command = "G()(al)"
print(interpret(command))
