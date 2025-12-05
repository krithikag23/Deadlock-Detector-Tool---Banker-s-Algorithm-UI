from typing import List, Tuple, Dict

def compute_need(max_demand: List[List[int]],
                 allocation: List[List[int]]) -> List[List[int]]:
    """
    need[i][j] = max_demand[i][j] - allocation[i][j]
    """
    n = len(max_demand)
    m = len(max_demand[0]) if n > 0 else 0
    need = [[0] * m for _ in range(n)]
    for i in range(n):
        for j in range(m):
            need[i][j] = max_demand[i][j] - allocation[i][j]
    return need