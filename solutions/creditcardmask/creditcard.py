# https://www.codewars.com/kata/5412509bd436bd33920011bc
def maskify(cc):
    # f formatted string that multiplies "#" with the length of the string minus last 4
    return f"{'#' * (len(cc) - 4)}{cc[-4:]}"


print(maskify("4556364607935616"))
