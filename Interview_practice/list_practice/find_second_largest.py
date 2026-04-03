abcd = [19,38,44,234,32,33,485,73,33,399,300,33,112,12]

if len(abcd) > 1 :
    print(abcd)
    largest = float('-inf')
    sec_larget = float('-inf')
    for i in abcd:
        if i > largest :   
            sec_larget = largest
            largest = i
        elif i > sec_larget and i != largest:
            sec_larget = i
            
    print(largest)
    print(sec_larget)

    # abcd.sort()
    # print(abcd[-2])


else:
    print("can not compare to another element")