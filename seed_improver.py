from helpers import extract_code, prompt


def improve_algorithm(initial_solution, initial_score, utility_str, utility):
    """
    Improves a solution according to a utility function.
    """
    role = "You are an expert computer science researcher and programmer, especially skilled at optimizing algorithms."
    message = \
    f"""
    You must improve the following code. You will be evaluated based on a following score function: 
    ‘‘‘python
    {utility_str} 
    ‘‘‘
    Here is the current solution: 
    ‘‘‘python
    {initial_solution}
    ‘‘‘
    When run, your script must define an improved solution. Try to be as creative as possible under the constraints.
    Your primary improvement must be novel and non-trivial. First, propose an idea for an improvement, then implement it.
    You are not allowed to output a "utility" python function. DO NOT remove "from helpers import extract_code, prompt".
    """
    new_solutions = prompt(message, temperature=0.7)
    new_solutions = extract_code(new_solutions)
    best_solution, best_utility = initial_solution, initial_score
    print("seed_improver: [NEW SOLUTION]", new_solutions[0])
    for new_solution in new_solutions:
        utility_val = utility(new_solution)
        print("seed_improver: [BEST UTILITY BEFORE EVAL]", best_utility)
        print("seed_improver: [CURR UTILITY ]", utility_val)
        if utility_val > best_utility:
            best_solution = new_solution
            best_utility = utility_val
            print("seed_improver: [BEST SOLUTION UTILITY]:", best_utility)
            print("seed_improver: [BEST SOLUTION]:", best_solution)
    return best_solution, best_utility
