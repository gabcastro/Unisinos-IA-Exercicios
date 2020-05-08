import io
import pandas as pd
import matplotlib.pyplot as plt
from genetic_algorithm import GeneticAlgorithm

class EvaluateGC:
    # during initialization, store the problem instance
    def __init__(self, problem_instance):
        self.problem_instance = problem_instance
    
    # compute the value of the received solution
    def __call__(self, solution):
        return sum(solution[n1] != solution[n2] for (n1, n2) in self.problem_instance.values())


def exectute_pop(num_colors, n_runs):
    """Running pipeline to solve problem
    
    Keywords arguments:
        num_colors      - number of colors to set 
        n_runs          - number of executions
    """

    df = pd.read_csv('D:\\Repositórios\\GitHub\\Personal\\Unisinos-IA-Exercicios\\Trabalho_GA\\connected_countries.txt', header=None, delim_whitespace=True)
    df.rename(columns={
        0: 'x_country',
        1: 'y_country'
    }, inplace=True)

    problem_length = (int(df.iloc[0]['x_country']), int(df.iloc[0]['y_country']))

    countries = {
        0: 'BR',    # Brasil
        1: 'UY',    # Uruguai
        2: 'PY',    # Paraguai
        3: 'AR',    # Argentina
        4: 'BO',    # Bolívia
        5: 'CH',    # Chile
        6: 'PE',    # Peru
        7: 'CO',    # Colômbia
        8: 'EC',    # Ecuador
        9: 'VE',    # Venezuela
        10: 'GY',   # Guiana
        11: 'SR',   # Suriname
        12: 'GF',   # Guiana Francesa
        13: 'PA',   # Panamá
        14: 'CR'    # Costa Rica
    }

    connected_countries = {}

    for index, row in df.tail(len(df)-1).iterrows():
        str_countries = countries.get(row['x_country']) + '-' + countries.get(row['y_country'])
        connected_countries[str_countries] = [row['x_country'], row['y_country']]

    # set of possible colours (pink, orange, green, gray, purple, yellow, blue, red, white, brown, black)
    possible_values = ['P', 'O', 'GN', 'GY', 'P', 'Y', 'B', 'R', 'W', 'BR', 'BK'] 

    colors = [possible_values[j] for j in range(num_colors)]

    # length of an individual (one position per territory)
    individual_length = problem_length[0]

    # population size
    population_size = [3, 20, 200]

    dict_avg_pop = {}
    
    for i in population_size:
        dict_avg_pop[str(i)] = []

    # evaluation class
    fn_fitness = EvaluateGC(connected_countries)

    for i in range(n_runs):
        
        # instance of generic algorithm
        gen_alg = GeneticAlgorithm()

        # list to record solutions for each population 
        solutions = []

        for p in population_size:

            # initial population
            population = gen_alg.init_population(p, colors, individual_length)

            # run the algoritm
            solution = gen_alg.genetic_algorithm(population, fn_fitness, gene_pool=colors, fn_thres=problem_length[1])

            solutions.append(solution)

        ps = 1
        for s in solutions:
            # print the results
            val = fn_fitness(s)
            print('|    {}º population   ---   Length: {}     |'.format(ps, population_size[ps-1]))
            print('Resulting solution: %s' % s)
            print('Value of resulting solution: %d\n' % val)
            
            lista_temp = dict_avg_pop.get(str(population_size[ps-1]))
            lista_temp.append(val)
            dict_avg_pop[str(population_size[ps-1])] = lista_temp

            ps += 1

    return dict_avg_pop


def main():
    dict_avg_pop = exectute_pop(7, 3)

    avg_pop = []
    groups = []
    for population, list_values in dict_avg_pop.items():
        groups.append(population)
        avg_pop.append(sum(list_values) / len(list_values))

    plt.figure(figsize=(9, 3))

    plt.subplot(131)
    plt.bar(groups, avg_pop)

if __name__ == "__main__":
    main()