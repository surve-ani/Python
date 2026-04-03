class FindDuplicate:

    def dup():
        print("find duplicate....")
        st = "abccdefgqbdeab"
        f_dup = ""

        print(f"a = {st}")
        print(f"len(a) = {len(st)}")

        for i in st:
            count = 0
            for j in st:
                if i == j:
                    count = count + 1
                    
            if count>1:
                if i not in f_dup:
                    print(f"{i} = {count}")
                    f_dup = f_dup+i

               
        print(f"rm_dup = {f_dup}")
        print(f"len(rm_dup) = {len(f_dup)}")


    dup()