from brain import *
import pytest

class TestAssignment:
    def test_creation(self):

        
        graph = {0:[1,2], 1:[0,2], 2:[0,1]} 
        a = Assignment(3, graph)
        assert a.table == [[0,1,2],[0,1,2],[0,1,2]]
        
        a.table[1].pop()
        assert a.choose() == (1, [0,1])
        
        b = a.set(1,0)
        assert b.table[1] == [0]
        assert a.table[1] != b.table[1]


    def test_triangle(self):

        graph = {0:[1,2], 1:[0,2], 2:[0,1]} 
        a1 = Assignment(3, graph)

        a2 = a1.set(0,0)
        assert a2.propagate()
        assert a2.table[0] == [0]
        assert a2.table[1] == [1,2]
        assert a2.table[2] == [1,2]


        v,d = a2.choose()
        assert v == 1
        assert d == [1,2]
        
        a3 = a2.set(v,d[0])
        assert a3.propagate()
        assert a3.table[0] == [0]
        assert a3.table[1] == [1]
        assert a3.table[2] == [2]


    def test_search(self):

        graph = {0:[1,2], 1:[0,2], 2:[0,1]} 
        result = search(3, graph)  
        assert result.table[0] == [0]
        assert result.table[1] == [1]
        assert result.table[2] == [2]

    def test_baetter(self):
        graph = {0:[1,2,3,4], 1:[0,2,3,4], 2:[0,1,3,4], 3:[0,1,2], 4:[0,1,2]}
        result = search(20, graph)
        assert result.table == [[0],[1],[2],[3],[3]]


