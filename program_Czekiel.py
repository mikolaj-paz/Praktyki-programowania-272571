import re

def Add(numbers):
    if numbers == "" or numbers == ",":
        return 0
    elif re.match(r'^\d+((,|\n)\d+)*$', numbers):
        splitted = re.split(r',|\n', numbers)
        nums = []
        for n in splitted:
            if n.isdigit():
                nums.append(int(n))
            else:
                return -1
        return sum(nums)
    else:
        return -1