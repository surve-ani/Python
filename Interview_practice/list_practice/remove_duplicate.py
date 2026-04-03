class RemoveDuplicate:
    
    def dup():
        print("start find duplicate")
        a = [1,2,3,4,1,2,3,4,5,6,7]
        b = []
        print(f"a = {a}")
        print(f"len(a) = {len(a)}")

        for i in range(len(a)):
            count = 0
           
            for j in range(len(a)):
                if a[i] == a[j]:
                    count = count + 1
                    
            if count==1:
                if a[i] not in b:
                    print(f"{a[i]} = {count}")
                    b.append(a[i])
               
        print(f"b = {b}")
        print(f"len(a) = {len(b)}")
                          
    dup()