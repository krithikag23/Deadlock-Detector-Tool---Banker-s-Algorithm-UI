# 🧯 Deadlock Detector – Banker's Algorithm

A small OS project that checks if a system is in a **safe state** using
**Banker's Algorithm**. Includes:

- ✅ Core Banker's Algorithm implementation
- 🖥 Streamlit **web UI** to edit matrices and run the check
- 🐍 Simple CLI demo

## 🔧 Features

- Edit **Allocation** and **Max Demand** matrices
- Set **Available** resources
- Compute:
  - Need matrix = Max - Allocation
  - Safe / Unsafe state
  - Safe sequence (if it exists)
- View internal `work` vector for each step (explanation of algorithm)

---

