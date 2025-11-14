# Quicksort Algorithm – Deterministic and Randomized Versions

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

-----------------------------------------------------------------------------------------------
n        random_det   random_rand  sorted_det   sorted_rand  reverse_det  reverse_rand
-----------------------------------------------------------------------------------------------
1000     0.000737     0.001216     0.027133     0.000892     0.014472     0.000862
5000     0.003922     0.006329     0.797572     0.005203     0.402167     0.005402
10000    0.008739     0.012413     3.234579     0.010760     1.551814     0.011527
20000    0.022907     0.026380     13.024872    0.025531     6.462369     0.024445
-----------------------------------------------------------------------------------------------

## 📈 What the Results Show

- Deterministic Quicksort performs very well on random input but terribly on sorted and reverse-sorted input (worst-case O(n²)).
- Randomized Quicksort performs consistently well on all inputs and avoids the worst-case by using a random pivot (expected O(n log n)).

These results match the theoretical behavior perfectly.