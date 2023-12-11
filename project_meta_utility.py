from task_utility import utility, utility_str
from task import algorithm_str, algorithm_score

def meta_utility(improve_str: str):
    print("project_meta_utility: [META_UTILITY]")
    """
    Evaluates the algorithm in improve_str to improve the algorithm in algorithm_str,
    according to some downstream utility function.
    """
    # if meta_utility.uses > meta_utility.budget:
    #     return 0
    # meta_utility.increment_uses()
    n_tests = 1
    expected_algorithm_str = ""
    expected_utility = 0
    for _ in range(n_tests):
        exec(improve_str, globals())
        print("project_meta_utility: [ALGO BEFORE IMPROVEMENT]")
        print(algorithm_str)
        print("project_meta_utility: [ALGO SCORE BEFORE IMPROVEMENT]")
        print(algorithm_score)
        improved_algorithm_str,improved_algorithm_utility = improve_algorithm(algorithm_str, algorithm_score, utility_str, utility)
        expected_algorithm_str = improved_algorithm_str
        expected_utility += improved_algorithm_utility / n_tests

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
    # print(expected_algorithm_str, expected_utility)
    return expected_algorithm_str, expected_utility
