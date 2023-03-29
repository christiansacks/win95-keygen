import datetime,random,sys

def genKey():
    # XXXYY-OEM-NNSSSSS-ZZZZZ
    #
    # XXX   = Ordinal of the day
    # YY    = Year (95-03)
    # NN    = zeros
    # SSSSS = Random numbers, sum is divisible by 7
    # ZZZZZ = Random numbers
    today            = datetime.date.today()
    #day_of_year      = today.timetuple().tm_yday # use the actual day of the year
    day_of_year      = random.randint(1,365) # use any random 3 digit number
    random_year_full = random.randint(1995,2003)
    random_year_two  = str(random_year_full)[2:]
    rand_five = random.randint(10000,99999)
    while True:
        number = random.randint(10000,99999)
        digit_sum = sum(map(int, str(number)))
        if digit_sum % 7 == 0:
            break
    newKey = "{:03d}{}-OEM-{}{}-{}".format(day_of_year,random_year_two,"00",number,rand_five)
    return newKey

if len(sys.argv) > 1:
    try:
        argument = int(sys.argv[1])
        if argument >= 1 and argument <= 20:
            for i in range(1, argument+1):
                print("{}:\t{}".format(i,genKey()))
        else:
            print("Argument not between 1 and 20.")
    except ValueError:
        print("Argument is not an integer.")
else:
    print(genKey())
