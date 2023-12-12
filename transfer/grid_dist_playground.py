import random
import time
        
def utility(algorithm):#algorithm_str: str):
    """Implements the str_grid_dist task. Returns a value between 0 and 1."""
    # exec(algorithm_str, globals())
    # try:
    #     exec(algorithm_str, globals())
    # except:
    #     return 0.0

    scores = []
    for _ in range(10):
        length = random.randint(1, 30)
        t = "".join(random.choice("AB") for _ in range(length))
        s = "".join(random.choice("AB") for _ in range(length))
        print(t)
        dist = algorithm(s, t)
        #print(dist)
        scores.append(score_test(t, dist, algorithm))

    return sum(scores) / len(scores)

    
def score_test(t: str, dist: int, find_at_dist: callable, max_time=0.1) -> float:
    start_time = time.time()
    s = find_at_dist(t, dist)
    try:
        print("ERRRO")
        s = find_at_dist(t, dist)
        print('wow')
        d = algorithm(s, t)
        if time.time() - start_time > max_time:
            return 0.0
        if d == dist:
            return 1.0 # perfect!
        else:
            return 0.5 - abs(d - dist)/(6*len(t)) # between 0 and 0.5
    except:
        return 0.0 # error
    
def algorithm(s: str, t: str):
    # assert isinstance(s, str) 
    # assert isinstance(t, str) 
    #and len(s) == len(t) and set(s + t) <= set("AB")
    ans = sum(a != b for a, b in zip(s, t))
    ans += sum(a != b for a, b in zip(s, s[1:]))
    ans += sum(a != b for a, b in zip(t, t[1:]))
    return ans

algorithm_str = """
def algorithm(s: str, t: str):
    # assert isinstance(s, str) 
    # assert isinstance(t, str) 
    #and len(s) == len(t) and set(s + t) <= set("AB")
    ans = sum(a != b for a, b in zip(s, t))
    ans += sum(a != b for a, b in zip(s, s[1:]))
    ans += sum(a != b for a, b in zip(t, t[1:]))
    return ans
"""

# print(utility(algorithm_str))
print((0.42328487872465886+0.5390674603174604+0.40725511695906436+0.41923656206231835)/4)