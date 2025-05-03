# CMPS 2200 Recitation 09

## Answers

**Name:** Sophie Strobl


Place all written answers from `recitation-09.md` here for easier grading.



- **2)**
The worst-case work is O((n+m)logn), since the algorithm may restart up to k times (once per component), and each restart processes nodes and edges using a priority queue with logn operations.

- **4)**
The total work is O(n^2 log n)