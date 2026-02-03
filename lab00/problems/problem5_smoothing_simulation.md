## Problem 5: Neighbor Smoothing Simulation

Write:
```python
def smooth_until_stable(values: list[float], max_iters: int = 100, tol: float = 1e-9) -> tuple[int, list[float]]:
    ...
```

Repeatedly update:
- each element becomes the average of itself and its immediate neighbors
- ends have only one neighbor

Stop when max absolute change <= tol, or after max_iters.
Return (iterations_run, final_values).
