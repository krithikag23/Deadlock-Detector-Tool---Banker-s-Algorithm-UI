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

def bankers_safety(
    allocation: List[List[int]],
    max_demand: List[List[int]],
    available: List[int],
) -> Tuple[bool, List[int], Dict[str, List[List[int]]]]:
    """
    Return (is_safe, safe_sequence, extra_info)

    extra_info contains:
      - 'need': Need matrix
      - 'work_sequence': list of work vectors after each allocation
    """
    n = len(allocation)   # processes
    m = len(allocation[0]) if n > 0 else 0  # resources

    need = compute_need(max_demand, allocation)

    work = available[:]
    finish = [False] * n
    safe_sequence: List[int] = []
    work_sequence: List[List[int]] = [work[:]]

    while len(safe_sequence) < n:
        progress = False

        for i in range(n):
            if not finish[i]:
                # Check if need[i] <= work for all resources
                if all(need[i][j] <= work[j] for j in range(m)):
                    # This process can finish
                    for j in range(m):
                        work[j] += allocation[i][j]
                    finish[i] = True
                    safe_sequence.append(i)
                    work_sequence.append(work[:])
                    progress = True

        if not progress:
            # No process could be allocated in this iteration
            break

    is_safe = all(finish)

    extra_info = {
        "need": need,
        "work_sequence": work_sequence,
    }

    return is_safe, safe_sequence, extra_info
