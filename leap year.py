# is this a leap year or not
year = int(input("Enter an year"))
if (( year%400 == 0) or ((year%4 == 0) and (year%100 != 0))):
    print("%d is an leap year"%year)
else:
    print("%d is not an leap year" % year)