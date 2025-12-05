from bankers.algorithm import bankers_safety, compute_need

def main():
    print("🧯 Deadlock Detector – Banker's Algorithm (CLI Version)")
    print("Using a built-in sample dataset.\n")

    # Sample data (same as UI defaults)
    allocation = [
        [0, 1, 0],
        [2, 0, 0],
        [3, 0, 2],
        [2, 1, 1],
        [0, 0, 2],
    ]

    max_demand = [
        [7, 5, 3],
        [3, 2, 2],
        [9, 0, 2],
        [2, 2, 2],
        [4, 3, 3],
    ]

    available = [3, 3, 2]

    is_safe, safe_sequence, extra = bankers_safety(
        allocation, max_demand, available
    )
    need = compute_need(max_demand, allocation)

    print("Allocation Matrix:")
    for row in allocation:
        print(row)

    print("\nMax Demand Matrix:")
    for row in max_demand:
        print(row)

    print("\nAvailable:", available)

    print("\nNeed Matrix (Max - Allocation):")
    for row in need:
        print(row)

    if is_safe:
        print("\n✅ System is in a SAFE STATE")
        print("Safe sequence (process indices):", " -> ".join(f"P{i}" for i in safe_sequence))
    else:
        print("\n❌ System is in an UNSAFE STATE (deadlock possible)")


if __name__ == "__main__":
    main()