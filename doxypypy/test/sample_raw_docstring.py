#!/usr/bin/env python
# encoding: utf-8
"""
Raw docstring Example

This example demonstrates the usage of raw-strings as docstrings.
Mainly, with maths in mind.
"""


def sqrt(x):
    r"""
    Calculates the square root.

    @f[
    \sqrt{x}
    @f]

    Args:
        x:  The argument.

    Returns:
        The square-root.
    """
    pass


def inverse(x):
    r"""
    Calculates the inverse.

    @f[
    \frac{1}{x}
    @f]

    Args:
        x:  The argument.

    Returns:
        The inverse.
    """
    return 1/x
