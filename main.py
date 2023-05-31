import gene
import random

N = 8
Gene_Size = 1000
Generation_Number = 10

genes = []
fitness = []
ls = []

for i in range(N):
    ls.append(i + 1)

best_gene = gene.Gene(ls)

for i in range(Gene_Size):
    random.shuffle(ls)
    cur_gene = gene.Gene(ls)
    if cur_gene.fitness() > best_gene.fitness():
        best_gene = cur_gene
    genes.append(cur_gene)
    fitness.append(cur_gene.fitness())

for gen_num in range(Generation_Number):
    new_genes = []
    new_fitness = []

    while len(new_genes) < Gene_Size:
        par_list = random.choices(population=genes, weights=fitness, k=2)
        par1 = par_list[0]
        par2 = par_list[1]
        break_point = random.randint(0, 8)

        new_child1 = gene.Gene(par1.gene[:break_point] + (par2.gene[break_point:]))
        new_child2 = gene.Gene(par2.gene[:break_point] + (par1.gene[break_point:]))

        new_genes.append(new_child1)
        new_fitness.append(new_child1.fitness())

        new_genes.append(new_child2)
        new_fitness.append(new_child2.fitness())

    genes = new_genes
    fitness = new_fitness

    Gene_Size = len(genes)

    for i in range(Gene_Size):
        if fitness[i] > best_gene.fitness():
            best_gene = genes[i]

print("N is", N)
print("Gene Size is", Gene_Size)
print("Generation Number is", Generation_Number)
print("Best Gene Found:", best_gene.gene)
print(best_gene.fitness())