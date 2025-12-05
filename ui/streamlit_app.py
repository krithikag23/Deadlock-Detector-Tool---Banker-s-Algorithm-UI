import streamlit as st
import pandas as pd

from bankers.algorithm import bankers_safety, compute_need
st.set_page_config(page_title="Banker's Algorithm Deadlock Detector", layout="wide")
st.title("🧯 Deadlock Detector – Banker's Algorithm")

st.markdown(
    """
This tool checks whether the system is in a **safe state** using Banker's Algorithm.

- Edit the **Allocation** and **Max** matrices.
- Set the **Available** vector.
- Click **Run Banker's Algorithm** to see if the state is safe.
"""
)

# --- Default sample data ---
default_allocation = pd.DataFrame(
    [
        [0, 1, 0],
        [2, 0, 0],
        [3, 0, 2],
        [2, 1, 1],
        [0, 0, 2],
    ],
    columns=["A", "B", "C"],
    index=[f"P{i}" for i in range(5)],
)

default_max_demand = pd.DataFrame(
    [
        [7, 5, 3],
        [3, 2, 2],
        [9, 0, 2],
        [2, 2, 2],
        [4, 3, 3],
    ],
    columns=["A", "B", "C"],
    index=[f"P{i}" for i in range(5)],
)

default_available_str = "3 3 2"

st.subheader("1️⃣ Resource Allocation Matrices")

col1, col2 = st.columns(2)

with col1:
    st.markdown("**Allocation Matrix**")
    allocation_df = st.data_editor(
        default_allocation,
        num_rows="dynamic",
        key="allocation_editor",
    )

with col2:
    st.markdown("**Max Demand Matrix**")
    max_df = st.data_editor(
        default_max_demand,
        num_rows="dynamic",
        key="max_editor",
    )

st.subheader("2️⃣ Available Resources")

available_str = st.text_input(
    "Available vector (space-separated, e.g. `3 3 2`):",
    value=default_available_str,
)

run_button = st.button("▶ Run Banker's Algorithm")

if run_button:
    try:
        allocation = allocation_df.values.tolist()
        max_demand = max_df.values.tolist()
        available = [int(x) for x in available_str.strip().split()]

        # Basic validation
        if len(allocation[0]) != len(available):
            st.error(
                "Number of resources in **Available** must match the columns of Allocation/Max."
            )
        elif len(allocation[0]) != len(max_demand[0]):
            st.error("Allocation and Max matrices must have the **same number of columns**.")
        elif len(allocation) != len(max_demand):
            st.error("Allocation and Max matrices must have the **same number of rows (processes)**.")
        else:
            is_safe, safe_sequence, extra = bankers_safety(
                allocation, max_demand, available
            )
            need_matrix = compute_need(max_demand, allocation)

            st.subheader("3️⃣ Need Matrix (Max - Allocation)")
            need_df = pd.DataFrame(
                need_matrix,
                columns=allocation_df.columns,
                index=allocation_df.index,
            )
            st.dataframe(need_df)

            st.subheader("4️⃣ Result")

            if is_safe:
                proc_names = allocation_df.index.tolist()
                seq_labels = [proc_names[i] for i in safe_sequence]

                st.success("✅ The system is in a **SAFE STATE**.")
                st.write("**Safe sequence:**", " → ".join(seq_labels))
            else:
                st.error("❌ The system is in an **UNSAFE STATE**. Deadlock is possible.")

            with st.expander("Show internal work sequence (Banker's Algorithm steps)"):
                work_seq = extra["work_sequence"]
                work_df = pd.DataFrame(
                    work_seq, columns=allocation_df.columns
                )
                work_df.index = [f"Step {i}" for i in range(len(work_seq))]
                st.dataframe(work_df)

    except ValueError:
        st.error("Please enter only integers in the matrices and available vector.")