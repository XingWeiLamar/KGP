# KGP
Knowledge Graph Processor (KGP)
KGP is a simple tool to generate knowledge graph triplets list from the input csv file and replace each entity with a unique index number. 

Run the program by enter “python kgp.py” in the terminal.
Please follow the instruction and enter all the required input information
We use yelp.csv as an example

1.	Enter the file path of yelp.csv
   D:/kgp/yelp.csv
   (Terminal will display all the columns name of the file)
2.	The program will require user to enter the columns number of entities one by one for the KG triplets list
   we enter 8 9 10 11 
3.	Enter the relation name and the two entity column numbers on the left and right in the triplet .
   We enter a,8,10 and 
4.	Enter the path of item index file and path of relation index file
5.	Enter the type of output KG file(txt or csv) and the path of the output KG file. 
6.	Generate rating file. 
7.	Enter the columns numbers that contains user id, business name and rating score
8.	Enter the path of user index file
9.	Enter the type of output rating file(txt or csv) and the path of the output rating file.

Transfer rating file for explicit feedback to implicit feedback. And 
 Run the program by enter ”python irt.py ”
1.	Follow the instruction enter the path of kg file and the path of rating file.
2.	Enter the output paths.

Try the program with the yelp.csv. 
