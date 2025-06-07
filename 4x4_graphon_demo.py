import numpy as np
import itertools
import random
from itertools import product
from helpers import *


# ---- Define the graph H ----
H = np.array([
    [0,0,0,0,0,0,0,1,1,1],
    [0,0,0,0,0,1,0,0,1,1],
    [0,0,0,0,0,1,1,0,0,1],
    [0,0,0,0,0,1,1,1,0,0],
    [0,0,0,0,0,0,1,1,1,0],
    [0,1,1,1,0,0,0,0,0,0],
    [0,0,1,1,1,0,0,0,0,0],
    [1,0,0,1,1,0,0,0,0,0],
    [1,1,0,0,1,0,0,0,0,0],
    [1,1,1,0,0,0,0,0,0,0]
])

# ---- Define initial W ----

""" W with average p = 0.80 gives the result of Final Sidorenko gap: -2.7126e-05 - not so great"""
# W = np.array([
#     [0.78, 0.86, 0.69, 0.87],
#     [0.91, 0.81, 0.6,  0.88],
#     [0.8,  0.68, 0.96, 0.76],
#     [0.71, 0.85, 0.95, 0.69]
# ])

""" W with average p = 0.80 gives much better results for Final Sidorenko gap: -"""
W = np.array([
[0.89, 0.49, 0.35, 0.5],
[0.31, 0.78, 0.2, 0.59],
[0.39, 0.71, 0.51, 0.2],
[0.11, 0.87, 0.39, 0.68],
])

# --- Optimization loop with Progress ---
print("\n--- Starting Optimization ---")
print("Calculating initial gap...")
# First, calculate the initial gap
best_gap, _, _ = sidorenko_gap(H, W)
W_best = W.copy()
print(f"Initial W matrix:\n{np.round(W_best, 3)}")
print(f"Initial Sidorenko gap: {best_gap:.4e}")

num_steps = 1000
for step in range(num_steps):
    # Perturb the current best matrix to find a new candidate
    W_new = perturb(W_best)
    new_gap, _, _ = sidorenko_gap(H, W_new)
    
    # Hill-climbing: if the new matrix gives a smaller absolute gap, it's our new best
    if abs(new_gap) < abs(best_gap):
        W_best = W_new.copy()
        best_gap = new_gap
    
    # --- Progress indicator for the main optimization loop ---
    if (step + 1) % 10 == 0 or step == num_steps - 1:
        print(f"Step [{step + 1}/{num_steps}] | Current Best Gap: {best_gap:.4e}")

# --- Final output ---
print("\n--- Optimization Finished ---")
print("Final optimized W:")
print(np.round(W_best, 3))
print(f"Final Sidorenko gap: {best_gap:.4e}")