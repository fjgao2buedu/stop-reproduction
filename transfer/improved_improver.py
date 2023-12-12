from helpers import extract_code, prompt

def improve_algorithm(initial_solution, initial_score, utility_str, utility):
    """Improves a solution according to a utility function."""
    role = "You are an expert computer science researcher and programmer, especially skilled at optimizing algorithms."

    temperature_values = [0.4]#, 0.7, 1.0]
    solutions_cache = set()
    new_solutions = []
    utility_cache = {}

    def evaluate_solution(solution):
        if solution not in utility_cache:
            utility_cache[solution] = utility(solution)
        return utility_cache[solution]
    
    for temp in temperature_values:
        base_message = f"""Improve the following solution:
‘‘‘python
{initial_solution}
‘‘‘
You will be evaluated based on this score function:
‘‘‘python
{utility_str}
‘‘‘

You must return an improved solution. Be as creative as you can under the constraints.
Your primary improvement must be novel and non-trivial. Generate a solution with temperature={temp}, 
that focuses on different aspects of optimization. 
Do not generate a utility function. 
Do not remove current imports.
Do not change "algorithm" function signature."""
        
        generated_solutions = prompt(base_message, temperature=temp)
        generated_solutions = extract_code(generated_solutions)

        # Evaluate and sort the generated solutions by their utility score
        scored_solutions = [(sol, evaluate_solution(sol)) for sol in generated_solutions if sol not in solutions_cache]
        scored_solutions.sort(key=lambda x: x[1], reverse=True)

        for sol, _ in scored_solutions:
            new_solutions.append(sol)
            solutions_cache.add(sol)

        print("[improved_improver.py] Initial solution", initial_solution)
        print("[improved_improver.py] eval iniital", evaluate_solution(initial_solution))
        print("[improved_improver.py] improved solutions:", evaluate_solution(sol))
        # Dynamically adjust temperature values based on the utility scores
        temperature_values = [temp * (1 + evaluate_solution(sol) / evaluate_solution(initial_solution)) for temp, sol in zip(temperature_values, new_solutions)]
    
 
    best_solution = max(new_solutions, key=evaluate_solution)

    print("[improved_improver.py] Best solution:", best_solution)
    print("[improved_improver.py] utility of best solution:", utility_cache[best_solution])
    return best_solution, utility_cache[best_solution]