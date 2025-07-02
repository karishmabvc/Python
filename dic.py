def digits(year):
    return sum(int(digit) for digit in str(year))
year = input("")
print(digits(year))