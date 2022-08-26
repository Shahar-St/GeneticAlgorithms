# Genetic Algorithms

Developers: [Shahar-St](https://github.com/Shahar-St) and [GalMirovsky](https://github.com/GalMirovsky)

## What is this project?

Solving NP-Hard problems using Genetic and other AI algorithms.

This is the main repo, some problems/algorithms are in other repos.

## Algorithms
- Genetic Algorithm with the option to provide multiple variations:
  - Crossovers: Single Point Crossover, Two Point Crossover, UniformCrossover
  - Fitness functions: Bulls And Cows
  - Continuation Rules: Aging, Elite
  - Mutations: Flip Mutation, Scramble Mutation
- PSO (Particle swarm optimization)
- Minimal Conflict
- Ant Colony Optimization
- Simulated Annealing
- Tabu Search
- Forward Checking
- Back Jumping
- Objective Minimizer

## Problems
- CVRP (Capacitated Vehicle Routing Problem)
- Edge Coloring
- Multi-Dimentions Knapsack
- N-Queens
- Knapsack

## How can I run it?
`Python main.py`

There are multiple flags that can be used (some restrictions apply)

`-c` The crossover method. Optional values: `singlePointCrossover`, `TwoPointCrossover`, `UniformCrossover`. default is based on the problem

`-f` The fitness function to use. Optional values: `BullsAndCows`, `AsciiDistance`. default is based on the problem

`-a` The algorithm to use in order to solve the problem. Optional values: `GeneticAlgorithm`, `PSO`, `MinimalConflict`. default: `GeneticAlgorithm`

`-s` The parent selction method. Optional values: `NaiveParentSelection`, `RWS`, `SUS`, `DeterministicTournament`, `StochasticTournament`. default: `NaiveParentSelection`

`-r` The continuation rule method. Optional values: `EliteRule`, `AgingRule`. default: `EliteRule`

`-p` The problem to solve. Optional values: `NQueens`, `StringMatching`. default: `StringMatching`

`-m` The mutation method to use. Optional values: `FlipMutation`, `ScrambleMutation`, `KnapsackFlipMutation`. default is based on the problem

