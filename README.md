# KGP
Knowledge Graph Processor (KGP)
KGP is a simple tool to generate knowledge graph triplets list from the input csv file and replace each entity with a unique index number. 

Run the program by enter “python kgp.py” in the terminal.
Please follow the instruction and enter all the required input information
1.	Enter the file path of the original csv file e.g. C:\data.csv
2.	Enter the columns of entities you need in the KG triplets list
3.	Enter the relation name and the two entity column numbers.
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
