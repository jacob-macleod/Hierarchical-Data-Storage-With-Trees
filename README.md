# Hierarchical-Data-Storage-With-Trees
A practice project to test an implementation of hierarchical file storage with trees

This is one implementation of the theoretical concept of trees.

<!-- vim-markdown-toc GFM -->

* [Notes on my Implementation](#notes-on-my-implementation)
* [The Aim of this Implementation](#the-aim-of-this-implementation)

<!-- vim-markdown-toc -->

## Notes on my Implementation
Each node of the tree has a number assigned to it, representing the line in which it is stored in the .csv files. Tree nodes and branches stored sequentially in files are manipulated based on this fact. Trees are numbered left to right, where the left most root is 1, it's left most branch is 2, and so on. 

## The Aim of this Implementation
This is not an implementation of a Binary tree or other system. As a result, data is not stored in a linearly increasing order or anything. This program is designed to create a data structure to be able to store items in a hierarchical format. This could be for several reasons, such as:
* Storing files and folders in an OS
* Storing flashcards and folders in a flashcard app
* Storing documents and notes in a notetaking app

The second option is the main reason why I am developing this program. This differs from normal trees such as binary trees in some main regards:
* **Data is not saved in any particular order**: When saving data, the user decides where the data is stored and to what parent by selecting the folder or some other thing to save the data (if this was implemented in a finished program). Therefore, data is saved to whichever parent the user wants
* **There is no single root node**: In a finished project, the nodes could represent files and folders. In the root location, you could have multiple files without storing them in a folder. Thus, there are muliple root nodes. Each root node could store the data for a single user and be named after their username. The root nodes are stored in an index for easy manipulation
* **Data is searched differently**: To search the data, I have only included a function to find the children of a node. This is to best suit the program to the application it is designed for

This code is written so you can copy and edit it to use in your program. If you want help of advice on this, please open an issue. If you use this code in your project, please give me credit!
