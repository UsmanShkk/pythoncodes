import random


def create_distance_matrix(n):
    return [[random.randint(10, 100) if i != j else 0 for j in range(n)] for i in range(n)]


def initialize_population(pop_size, n):
    return [random.sample(range(n), n) for _ in range(pop_size)]


def calculate_distance(tour, dist_matrix):
    return sum(dist_matrix[tour[i]][tour[i + 1]] for i in range(len(tour) - 1)) + dist_matrix[tour[-1]][tour[0]]


def select_parents(population, dist_matrix):
    population.sort(key=lambda x: calculate_distance(x, dist_matrix))
    return population[:2]


def crossover(parent1, parent2):
    cut = len(parent1) // 2
    child = parent1[:cut] + [gene for gene in parent2 if gene not in parent1[:cut]]
    return child


def mutate(tour):
    i, j = random.sample(range(len(tour)), 2)
    tour[i], tour[j] = tour[j], tour[i]


def genetic_algorithm_tsp(n, pop_size, generations):
    dist_matrix = create_distance_matrix(n)
    population = initialize_population(pop_size, n)

    for _ in range(generations):
        new_population = []

        for _ in range(pop_size // 2):
            parents = select_parents(population, dist_matrix)
            child1, child2 = crossover(parents[0], parents[1]), crossover(parents[1], parents[0])
            mutate(child1)
            mutate(child2)
            new_population.extend([child1, child2])

        population = new_population

    best_tour = min(population, key=lambda tour: calculate_distance(tour, dist_matrix))
    return best_tour, calculate_distance(best_tour, dist_matrix)


n, pop_size, generations = 5, 6, 10
best_tour, best_distance = genetic_algorithm_tsp(n, pop_size, generations)
print("Best Tour:", best_tour)
print("Best Distance:", best_distance)
