# Genetic Algorithm Example

This code represents my first foray into the world of programming during my studies as a Civil Engineering student at UFOB (Federal University of Western Bahia). The primary goal was to explore genetic algorithms and their application in optimizing structural designs

## Getting Started

1. **Prerequisites**:
   - Python 3.x installed on your system.
   - Basic understanding of genetic algorithms.
2. **Installation**:
   - Clone this repository to your local machine.
   - Open a terminal and navigate to the project directory.
3. **Usage**:
   - Run the `genetic_algorithm.py` script.
   - Follow the prompts to set the number of generations, gene quantities, and chromosome quantities.
   - Observe the algorithm’s progress as it evolves the population.

## Algorithm Overview

1. **Initialization**:
   - Create an initial population of random binary chromosomes.
   - Evaluate each chromosome’s fitness using the given function.
2. **Selection**:
   - Select the best-performing chromosomes (based on fitness) to form the next generation.
3. **Crossover**:
   - Combine pairs of selected chromosomes to create offspring.
   - Perform crossover (exchange of genetic material) to create new chromosomes.
4. **Mutation**:
   - Introduce random mutations (flips) in the offspring’s genes.
5. **Repeat**:
   - Repeat steps 2-4 for a specified number of generations.
6. **Results**:
   - The algorithm converges toward an optimal solution (maximizing the given function).

## Example Output

```
Choose the number of generations: 50
Choose the gene quantities in each chromosome: 10
Choose the chromosome quantities in the population: 20

Generation: 1 /// Population Values: [123, 45, ...]
...
Generation: 50 /// Population Values: [456, 789, ...]
```
