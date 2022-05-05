def assemble_genome2(dna_list):
    file = {}
    for i in range(len(dna_list)):
        for j in range(len(dna_list)):
            if i != j:
                y = 0
                for k in range(9):
                    if dna_list[j][:8] == dna_list[i][-8:]:
                        y = k
                file[(i,j)] = y
    if max(file.values())>0:
        result = "".join(dna_list)
        l = len(result)
        string = []
        for i,b in enumerate(dna_list):
            temp = set(range(len(dna_list)))
            temp.remove(i)
            string.append((b,i,temp))
        while string:
            ans,c,remain = string.pop()
            if len(ans)<l:
                if not remain:
                    result = ans
                    l = len(ans)
                else:
                    temp = [[file[c,d],d] for d in remain]
                    temp.sort()
                    for y,d in temp:
                        ans = ans + dna_list[d][y:]
                        remain = set(remain)
                        remain.remove(d)
                        string.append((ans,d,remain))
        return result
 
  
 
def load_file(filename):
    with open(filename, "r") as file:
        data = file.read()
        dna_list = data.splitlines()
        return dna_list

assemble_genome2(load_file('ms3-dna-50.txt'))
