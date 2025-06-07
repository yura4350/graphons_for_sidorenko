import numpy as np
import itertools
import random
from itertools import product
from helpers import *

# ------ The first demo ------
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
G = np.array([
    [0, 1, 1, 0, 1, 0, 0, 0, 1, 1, 1, 0],
    [1, 0, 1, 0, 0, 1, 0, 1, 0, 1, 0, 1],
    [1, 1, 0, 1, 0, 0, 0, 1, 1, 0, 0, 1],
    [0, 0, 1, 0, 0, 0, 1, 1, 1, 0, 1, 0],
    [1, 0, 0, 0, 0, 1, 1, 0, 1, 0, 0, 1],
    [0, 1, 0, 0, 1, 0, 1, 0, 1, 0, 1, 0],
    [0, 0, 0, 1, 1, 1, 0, 0, 0, 0, 1, 0],
    [0, 1, 1, 1, 0, 0, 0, 0, 1, 0, 1, 1],
    [1, 0, 1, 1, 1, 1, 0, 1, 0, 1, 1, 0],
    [1, 1, 0, 0, 0, 0, 0, 0, 1, 0, 1, 1],
    [1, 0, 0, 1, 0, 1, 1, 1, 1, 1, 0, 0],
    [0, 1, 1, 0, 1, 0, 0, 1, 0, 1, 0, 0]
])
G1 = np.array([[0, 1], [1, 0]])
G2 = np.array([
    [0, 1, 1, 1, 1, 1],
    [1, 0, 1, 0, 1, 1],
    [1, 1, 0, 1, 1, 1],
    [1, 0, 1, 0, 1, 1],
    [1, 1, 1, 1, 0, 1],
    [1, 1, 1, 1, 1, 0],
])

# --- Executing User's Requested Function Calls with Progress Updates ---

# Calculating for G1
hom_H_G1 = count_homomorphisms_backtrack(H, G1)
print("Number of homomorphisms from H to G1:", hom_H_G1)

# Calculating for G2
hom_H_G2 = count_homomorphisms_backtrack(H, G2)
print("Number of homomorphisms from H to G2:", hom_H_G2)

# Calculating Sidorenko Ratio for G2
print("\n--- Calculating Sidorenko Ratio for H -> G2 ---")
gap = sidorenko_ratio(H, G2) # This will print its own progress
print("p^|E(H)| / t(H, G2) - 1 =", gap)

# Calculating for G (Note: This may take a long time to run)
hom_H_G = count_homomorphisms_backtrack(H, G)
print("Number of homomorphisms from H to G:", hom_H_G)