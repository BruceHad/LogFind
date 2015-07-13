import os

from nose.tools import *
from logfind.logfind import *

def test_search_all():
    lf = os.path.join(os.getcwd(), 'tests/test_log_file.txt')
    assert(search_all("one", lf) == True)
    assert(search_all(["one"], lf) == True)
    assert(search_all(["one","two"], lf) == True)
    assert(search_all(["four"], lf) == False)
    assert(search_all(["two", "four"], lf) == False)
    assert(search_all(["one", "two", "four"], lf) == False)

def test_search_any():
    lf = os.path.join(os.getcwd(), 'tests/test_log_file.txt')
    assert(search_any("one", lf) == True)
    assert(search_any(["one"], lf) == True)
    assert(search_any(["one","two"], lf) == True)
    assert(search_any(["four"], lf) == False)
    assert(search_any(["two", "four"], lf) == True)
    assert(search_any(["one","two", "four"], lf) == True)