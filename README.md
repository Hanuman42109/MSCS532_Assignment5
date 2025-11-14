# Quicksort Algorithm - Deterministic and Randomized Versions

This repository contains the full implementation and empirical analysis of the **Deterministic Quicksort** and **Randomized Quicksort** algorithms.  
The project includes:

- Deterministic Quicksort (in-place Lomuto partition)
- Randomized Quicksort (random pivot selection)
- Empirical running-time comparison
- Table-formatted output printed in the terminal
- Results saved to files (`results.txt`, `results.csv`, `results.md`)
- A detailed report explaining all analysis

---

## 🚀 How to Run

Make sure you have Python 3 installed.

Run the main program:

```bash
python quick_sort.py
```
## 📊 Example of Output Table

![Alt text](results.md)

## 📈 What the Results Show

- Deterministic Quicksort performs very well on random input but terribly on sorted and reverse-sorted input (worst-case O(n²)).
- Randomized Quicksort performs consistently well on all inputs and avoids the worst-case by using a random pivot (expected O(n log n)).

These results match the theoretical behavior perfectly.