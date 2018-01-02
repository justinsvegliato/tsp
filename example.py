import solver
import tsp

def main():
    states = tsp.get_instance(10, 0, 10000, 10)
    start_state = list(states)[0]
    statistics = {'time': [], 'distances': []}

    print('Initial Tour:', states)
    print('Solving TSP...')
    optimal_tour = solver.k_opt_solve(states, start_state, statistics, 1000)
    print('Optimal Tour:', optimal_tour)


if __name__ == '__main__':
    main()