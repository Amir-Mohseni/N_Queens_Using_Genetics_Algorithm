class Gene:

    def __init__(self, ls):
        self.gene = ls

    def print_gene(self):
        print(self.gene)

    def fitness(self):
        count = 0
        for i in range(len(self.gene)):
            for j in range(i + 1, len(self.gene)):
                if self.gene[i] != self.gene[j] and abs(self.gene[i] - self.gene[j]) != j - i:
                    count += 1
        return count

