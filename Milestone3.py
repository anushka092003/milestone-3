def assemble_genome2(dna_list):
    dict = {}
    for i in range(len(dna_list)):
        for j in range(len(dna_list)):
            if i != j:
                y = 0
                for k in range(8):
                    if dna_list[j][:8]==dna_list[i][-8:]:
                        y = k
                dict[(i,j)] = y
    if max(dict.values()) > 0 :
        ret = "".join(dna_list)
        l =len(ret)
        string = []
        while string:
            ans,cur,remain=string.pop()
            if len(ans)<l:
                if not remain:
                    ret = ans
                    l=len(ans)
                else:
                    tmp=[[dict[cur,idx],idx] for idx in remain]
                    tmp.sort()
                    for y,idx in tmp:
                        nans = ans+dna_list[idx][y:]
                        nremain=set(remain)
                        nremain.remove(idx)
                        string.append((nans,idx,nremain))
        return ret
 
def load_file(file):
    with open(file, "r") as infile:
        data = infile.read()
        dna_list = data.splitlines()
        return dna_list

assemble_genome2(load_file('ms3-dna-50.txt'))
