__all__ = (
    "true",
    "false",
)


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
