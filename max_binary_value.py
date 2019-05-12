import random
import matplotlib.pyplot as plt

# Base algorithm taken from:
# COLEY, David A. An Introduction to Genetic Algorithms for Scientists and Engineers. 1998.


def function(x: int) -> int:
    return x


def start(gens: int, chromosomes: int) -> list:         # Create y chromosomes with x random gens in it
    return [[random.randint(0, 1) for _ in range(gens)] for _ in range(chromosomes)]


def evaluation(unordered_population: list) -> list:      # Sort the population according to their values
    values = [0]*len(unordered_population)
    for i in range(len(unordered_population)):
        values[i] = function(int(str(int(''.join(map(str, unordered_population[i])))), 2))
    values, ordered_population = zip(*sorted(zip(values, unordered_population), reverse=True))
    return ordered_population


def selection(whole_population: list) -> list:      # Selects the best (first) half of the ordered population
    selected_population = [0]*int(len(whole_population)/2)
    for i in range((int(len(whole_population)/2))):
        selected_population[i] = whole_population[i]
    return selected_population

    # This code selects the best ones through the ordering and slicing.
    # Has to be changed by random selection trough the slicing of the evaluations percents.


def crossover(selected_population: list) -> list:  # Messy function, to work on
    parents = [0]*int(len(selected_population)/2)
    for i in range(int(len(selected_population)/2)):
        parents[i] = i
    random.shuffle(parents)
    for i in range(0, int(len(selected_population)/2), 2):
        x = random.randint(0, (int(len(selected_population[i])-1)))
        tmp = selected_population[parents[i]][:x].copy()
        selected_population[parents[i]][:x] = selected_population[parents[i+1]][:x]
        selected_population[parents[i + 1]][:x] = tmp
    return selected_population


def mutation(child_population: list) -> list:       # 0.8 percent chance of an chromosomes mutation
    for i in range(int(len(child_population))):
        probability = random.randint(0, 1000)
        if probability <= 8:     # if this happens, the exchange of allele in the gene is still not guaranteed
            mutated_allele = random.randint(0, int(len(child_population[0]))-1)
            child_population[i][mutated_allele] = random.randint(0, 1)
    return child_population


def merge_population(population_a: list, population_b: list) -> list:
    return population_a+population_b


# Main code::
generations_number = int(input("Choose the number of generations:"))
gene_quantities = int(input("Choose the gene quantities in each chromosome: "))
chromosome_quantities = int(input("Choose the chromosome quantities in the population: "))

population = start(gene_quantities, chromosome_quantities)

x_axis_values = [0]*generations_number
y_axis_values = [0]*generations_number

for i in range(0, generations_number):
    population = merge_population(
        mutation(crossover(selection(evaluation(population))))
        , start(gene_quantities, int(chromosome_quantities/2)))

    x_axis_values[i] = i
    tmp = (int(''.join(map(str, population[0]))))
    y_axis_values[i] = int(str(tmp), 2)

    to_print = [0]*int(len(population))
    for j in range(int(len(population))):
        to_print[j] = int(str((int(''.join(map(str, population[j]))))), 2)
    print("Generation: ", i+1, "/// Population Values : ", to_print)

plt.step(x_axis_values, y_axis_values)
plt.show()
