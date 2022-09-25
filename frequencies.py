"""Frequencies function."""
"""ENTER YOUR SOLUTION HERE!"""

def frequencies(items):
    frequencies = {}
    for i in items:
        v = str(i)
        if(frequencies.get(v) == None):
            frequencies[v] = 1
        else:
            frequencies[v] = frequencies[v]+ 1
    return frequencies
