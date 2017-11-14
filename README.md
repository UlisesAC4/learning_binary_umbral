# Learning binary umbral
A binary umbral is a black and white filter, a range is provided to define what will be color black and white. In this script from 62 to 191 grayscale color is defined as black, and the rest as white.

## Installing this script
You need to install the ```scipy``` Python package.

## Inner working
Python lists are slow, processing a high density image can be slow in procedural algorithms like the one of this project, so I am implementing the solution with the ```scipy``` package to skyrocket the performance.

In this implementation black color is in the range (61, 192) and white in the complement of that range in the [0, 255].
