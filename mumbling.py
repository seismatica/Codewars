# http://www.codewars.com/kata/mumbling/train/python
# accum("abcd")    # "A-Bb-Ccc-Dddd"
# accum("RqaEzty") # "R-Qq-Aaa-Eeee-Zzzzz-Tttttt-Yyyyyyy"
# accum("cwAt")    # "C-Ww-Aaa-Tttt"

# Best practice: use generator expression that can be used by an enclosing function (join)
# def accum(s):
#     return '-'.join(c.upper() + c.lower() * i for i, c in enumerate(s))


def repeat(letter, time):
    string = letter * time
    return string.title()


def accum(string):
    accum_string = ""
    i = 0
    while i < len(string):
        accum_string += repeat(string[i], i + 1)
        if i < (len(string) - 1):
            accum_string += "-"
        i += 1
    return accum_string


print(accum("aBcD"))
