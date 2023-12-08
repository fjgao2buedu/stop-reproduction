# from language_model import LanguageModel

from openai import OpenAI
import os
from dotenv import load_dotenv
import json
import numpy as np
import time
from helpers import extract_code
from task_utility import utility, utility_str

load_dotenv()



client = OpenAI(
    api_key=os.getenv("OPENAI_API_KEY"),
)

role = "You are an expert computer science researcher and programmer, especially skilled at optimizing algorithms."

prompt_count = 0


def prompt(message,temperature):
    response = client.chat.completions.create(
    model="gpt-3.5-turbo-1106", #gpt-4-0314
    response_format={ "type": "text" },
    messages=[
        {"role": "system", "content": role},
        {"role": "user", "content": message}
    ],
    temperature=temperature
    )
    print(response.choices[0].message.content)
    # prompt_count += 1
    return response.choices

# SEED IMPROVER
initial_solution = \
"""
def improve_algorithm(initial_solution, utility_str, utility):
    \"""Improves a solution according to a utility function.\"""
    role = "You are an expert computer science researcher and programmer, especially skilled at optimizing algorithms."
    message = f\"""You must improve the following code. You will be evaluated based on a following score function: 
    ‘‘‘python
    {utility_str} 
    ‘‘‘
    Here is the current solution: 
    ‘‘‘python
    {initial_solution}
    ‘‘‘
    When run, your script must define an improved solution. Try to be as creative as possible under the constraints.
    Your primary improvement must be novel and non-trivial. First, propose an idea for an improvement, then implement it.\"""
    print("PROMPTING NEW SOLUTIONS")
    new_solutions = prompt(message, temperature=0.7)
    print("[BEFORE EXTRACT CODE]")
    new_solutions = extract_code(new_solutions)
    print("[NEW SOLUTIONS]")
    print(new_solutions)
    
    best_solution, best_utility = initial_solution, 0

    for new_solution in new_solutions:
        print("[EVAL NEW SOLUTION]")
        print(new_solution)
        utility_val = utility(new_solution) ### StUCK HERE
        print("[UTIL VALUE]", utility_val)
        if utility_val > best_utility:
            best_solution = new_solution
            best_utility = utility_val
    return best_solution"""

meta_utility_str = \
"""
def meta_utility(improve_str: str):
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


# def improve_algorithm_1(initial_solution, utility_str, utility): # NOT USING, SAME AS STRING ABOVE
#     """Improves a solution according to a utility function."""
#     role = "You are an expert computer science researcher and programmer, especially skilled at optimizing algorithms."
#     message = f"""You must improve the following code. You will be evaluated based on a following score function: 
#     ‘‘‘python
#     {utility_str} 
#     ‘‘‘
#     Here is the current solution: 
#     ‘‘‘python
#     {initial_solution}
#     ‘‘‘
#     When run, your script must define an improved solution. Try to be as creative as possible under the constraints.
#     Your primary improvement must be novel and non-trivial. First, propose an idea for an improvement, then implement it."""
    
#     new_solutions = prompt(message, temperature=0.7)
#     new_solutions = extract_code(new_solutions)
#     print('NEW_SOLUTION')
#     best_solution, best_utility = initial_solution, 0
#     for new_solution in new_solutions:
#         utility_val = utility(new_solution)
#         if utility_val > best_utility:
#             best_solution = new_solution
#             best_utility = utility_val
#     return best_solution


# INITIAL
algorithm_str = """
def algorithm(a, b , c):
    return a
"""

def meta_utility(improve_str: str):
    """
    Evaluates the algorithm in improve_str to improve the algorithm in algorithm_str, 
    according to some downstream utility function. 
    """
    # if meta_utility.uses > meta_utility.budget:
    #     return 0
    # meta_utility.increment_uses()

    n_tests = 2
    expected_utility = 0
    print('metautl')
    for _ in range(n_tests):
        exec(improve_str, globals())
        improved_algorithm_str = improve_algorithm(algorithm_str, utility_str, utility)

        print('[IMRPOVE ALGO]')
        print(improved_algorithm_str)
        expected_utility += utility(improved_algorithm_str) / n_tests
    
        # if utility.uses >= utility.budget:
        #     break
        # try:
        #     # exec(improve_str, globals())  # Define improve_algorithm function
        #     # At most 6 calls to language model, and at most 6 samples each time
        #     # language_model = LanguageModel(budget=6, max_responses_per_call=6)
        #     improved_algorithm_str = improve_algorithm_1(algorithm_str, utility_str, utility)
        #     print('[IMRPOVE ALGO]')
        #     print(improved_algorithm_str)
        #     expected_utility += utility(improved_algorithm_str) / n_tests





        # except:
        #     print('EXEPTION IN METAUTILITY')
        #     continue
    print(expected_utility)    
    return expected_utility

# algorithm_str = """
# def algorithm(a):
#     return a
# """
utility_str = """
def utility(algorithm_str: str):
    \"""
    Implements the sort utility function. Returns the score.
    If the algorithm requires more than 100 milliseconds to run per test, it is a failure.
    \"""

    try:
        exec(algorithm_str, globals())
    except:
        return 0
    
    A = np.random.randint(0, 100, size=(13,))
    start_time = time.time()
    output, _ = algorithm(A)
    total_time = time.time() - start_time

    if sorted(A) != output:
       return 0

    if total_time > 0.1:
       return 0

    n_tests = 10

    for test_idx in range(n_tests):
        # average score for multiple tests
        pass

    return 1
"""


message = f"""You must improve the following code. You will be evaluated based on a following score function: 
‘‘‘python
{utility_str} 
‘‘‘
Here is the current solution: 
‘‘‘python
{initial_solution}
‘‘‘
When run, your script must define an improved solution. Try to be as creative as possible under the constraints.
Your primary improvement must be novel and non-trivial. First, propose an idea for an improvement, then implement it."""
print(message)


print("--------------------------------------")
print()
print('-----------------------')

meta_utility(initial_solution)
