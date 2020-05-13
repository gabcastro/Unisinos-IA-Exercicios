import random

# evaluation class; 
# since that a solution needs to be evaluated with respect to the problem instance 
# in consideration, we created this class to store the problem instance and to 
# allow the evaluation to be performed without having the problem instance at hand
class EvaluateNQueens:
    # during initialization, store the problem instance
    def __init__(self, problem_instance):
        self.problem_instance = problem_instance
    
    # compute the value of the received solution
    def __call__(self, solution):
        conflicts = 0

        for (c1, r1) in enumerate(solution):
          for (c2, r2) in enumerate(solution):
            if c2 <= c1:
              continue
            if (r1, c1) != (r2, c2):
              if (r1 == r2) or (c1 == c2) or (r1 - c1 == r2 - c2) or (r1 + c1 == r2 + c2):
                conflicts+=1

        return -conflicts 



def hill_climbing(init_state, fn_neighbours, fn_evaluate, possible_values, iterations=10000):
    
    current = init_state

    while iterations:

        # explore the neighbourhood
        neighbors = fn_neighbours(current, possible_values)
        if not neighbors:
            break
        
        # select the best neighbour
        neighbor = argmax_random_tie(neighbors, key=lambda node: fn_evaluate(node))

        # store the neighbour only if it is better than the current solution
        if fn_evaluate(neighbor) > fn_evaluate(current):
           current = neighbor
        iterations -= 1
        
    return current

# return the best element from the received list; ties are break uniformly at random
def argmax_random_tie(seq, key=lambda x: x):
    items = list(seq)
    random.shuffle(items)
    return max(items, key=key)


def find_neighbours_NQueens(state, possible_values):
    
    # list of neighbours
    neighbours = []

    # for each position (i.e., territory)
    for i in range(len(state)):
        # for each possible value (i.e., colour)
        for v in possible_values:
            # if the change generates a new neighbour, create it and add to the neighbourhood list
            if state[i] != v:
              neighbour = state[:]
              neighbour[i] = v
              neighbours.append(neighbour)
    
    return neighbours

def main():
    # number of n-queens
    n = 8

    # create an instance of the evaluation class for the considered problem instance
    fn_evaluate = EvaluateNQueens(n)

    # set of possible values 
    possible_values = [x for x in range(n)]

    # initial state (we begin with a solution where all queens are on the same row)
    init_state = [0 for _ in range(n)]

    # run the algoritm
    best = hill_climbing(init_state, find_neighbours_NQueens, fn_evaluate, possible_values)

    # print the results
    print('Resulting solution: %s' % best)
    print('Value of resulting solution: %d' % fn_evaluate(best))


if __name__ == "__main__":
    main()