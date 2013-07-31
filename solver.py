#!/usr/bin/python
# -*- coding: utf-8 -*-


from brain import search

def solveIt(inputData):
    # Modify this code to run your optimization algorithm

    # parse the input
    lines = inputData.split('\n')

    firstLine = lines[0].split()
    nodeCount = int(firstLine[0])
    edgeCount = int(firstLine[1])

    graph = [[] for n in xrange(nodeCount)] 
    for i in range(1, edgeCount + 1):
        line = lines[i]
        parts = line.split()
        n0 = int(parts[0])
        n1 = int(parts[1])
        graph[n0].append(n1)
        graph[n1].append(n0)

    num_colors = int(raw_input("Please enter color limit: "))
    solution = search(num_colors, graph) 

    # prepare the solution in the specified output format
    outputData = str(max(solution)) + ' ' + str(0) + '\n'
    outputData += ' '.join(map(str, solution))

    return outputData


import sys

if __name__ == '__main__':
    if len(sys.argv) > 1:
        fileLocation = sys.argv[1].strip()
        inputDataFile = open(fileLocation, 'r')
        inputData = ''.join(inputDataFile.readlines())
        inputDataFile.close()
        print solveIt(inputData)
    else:
        print 'This test requires an input file.  Please select one from the data directory. (i.e. python solver.py ./data/gc_4_1)'

