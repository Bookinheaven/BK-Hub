if __name__ == '__main__':
    s = 'qA2'
    isal = False
    isalno = False
    isdi = False
    islow = False
    isup = False
    for x in s:
        if x.isalnum() == True:
            isalno = True
        if x.isalpha() == True:
            isal = True
        if x.isdigit() == True:
            isdi = True
        if x.islower() == True:
            islow = True
        if x.isupper() == True:
            isup = True

    print(isalno,isal, isdi, islow, isup, sep='\n')