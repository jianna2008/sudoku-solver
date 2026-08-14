# **Sudoku Solver**

Sudoku Solver is a Python project that uses backtracking and constraint checking to solve a 9x9 sudoku board, represented as a 2D array. 

## **Overview**

This project implements algorithms in Python from scratch. 

The solver takes a partially completed sudoku board, identifies the empty cells represented as “0,” tests possible values and recursively explores each solution's validity. When the algorithm realizes that a solution is invalid, it backtracks by restoring the cell and trying another solution.

## **Features**

* Solves standard 9x9 Sudoku board  
* Recursive backtracking algorithm  
* Constraint checking for rows, columns, and each 3x3 grid  
* Identifies empty cells  
* Restores empty cells when a value fails  
* Displays solved 9x9 solution

## **Algorithm**

### **Backtracking**

The solver uses a recursive backtracking approach

1. Find an empty cell  
2. Try value from 1-9  
3. Check whether value fits the constraints for rows, columns, and 3x3 grid  
4. If valid, place value in cell  
5. Recursively try to solve the rest of the board  
6. If the recursive call fails, reset the cell to zero  
7. Try next value from 1-9  
8. Continue until the board is solved, or no valid solution exists

### **Validity Checking**

Before changing the value of a cell, the project checks if the value fits the constraints of sudoku.

The solver checks:

* Row: The value cannot already exist in the same row as the empty cell.  
* Column: The value cannot already exist in the same column as the empty cell.  
* 3x3 subgrid: The value cannot already exist in the 3x3 subgrid of the empty cell

## **Implementation**

### **`solve()`**

The main recursive function responsible for solving the board.

**Input:**

* The empty board

**Output:**

* True, if the board was successfully solved  
* False, if the solver failed to solve the board. 

### **`find_empty()`**

The program uses a double for loop to search through the entire board for an empty cell. 

### **`valid()`**

The program checks the constraints for the rows, columns, and 3x3 subgrid, and returns true if it's a possible solution, and false, if it is not. 

### **`print_board()`**

The print\_board() function prints the 2D array in a visually aesthetic sudoku board. 

## **Example**

### **Input**

0 3 0 | 0 0 1 | 0 2 4   
0 0 7 | 0 0 5 | 1 0 0   
0 0 0 | 7 0 0 | 0 8 0   
\---------------------  
7 0 0 | 0 1 0 | 6 9 0   
4 0 0 | 0 3 8 | 0 0 0   
0 0 2 | 5 0 0 | 0 0 1   
\---------------------  
0 0 1 | 3 4 2 | 9 0 0   
0 6 5 | 0 9 0 | 0 0 0   
0 2 0 | 0 0 0 | 0 3 7

### **Output**

5 3 8 | 9 6 1 | 7 2 4   
2 9 7 | 4 8 5 | 1 6 3   
1 4 6 | 7 2 3 | 5 8 9   
\---------------------  
7 5 3 | 2 1 4 | 6 9 8   
4 1 9 | 6 3 8 | 2 7 5   
6 8 2 | 5 7 9 | 3 4 1   
\---------------------  
8 7 1 | 3 4 2 | 9 5 6   
3 6 5 | 8 9 7 | 4 1 2   
9 2 4 | 1 5 6 | 8 3 7 

## **Complexity**

### **Time Complexity**

The backtracking algorithm is the worst case exponential time complexity because the algorithm may need to explore every possible solution before finding the right one. However, constraint checking eliminates many of the possible solutions. 

### **Space Complexity**

The solver uses **O(d)** auxiliary space for the recursion stack, where `d` is the maximum recursion depth. For a standard 9×9 Sudoku, the depth is bounded by the number of empty cells.

The board itself is modified **in place**, so the solver does not create a separate board for each possibility.

## **Performance Metrics**

The solver tracks performance metrics to measure the computational work performed by the backtracking algorithm.

### **Execution Time**

The solver uses Python's `time.perf_counter()` to measure the time required to solve the board.

### **Recursive Calls**

The solver counts the number of times `solve()` is recursively called while searching for a solution.

## **Language**

* Python

## **What I Learned**

* Implementing recursive algorithms  
* Translating an algorithm into a working Python implementation  
* Understanding base cases and recursive calls

## **Future Improvements**

* Support loading different boards from files  
* Add input validation  
* Implementing a better solving algorithm  
* Creating a user interface

## **Author**

Jianna Seale

github.com/jianna2008

