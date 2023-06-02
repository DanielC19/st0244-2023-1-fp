# st0244-2023-1-fp

## By:
- Juan Diego Robles de la Ossa
- Daniel Correa Botero

## Used OS for develop:
- Windows 10

## Python version:
- 3.11.2

## Project Overview
We made a program that, roughly, unifies and shows the substitutions needed
for unifying a given constraint set, also specifies if it cannot unify.

There are five constraint sets, defined in each one of the files inside
`/test` folder. They are called from the main function in `Python` which reads
the file as a `string` and the separate it by line breaks (`\n`) to evaluate
each constraint and start running the unify algorithm given in the final
project document by the lecturer.

Each constraint set should print the substitutions needed or the impossibility
of unifying correctly.