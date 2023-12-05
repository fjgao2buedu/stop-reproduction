# from language_model import LanguageModel
# from helpers import extract_code

from openai import OpenAI
client = OpenAI()

role = "You are an expert computer science researcher and programmer, especially skilled at optimizing algorithms."

def prompt(message,temperature):
    response = client.chat.completions.create(
    model="gpt-3.5-turbo-1106",
    response_format={ "type": "text" },
    messages=[
        {"role": "system", "content": role},
        {"role": "user", "content": message}
    ],
    temperature=temperature
    )
    print(response.choices[0].message.content)
    return response.choices

import re

def extract_code(responses):
    """
    Extracts code snippets from a batch of text.
    This example assumes Python code enclosed in triple backticks for simplicity.
    """

    solutions = []
    pattern = r'```python(.*?)```'  # Regex pattern to extract Python code blocks

    for response in responses:
        matches = re.findall(pattern, response.message.content, re.DOTALL)
        solutions.extend(matches)

    return solutions

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
    new_solutions = prompt(message, temperature=0.7)
    new_solutions = extract_code(new_solutions)
    best_solution, best_utility = initial_solution, 0
    for new_solution in new_solutions:
        utility_val = utility(new_solution)
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


def improve_algorithm(initial_solution, utility_str, utility):
    """Improves a solution according to a utility function."""
    role = "You are an expert computer science researcher and programmer, especially skilled at optimizing algorithms."
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
    
    new_solutions = prompt(message, temperature=0.7)
    new_solutions = extract_code(new_solutions)
    best_solution, best_utility = initial_solution, 0
    for new_solution in new_solutions:
        utility_val = utility(new_solution)
        if utility_val > best_utility:
            best_solution = new_solution
            best_utility = utility_val
    return best_solution

def meta_utility(improve_str: str):
    """
    Evaluates the algorithm in improve_str to improve the algorithm in algorithm_str, 
    according to some downstream utility function. 
    """
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

algorithm_str = """
def algorithm(a):
    return a
"""
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

def utility(algorithm_str: str):
    """
    Implements the sort utility function. Returns the score.
    If the algorithm requires more than 100 milliseconds to run per test, it is a failure.
    """

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