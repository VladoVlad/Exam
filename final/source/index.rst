.. final documentation master file, created by
   sphinx-quickstart on Wed Jan 31 04:45:02 2024.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

Welcome to final_project's documentation!
==========================================

Sorting program
This program provides the user with an interface to enter a sequence of numbers, sort them in a chosen order (ascending or descending), and display the sorted sequence as well as the time spent sorting.
User Interface

Input fields
 - Enter numbers separated by commas: An input field in which the user enters a sequence of numbers separated by commas.
Drop-down list
 - Sorting method: Drop-down list that allows you to select the sort order: ascending or descending.
Button
 - Start: A button that, when clicked, starts sorting the entered sequence.
Sorting results
 - Result List: A field that displays the sorted sequence of numbers.
Sort Time
 - A label that displays the time spent sorting in seconds.
Entered Numbers
 - A label that displays the sequence of numbers entered by the user.

Functionality
 - Input Validation: When you enter numbers, the program checks them for correct format.
 - Sort: After entering the numbers and selecting the sort method, the user can run the sort, which will display the sorted sequence and the time taken to sort.
 - Re-sorting or exiting the program: After each sort, the program offers the user a choice: repeat the sort or exit. When you select repeat sort, the input field is automatically cleared.



Import and functions
=====================

Importing libraries and modules
 - `import tkinter as tk`: Imports the `tkinter` library with the `tk` alias.
 - `from tkinter import ttk`: Import the `ttk` module from the `tkinter` library.
 - `import time`: Import the `time` module to work with time.
 - `import re`: I mport the `re` module for working with regular expressions.
 - `import tkinter.messagebox as msg`: Imports the `messagebox` module from the `tkinter` library with the `msg` alias.

Functions
 - `is_valid_input(input_str)`: Function for validating input. Checks that the input contains only numbers separated by commas.
 - `validate_input(new_value)`: Function for validating input. Checks that the input matches the specified format.
 - `sort_sequence()`: A function that sorts a sequence of numbers entered by the user.

Creating a GUI
 - Creating the main application window with the title "Sorting program" and size 1000x1000.
 - Setting a standard font for all interface elements.

Interface elements
 - `note_label`: Label for the input instruction.
 - `entry`: Entry field for a sequence of numbers.
 - `sort_combobox`: Drop-down list for selecting the sort type.
 - `start_button`: Button to start sorting.
 - `result_label`: Label for displaying the result list.
 - `result_text`: Multiline text field to display the sorted sequence.
 - `time_label`: Label to display the sorting time.
 - `original_sequence_label`: Label to display the user-entered sequence.

Main application loop
 - Running the main application loop `root.mainloop()` to display the interface and handle events.
