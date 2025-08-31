# All Pairs Shortest Path (Floyd-Warshall) Algorithm Implementation

This repository contains a Python implementation of the **Floyd–Warshall algorithm** for computing the shortest paths between all pairs of nodes in a directed weighted graph.  
The implementation is compared with NetworkX’s built-in `floyd_warshall` function for correctness, and the graph is also visualized using `matplotlib` and `networkx`.

---

## 📌 About the Algorithm

The **Floyd–Warshall algorithm** is a **dynamic programming** approach that finds shortest paths between all pairs of nodes in a weighted graph.  
It works even when edge weights are negative, as long as there are **no negative weight cycles**.

- **Input:** Directed graph with weighted edges  
- **Output:** Distance matrix showing shortest path distances between all pairs of nodes  

The algorithm updates paths step by step by checking whether including an intermediate node `k` shortens the path between nodes `i` and `j`.

---

## 🚀 Features of This Code

- Builds a directed, weighted graph using `networkx`  
- Implements Floyd–Warshall from scratch (without NumPy vectorization, for clarity)  
- Compares results with NetworkX’s built-in implementation  
- Displays the shortest path distance matrix in a clean Pandas DataFrame  
- Visualizes the graph with edge weights  

---

## 🧩 Code Structure

1. **Graph construction**  
   Creates a directed weighted graph with both positive and negative edges.  

2. **Floyd–Warshall function**  
   - Initializes a distance matrix with `∞` (no known path).  
   - Sets diagonal to `0` (distance to self).  
   - Iteratively updates shortest distances using triple nested loops.  

3. **Comparison with NetworkX**  
   Validates results against NetworkX’s implementation.  

4. **Visualization**  
   Draws the graph and edge weights using `matplotlib`.

---

## 📊 Bellman–Ford vs All-Pairs Shortest Path (APSP)

| Feature                  | **Bellman–Ford** (Single-source) | **APSP (Floyd–Warshall / Johnson)** |
|---------------------------|----------------------------------|-------------------------------------|
| **Type**                 | Single-source shortest path      | All-pairs shortest path             |
| **Input**                | Graph + 1 source node            | Graph only                          |
| **Output**               | Shortest path from source → all nodes | Matrix of shortest paths between every pair |
| **Negative weights**      | ✅ Supported                    | ✅ Supported (but not negative cycles) |
| **Detects negative cycles** | ✅ Yes                         | ✅ Yes                               |
| **Complexity**            | `O(V·E)`                        | Floyd–Warshall: `O(V³)` <br> Johnson: `O(V² log V + V·E)` |
| **When to use**           | If you only need paths from one node | If you need all pairs of shortest paths |

---

👉 **Key Difference**:  
- **Bellman–Ford** solves *single-source shortest path* (one node → all others).  
- **APSP algorithms** (like Floyd–Warshall or Johnson’s) solve *all-pairs shortest paths* (every node → every other node) in one run.  

⚡ **Analogy:**  
- Bellman–Ford: *“From my home, what’s the shortest path to every other city?”*  
- APSP: *“What’s the shortest path between every pair of cities in the whole country?”*


