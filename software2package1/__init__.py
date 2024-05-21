"""software2package1."""

__all__ = (
    "__version__",
    "hello_world",
    # Add functions and variables you want exposed in `software2package1.` namespace here
)

__version__ = "0.0.1"

from .printing import hello_world

