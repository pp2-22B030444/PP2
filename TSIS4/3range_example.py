
def range_analog(n):
    current_number = 0
    while current_number < n:
        # return current_number
        yield current_number
        current_number += 1


numbers = range_analog(5) # __iter__()
for number in numbers:  # __next__()
    print(number)
print(type(numbers))