
def assemble_genome2(dna_list):
  n = len(dna_list)
  overlaps = [[0 for _ in range(n)] for _ in range(n)]
  for i in range(n):
    for j in range(n):
      if i == j:
        continue
      x, y = dna_list[i], dna_list[j]
      #size = len(x)
      for k in range(1, len(x)):
        if y.startswith(x[k:]): #checking if string 
          overlaps[i][j] = len(x) - k
          break
          
def load_file(name):
  my_file = open(name, "r")
  dna = my_file.read()
  print(dna)
        
  assemble_genome2(load_file('ms3-dna-mammuthus.txt'))
