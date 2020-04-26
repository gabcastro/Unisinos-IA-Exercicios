import io
import pandas as pd
from genetic_algorithm import Genetic_Algorithm

class EvaluateGC:
    # during initialization, store the problem instance
    def __init__(self, problem_instance):
        self.problem_instance = problem_instance
    
    # compute the value of the received solution
    def __call__(self, solution):
        return sum(solution[n1] != solution[n2] for (n1, n2) in self.problem_instance.values())


def main():

    df = pd.read_csv('D:\\Repositórios\\GitHub\\Personal\\Unisinos-IA-Exercicios\\GA\\connected_countries.txt', header=None)
    df.rename(columns={
        0: 'x_country',
        1: 'y_country'
    }, inplace=True)

    problem_length = (int(df.iloc[0]['x_country']), int(df.iloc[0]['y_country']))

    countries = {
        0: 'BR',
        1: 'UY',
        2: 'PY',
        3: 'AR',
        4: 'BO', 
        5: 'CH', 
        6: 'PE',
        7: 'CO', 
        8: 'EC',
        9: 'VE'
    }

    connected_countries = {}

    for index, row in df.tail(len(df)-1).iterrows():
        str_countries = countries.get(row['x_country']) + '-' + countries.get(row['y_country'])
        connected_countries[str_countries] = [row['x_country'], row['y_country']]

    # set of possible colours (pink, orange, green, gray, purple, yellow, blue)
    possible_values = ['P', 'O', 'GN', 'GY', 'P', 'Y', 'B'] 

    # length of an individual (one position per territory)
    individual_length = problem_length[0]

    # population size
    population_size = 8

    gen_alg = Genetic_Algorithm()

    # initial population
    population = gen_alg.init_population(population_size, possible_values, individual_length)

    fn_fitness = EvaluateGC(connected_countries)
    
    # run the algoritm
    solution = gen_alg.genetic_algorithm(population, fn_fitness, gene_pool=possible_values, fn_thres=10)

    # print the results
    print('Resulting solution: %s' % solution)
    print('Value of resulting solution: %d' % fn_fitness(solution))

    # print('222')


if __name__ == "__main__":
    main()