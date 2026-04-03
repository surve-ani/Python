

class FindDuplicate:
    
    def dup():
        print("start find duplicate")
        a = [1,2,3,4,1,2,3,4,5,6,7]
        b = []
        print(f"a = {a}")
        print(f"len(a) = {len(a)}")

        for i in a:
            count = 0
            for j in a:
                if i == j:
                    count = count + 1
                    
            if count>1:
                if i not in b:
                    print(f"{i} = {count}")
                    b.append(i)

               
        print(f"b = {b}")
        print(f"len(a) = {len(b)}")
                          
    dup()