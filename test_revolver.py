import sys
sys.path.append('../')
from model.revolver import Revolver

def test_init():
    revolver = Revolver(6)
    assert len(revolver.chamber) == 6

def test_load():
    revolver = Revolver(6)
    revolver.load(3)
    assert revolver.chamber == [True] * 3 + [False] * 3

def test_spin():
    revolver = Revolver(6)
    revolver.load(1)
    revolver.spin()
    assert revolver.chamber != [True] + [False] * 5

def test_fire():
    revolver = Revolver(6)
    revolver.load(1)
    revolver.fire()
    assert revolver.chamber[0] == False

def test_empty():
    revolver = Revolver(6)
    revolver.load(6)
    revolver.empty()
    assert revolver.chamber == [False] * 6
