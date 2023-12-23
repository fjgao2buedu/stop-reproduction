from project_meta_utility import meta_utility


# SEED IMPROVER backup (not used)
initial_solution_bak = \
"""
from helpers import extract_code, prompt


def improve_algorithm(initial_solution, initial_score, utility_str, utility):
    \"""
    Improves a solution according to a utility function.
    \"""
    role = "You are an expert computer science researcher and programmer, especially skilled at optimizing algorithms."
    message = \
    f\"""
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
    DO NOT output a utility function.
    \"""
    new_solutions = prompt(message, temperature=0.7)
    new_solutions = extract_code(new_solutions)
    best_solution, best_utility = initial_solution, initial_score
    for new_solution in new_solutions:
        utility_val = utility(new_solution)
        print("project_seed_improver: [BEST UTILITY BEFORE EVAL]", best_utility)
        print("project_seed_improver: [CURR UTILITY ]", utility_val)
        if utility_val > best_utility:
            best_solution = new_solution
            best_utility = utility_val
            print("project_seed_improver: [BEST SOLUTION UTILITY]:", best_utility)
            print("project_seed_improver: [BEST SOLUTION]:", best_solution)
    return best_solution, best_utility

"""

meta_utility_str = \
"""
def meta_utility(improve_str: str):
    print("project_meta_utility: [META_UTILITY]")
    \"""
    Evaluates the algorithm in improve_str to improve the algorithm in algorithm_str, 
    according to some downstream utility function. 
    \"""
    if meta_utility.uses > meta_utility.budget:
        return 0
    meta_utility.increment_uses()

    n_tests = 1
    expected_utility = 0
    for _ in range(n_tests):
        if utility.uses >= utility.budget:
            break
        try:
            exec(improve_str, globals())  # Define improve_algorithm function
            # At most 6 calls to language model, and at most 6 samples each time
            # language_model = LanguageModel(budget=6, max_responses_per_call=6)
            improved_algorithm_str = improve_algorithm(algorithm_str, utility_str, utility)
            expected_utility += utility(improved_algorithm_str) / n_tests
        except:
            continue
        
    return expected_utility

"""

# def meta_utility(improve_str: str):

#     """
#     Evaluates the algorithm in improve_str to improve the algorithm in algorithm_str, 
#     according to some downstream utility function. 
#     """
#     # if meta_utility.uses > meta_utility.budget:
#     #     return 0
#     # meta_utility.increment_uses()
#     global algorithm_str
#     n_tests = 2
#     expected_utility = 0
#     print('metautl')
#     for _ in range(n_tests):
#         exec(improve_str, globals())
#         improved_algorithm_str = improve_algorithm(algorithm_str, utility_str, utility)

#         expected_utility += utility(improved_algorithm_str) / n_tests
    
#         # if utility.uses >= utility.budget:
#         #     break
#         # try:
#         #     # exec(improve_str, globals())  # Define improve_algorithm function
#         #     # At most 6 calls to language model, and at most 6 samples each time
#         #     # language_model = LanguageModel(budget=6, max_responses_per_call=6)
#         #     improved_algorithm_str = improve_algorithm_1(algorithm_str, utility_str, utility)
#         #     print('[IMRPOVE ALGO]')
#         #     print(improved_algorithm_str)
#         #     expected_utility += utility(improved_algorithm_str) / n_tests

#         # except:
#         #     print('EXEPTION IN METAUTILITY')
#         #     continue
#     print(expected_utility)    
#     return expected_utility



print("==============================================================================================")
print("==============================================================================================")
print("==============================================================================================")

file = open("seed_improver.py", "r")
initial_solution = file.read()
file.close()

sol,score = meta_utility(initial_solution)

file = open("task.py", "w")
stuff = f"""
algorithm_str = \"""{sol}\"""
algorithm_score = {score}
"""
file.write(stuff)
file.close()
