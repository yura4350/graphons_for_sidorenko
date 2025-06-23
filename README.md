# Disproving Sidorenko's Conjecture: A Numerical Exploration

## Overview

This project is dedicated to the numerical investigation of the famous **Sidorenko Conjecture** (also known as the Sidorenko-Erdos-Simonovits Conjecture). The primary goal is to search for a counterexample by calculating homomorphism densities for specific graph pairs `(H, W)`.

The conjecture, in simple terms, states that the density of a bipartite graph `H` in any graph `W` is at least the density of a single edge in `W` raised to the power of the number of edges in `H`. While widely believed to be true, it remains unproven. This project employs a computational approach to test the conjecture's limits by searching for a graph `H` and a target structure `W` that violate this inequality.

---

## The Sidorenko Conjecture

Let `H` be a bipartite graph with `v(H)` vertices and `e(H)` edges. Let `W` be any graph, which for our purposes is represented by a **graphon**. A graphon is a symmetric measurable function `W: [0, 1]^2 -> [0, 1]` that can be seen as the limit of a dense graph sequence.

The number of homomorphisms from `H` to `W` is denoted by `hom(H, W)`. The **homomorphism density**, `t(H, W)`, normalizes this count. The Sidorenko Conjecture states that for any bipartite graph `H` and any graphon `W`:

$$t(H, W) \ge t(K_2, W)^{e(H)}$$

Here, `t(K_2, W)` represents the edge density of the graphon `W`. The project's objective is to find a specific pair `(H, W)` for which this inequality does not hold.

---

## Methodology

### 1. Target Graph `W`: Step-Graphons

To make the problem computationally tractable, we restrict the target graphon `W` to be a **step-graphon**. A step-graphon can be represented by an `n x n` symmetric matrix where each entry `W_{ij}` corresponds to the constant edge density between partitions `i` and `j`. This project systematically tests step-graphons of increasing complexity, starting with matrices of size `4x4`, `5x5`, `6x6`, and larger.

### 2. Optimization via Adaptive Monte Carlo Search (AMCS)

Instead of a brute-force search, this project uses a sophisticated **Adaptive Monte Carlo Search (AMCS)** algorithm to find an optimal `W` that is most likely to be a counterexample. The algorithm's goal is to minimize the "Sidorenko gap": `p^e - t`, where `p` is the edge density and `t` is the homomorphism density.

The AMCS process works as follows:
- **Local Search (Exploration):** The algorithm performs a Nested Monte Carlo Search (NMCS) by taking the current best `W` and applying small, random changes (perturbations) to its matrix values for a fixed number of steps. It keeps the new matrix if it improves the score (i.e., reduces the gap).
- **Adaptive Strategy:** If the local search successfully finds a better `W`, the algorithm accepts it and continues searching from this new point. If it fails to find an improvement after a certain number of attempts (`max_depth`), it increases the intensity of the next local search (`level`), allowing it to escape local minima and explore the search space more effectively.

This adaptive approach allows the search to dynamically balance between fine-tuning a promising solution and broadly exploring for new, better candidates.

---

## Main Case Study: `H = K_{5,5} - C_{10}`

While the framework can test any bipartite graph `H`, the primary focus of this investigation is `H = K_{5,5} - C_{10}`.

- **Definition:** This graph is constructed by taking the complete bipartite graph `K_{5,5}` and removing the edges of a 10-cycle (`C_{10}`).
- **Significance:** This graph was proposed by de Caen (1998) as a potential counterexample to the Sidorenko conjecture. It is one of the most well-known candidates. `K_{5,5} - C_{10}` has 10 vertices and `25 - 10 = 15` edges.

The central goal of this project is to leverage AMCS to find a step-graphon `W` such that:

$$t(K_{5,5} - C_{10}, W) < t(K_2, W)^{15}$$

If such a `W` is found, it would serve as a concrete counterexample and disprove the Sidorenko conjecture.

## Project Structure


.
├── amcs_for_graphon_demo.py  # Main script to define H, W_initial and run the AMCS
├── amcs_graphons.py          # Implements the core AMCS and NMCS algorithms
├── helpers.py                # Helper functions for calculations (sidorenko_gap, perturb, etc.)
├── older_demos/                # Contains older demo files used in previous calculations
└── README.md                   # This file


## How to Run the Experiments

1.  **Define Graph H:** The adjacency matrix for `H` is defined directly within `amcs_for_graphon_demo.py`. You can modify it there for different test cases.
2.  **Configure Initial Graphon:** Set the initial `W_initial` matrix in `amcs_for_graphon_demo.py`. This serves as the starting point for the AMCS optimization.
3.  **Execute Script:** Run the main demo script from the terminal.
    ```bash
    python amcs_for_graphon_demo.py
    ```
4.  **Analyze Results:** The script will output the progress of the AMCS search and print the final optimized graphon `W` and the smallest Sidorenko gap found. Any result where the gap is negative is a potential counterexample and should be investigated further.
