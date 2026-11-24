""" Claude-powered toolkit for turning job postings into structured data, documents and agent workflows.
"""

# inherit version to avoid collision/drift
from importlib.metadata import PackageNotFoundError
from importlib.metadata import version as _version
try:
    __version__ = _version("applicant-kit")
except PackageNotFoundError:
    # Package is not installed (e.g. running locally or during tests)
    __version__ = "0+unknown"

# expose as public api 
__all__ = ["__version__"]
