class RemoveZero:
    
    def dup():
        print("start find duplicate")
        a = [1,2,3,4,1,2,3,4,5,6,7,0,0,0,0]
        b = []
        print(f"a = {a}")
        print(f"len(a) = {len(a)}")

        for i in range(len(a)):
            if a[i] != 0:
                b.append(a[i])
           
               
        print(f"b = {b}")
        print(f"len(a) = {len(b)}")
                          
    dup()