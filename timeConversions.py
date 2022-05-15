def timeConversion(s):
    # Write your code here
    # get AM or PM suffix
    prefixHour = s[0:2]
    suffix = s[-2:]
    if suffix == 'AM':
        if prefixHour == '12':
            out = s.replace(s[0:2], '00')[:-2]
        else:
            out = s[:-2]
    else:
        if prefixHour == '12':
            out = s[:-2]
        else:
            hour = int(s[0:2])
            hour24 = 12 + hour
            out = s.replace(s[0:2], str(hour24))[:-2]
    print(out)
if __name__ == '__main__':

    s = '07:05:45PM'

    timeConversion(s)
