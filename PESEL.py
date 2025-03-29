PESEL_LENGTH = 11
PESEL_WEIGHT = (1, 3, 7, 9, 1, 3, 7, 9, 1, 3)
total = correct = male = female = 0
invalid_length = invalid_digit = invalid_date = invalid_checksum = 0


def check_digit(value):
    global invalid_digit
    if not value.isdigit():
        invalid_digit += 1
        return False
    return True


def check_length(value):
    global invalid_length
    if not len(value) == PESEL_LENGTH:
        invalid_length += 1
        return False
    return True


def check_month(value):
    global invalid_date
    year = int(value[0:2])
    month = int(value[2:4])
    day = int(value[4:6])
    century = [1800, 1900, 2000, 2100, 2200]
    if 1 <= month <= 12:
        year += century[1]
    elif 21 <= month <= 32:
        year += century[2]
        month -= 20
    elif 41 <= month <= 52:
        year += century[3]
        month -= 40
    elif 61 <= month <= 72:
        year += century[4]
        month -= 60
    elif 81 <= month <= 92:
        year += century[0]
        month -= 80
    else:
        invalid_date += 1
        return False

    if day < 1:
        invalid_date += 1
        return False
    if (year % 4 == 0 and year % 100 != 0) or year % 400 == 0:
        if month == 2 and day > 29:
            invalid_date += 1
            return False
    else:
        if month == 2 and day > 28:
            invalid_date += 1
            return False
    if month in [1, 3, 5, 7, 8, 10, 12]:
        if day > 31:
            invalid_date += 1
            return False
    elif month in [4, 6, 9, 11]:
        if day > 30:
            invalid_date += 1
            return False
    return True


def checksum(value):
    global male
    global female
    global invalid_checksum
    global correct
    check_sum = 0
    c = 0
    for i in range(10):
        c += (int(value[i]) * PESEL_WEIGHT[i])
        check_sum = (10 - (c % 10)) % 10
    if check_sum == int(value[-1]):
        correct += 1
        if value[-2] in '02468':
            female += 1
        else:
            male += 1
    else:
        invalid_checksum += 1
        return False
    return True


file = open("1e6.dat", 'r')

for pesel in file:
    pesel = pesel.strip()
    total += 1
    if not check_length(pesel):
        continue
    if not check_digit(pesel):
        continue
    if not check_month(pesel):
        continue
    if not checksum(pesel):
        continue

print(total, correct, female, male)
print(invalid_length, invalid_digit, invalid_date, invalid_checksum)

file.close()
