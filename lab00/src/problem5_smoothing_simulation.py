from __future__ import annotations

def smooth_once(values: list[float]) -> list[float]:
    """Compute one smoothing step (helper)."""
    n = len(values)
    if n == 0:
        return []
    if n == 1:
        return [float(values[0])]
    out: list[float] = [0.0] * n
    out[0] = (values[0] + values[1]) / 2.0
    for i in range(1, n - 1):
        out[i] = (values[i - 1] + values[i] + values[i + 1]) / 3.0
    out[-1] = (values[-2] + values[-1]) / 2.0
    return out

def smooth_until_stable(values: list[float], max_iters: int = 100, tol: float = 1e-9) -> tuple[int, list[float]]:
    """Iteratively smooth until stable or max_iters.

    Stabilized means: max absolute change between iterations <= tol.
    Returns (iterations_run, final_values).
    """
    # TODO: implement
    raise NotImplementedError
