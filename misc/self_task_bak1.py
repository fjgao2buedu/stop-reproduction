
algorithm_str = """
from helpers import extract_code, prompt

def utility(algorithm_str: str):
    """
    Evaluates the algorithm in improve_str to improve the algorithm in algorithm_str,
    according to some downstream utility function.
    """
    n_tests = 1
    improved_algorithm_str, improved_algorithm_utility = "", 0
    for _ in range(n_tests):
        improved_algorithm_str, improved_algorithm_utility = improve_algorithm(algorithm_str, algorithm_score, utility_str, utility)
    return improved_algorithm_str, improved_algorithm_utility

def improve_algorithm(initial_solution, initial_score, utility_str, utility):
    """
    Improves a solution according to a utility function.
    """
    role = "You are an expert computer science researcher and programmer, especially skilled at optimizing algorithms."
    message = f"""
    You must improve the following code. You will be evaluated based on a following score function: 
    ```python
    {utility_str} 
    ```
    Here is the current solution: 
    ```python
    {initial_solution}
    ```
    When run, your script must define an improved solution. Try to be as creative as possible under the constraints.
    Your primary improvement must be novel and non-trivial. First, propose an idea for an improvement, then implement it.
    You are not allowed to output a "utility" python function. DO NOT remove "from helpers import extract_code, prompt".
    """
    new_solutions = prompt(message, temperature=0.7)
    new_solutions = extract_code(new_solutions)
    best_solution = (initial_solution, initial_score)
    
    for new_solution in new_solutions:
        utility_val = utility(new_solution)
        if utility_val > best_solution[1]:
            best_solution = (new_solution, utility_val)
            
    return best_solution
"""
algorithm_score = 0.6666666666666666
