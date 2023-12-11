import random
import time
import numpy as np


<<<<<<< Updated upstream
from task_lpn import lpn_algorithm_str,lpn_algorithm_score

def utility(algorithm_str: str):
    # print("project_meta_utility: [META_UTILITY]")
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
        exec(algorithm_str, globals())
        improved_algorithm_str,improved_algorithm_utility = improve_algorithm(lpn_algorithm_str, lpn_algorithm_score, lpn_utility_str, lpn_utility)
        expected_algorithm_str = improved_algorithm_str
        expected_utility += improved_algorithm_utility / n_tests

        file = open("task_lpn.py", "w")
        stuff = f"""
lpn_algorithm_str = \"""{improved_algorithm_str}\"""
lpn_algorithm_score = {improved_algorithm_utility}
        """
        file.write(stuff)
        file.close()

    return expected_utility

utility_str = \
"""

from task_lpn import lpn_algorithm_str,lpn_algorithm_score

def utility(algorithm_str: str):
    # print("project_meta_utility: [META_UTILITY]")
    \"""
    Evaluates the algorithm in improve_str to improve the algorithm in algorithm_str,
    according to some downstream utility function.
    \"""

    n_tests = 1
    expected_algorithm_str = ""
    expected_utility = 0
    for _ in range(n_tests):
        exec(algorithm_str, globals())
        improved_algorithm_str,improved_algorithm_utility = improve_algorithm(lpn_algorithm_str, lpn_algorithm_score, lpn_utility_str, lpn_utility)
        expected_algorithm_str = improved_algorithm_str
        expected_utility += improved_algorithm_utility / n_tests

        file = open("task_lpn.py", "w")
        stuff = f\"""
lpn_algorithm_str = \"""{improved_algorithm_str}\"""
lpn_algorithm_score = {improved_algorithm_utility}
        \"""
        file.write(stuff)
        file.close()

    return expected_utility
"""

=======
>>>>>>> Stashed changes
# def utility(algorithm_str: str):
#     """
#     Implements the sort utility function. Returns the score.
#     If the algorithm requires more than 100 milliseconds to run per test, it is a failure.
#     """

<<<<<<< Updated upstream
#     exec(algorithm_str, globals())
=======
>>>>>>> Stashed changes
#     try:
#         exec(algorithm_str, globals())
#     except:
#         print("task_utility: [EXEC Algorithm_str NOT WORKING] RETURNING 0")
#         return 0
    
#     A = np.array([17, 15, 61, 81, 86, 41, 97, 58, 74, 32, 18, 91, 10, 28, 72, 16, 3,
#        58, 35, 62,  3, 25, 40, 71, 61, 19, 47, 20, 43, 55, 52, 22, 49, 36,
#         7, 78, 62, 55, 47, 48, 43, 14, 24,  4, 84,  3, 18, 95, 35, 13, 32,
#        78, 75, 40, 98, 46, 60, 77, 87, 43, 18, 47, 89, 33, 82,  4, 27, 26,
#        16, 51, 73, 81, 19, 59, 64, 98, 71,  1, 22,  3, 34, 45, 41, 48, 23,
#         6, 62, 41, 77, 78, 12, 24, 12, 38, 60, 80, 74, 11, 89, 18, 85, 65,
#        16, 20, 72, 37, 25, 90, 81, 45,  3, 45, 15, 18, 68, 12, 79, 50, 32,
#        93, 89, 17, 37, 65,  4, 17, 32, 86, 77, 19])
#     start_time = time.time()
#     print("task_utility: [EXECUTING ALGO]")
#     output = algorithm(A)
#     print(output)
#     print("task_utility: [OUTPUT]", output)
#     total_time = time.time() - start_time
#     print(f"task_utility: [total time] {total_time}")
#     if sorted(A) != list(output):
#        return 0

#     if total_time > 1:
#        return 0

#     # n_tests = 10

#     # for test_idx in range(n_tests):
#     #     # average score for multiple tests
#     #     pass

#     print("task_utility: utility returns " + str(1/total_time))
#     return 1/total_time

# utility_str = \
# """
# def utility(algorithm_str: str):
#     \"""
#     Implements the sort utility function. Returns the score.
#     If the algorithm requires more than 100 milliseconds to run per test, it is a failure.
#     \"""

#     try:
#         exec(algorithm_str, globals())
#     except:
#         return 0
    
#     A = np.array([17, 15, 61, 81, 86, 41, 97, 58, 74, 32, 18, 91, 10, 28, 72, 16, 3,
#        58, 35, 62,  3, 25, 40, 71, 61, 19, 47, 20, 43, 55, 52, 22, 49, 36,
#         7, 78, 62, 55, 47, 48, 43, 14, 24,  4, 84,  3, 18, 95, 35, 13, 32,
#        78, 75, 40, 98, 46, 60, 77, 87, 43, 18, 47, 89, 33, 82,  4, 27, 26,
#        16, 51, 73, 81, 19, 59, 64, 98, 71,  1, 22,  3, 34, 45, 41, 48, 23,
#         6, 62, 41, 77, 78, 12, 24, 12, 38, 60, 80, 74, 11, 89, 18, 85, 65,
#        16, 20, 72, 37, 25, 90, 81, 45,  3, 45, 15, 18, 68, 12, 79, 50, 32,
#        93, 89, 17, 37, 65,  4, 17, 32, 86, 77, 19])
#     start_time = time.time()
#     print("[EXECUTING ALGO]")
#     output = algorithm(A)
#     print(output)
#     print("[OUTPUT]", output)
#     total_time = time.time() - start_time
#     print(f"[total time] {total_time}")
#     if sorted(A) != list(output):
#        return 0

#     if total_time > 1:
#        return 0

#     # n_tests = 10

#     # for test_idx in range(n_tests):
#     #     # average score for multiple tests
#     #     pass

#     print("utility returns " + 1/total_time)
#     return 1/total_time
# """

# LPN UTILITY
def lpn_utility(algorithm_str: str):
    print("utility")
    """
    Implements the parity learning task. Returns the number of correct predictions.
    """

    n_tests = 3
    average_correct = 0

    exec(algorithm_str, globals())
    try:
        exec(algorithm_str, globals())
    except Exception as e: 
        print(e)
        return 0

    for _ in range(n_tests):
        start_time = time.time()
        n_bits = 10
        p_true = 0.3
        n_train_samples = 100
        n_test_samples = 20
        noise_level = 0.05
        true_bits = np.random.binomial(1, p_true, n_bits)

        samples = np.random.binomial(1, 0.5, (n_train_samples + n_test_samples, n_bits))
        masked_samples = samples * true_bits
        parity = np.sum(masked_samples, axis=1) % 2
        train_samples = samples[:n_train_samples]
        train_parity = parity[:n_train_samples]
        parity_noise = np.random.binomial(1, noise_level, n_train_samples)
        train_parity = (train_parity + parity_noise) % 2

        test_samples = samples[n_train_samples:]
        test_parity = parity[n_train_samples:]

        # Because algorithm is a string, we can’t call it directly. Instead, we can use eval to
        # evaluate it as a Python expression.
        try:
            predictions = algorithm(train_samples, train_parity, test_samples)
            test_parity = np.array(test_parity).reshape(-1)
            predictions = np.array(predictions).reshape(-1)
            correct = np.sum(predictions == test_parity) / n_test_samples
        except:
            correct = 0
        # Use no more than 100 milliseconds per test
        if time.time() - start_time > 0.1:
            return 0
        average_correct += correct / n_tests

    return average_correct

lpn_utility_str = \
"""
def utility(algorithm_str: str):
    \"""
    Implements the parity learning task. Returns the number of correct predictions.
    \"""

    n_tests = 3
    average_correct = 0

    try:
        exec(algorithm_str, globals())
    except:
        return 0

    for _ in range(n_tests):
        start_time = time.time()
        n_bits = 10
        p_true = 0.3
        n_train_samples = 100
        n_test_samples = 20
        noise_level = 0.05
        true_bits = np.random.binomial(1, p_true, n_bits)

        samples = np.random.binomial(1, 0.5, (n_train_samples + n_test_samples, n_bits))
        masked_samples = samples * true_bits
        parity = np.sum(masked_samples, axis=1) % 2
        train_samples = samples[:n_train_samples]
        train_parity = parity[:n_train_samples]
        parity_noise = np.random.binomial(1, noise_level, n_train_samples)
        train_parity = (train_parity + parity_noise) % 2

        test_samples = samples[n_train_samples:]
        test_parity = parity[n_train_samples:]

        # Because algorithm is a string, we can’t call it directly. Instead, we can use eval to
        # evaluate it as a Python expression.
        try:
            predictions = algorithm(train_samples, train_parity, test_samples)
            test_parity = np.array(test_parity).reshape(-1)
            predictions = np.array(predictions).reshape(-1)
            correct = np.sum(predictions == test_parity) / n_test_samples
        except:
            correct = 0
        # Use no more than 100 milliseconds per test
        if time.time() - start_time > 0.1:
            return 0
        average_correct += correct / n_tests

    return average_correct
"""