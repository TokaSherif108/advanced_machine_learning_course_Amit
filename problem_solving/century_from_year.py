def century(year):
    # Finish this :)
        year=int(input(" enter year to know the century "))
        if year %100 == 0:
            print(year//100)
        else:
            print((year//100)+1)
century(year=1998)