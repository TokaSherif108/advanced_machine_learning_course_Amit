def century(year):
    # Finish this :)
    year=int(input(" enter a year to check the century "))
    if year[-1]and year[-2]== 0:
        print(year[0:1])
    else:
        print(year[0:1]+1)
        return 
    century(year)