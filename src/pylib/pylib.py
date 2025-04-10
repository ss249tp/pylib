__all__ = (
    "true",
    "false",
)


import torch as tc


def true(arg: object = None) -> bool:
    """Return `True` no matter what.

    Args:
        arg: Any object.

    Returns:
        `True`.
    """
    return True


def false(arg: object = None) -> bool:
    """Return `False` no matter what.

    Args:
        arg: Any object.

    Returns:
        `False`.
    """
    return False


def linear(in_dim: int, out_dim: int) -> tc.nn.Module:
    return tc.nn.Linear(in_dim, out_dim)
