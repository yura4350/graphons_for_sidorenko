import numpy as np
import itertools
import random
from itertools import product
from time import time
from helpers import *
from amcs_graphons import *

if __name__ == "__main__":
    # ---- Define the graph H ----
    H = np.array([
        [0,0,0,0,0,0,0,1,1,1], [0,0,0,0,0,1,0,0,1,1], [0,0,0,0,0,1,1,0,0,1],
        [0,0,0,0,0,1,1,1,0,0], [0,0,0,0,0,0,1,1,1,0], [0,1,1,1,0,0,0,0,0,0],
        [0,0,1,1,1,0,0,0,0,0], [1,0,0,1,1,0,0,0,0,0], [1,1,0,0,1,0,0,0,0,0],
        [1,1,1,0,0,0,0,0,0,0]
    ])

    # ---- Define initial W ----
    # W_initial = np.array([
    #     [0.89, 0.49, 0.35, 0.5], [0.31, 0.78, 0.2, 0.59],
    #     [0.39, 0.71, 0.51, 0.2], [0.11, 0.87, 0.39, 0.68],
    # ])
    # ---- Define initial W ----
    W_initial = np.array([
        [0.48, 0.86, 0.76, 0.61, 0.21],
        [0.22, 0.83, 0.17, 0.28, 0.80],
        [0.55, 0.44, 0.64, 0.21, 0.28],
        [0.43, 0.84, 0.60, 0.51, 0.22],
        [0.61, 0.55, 0.64, 0.31, 0.76]
    ])

    # --- Run the AMCS Optimization ---
    start_time = time()
    W_final, final_gap = AMCS_graphon(H, W_initial, max_depth=5, max_level=3)
    print(f"\nTotal search time: {time() - start_time:.2f} seconds")
