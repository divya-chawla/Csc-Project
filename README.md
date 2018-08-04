Sud2SAT 
=============

Created By
-------------

Dryden Linden-Bremner V00849440
Whitney Dluhosh  V00839944


Introduction 
------------

The Program Sud2Sat inclosed is designed to take a unsolved suduko puzzle of the form 

    000001000
    100020040
    200030060
    000000000
    000000000
    000000000
    000000000
    000000000
    000000000

or of the form 

    000001000100020040200030060000000000000000000000000000000000000000000000000000000

Where the zeros or other non-numeric characters represent unknown values ranging from 1-9. 

The program will then take the text and convert it into a cnf format with the form 123 where the 1 correspods to row the 2 corresponds to col and 3 is the value. 

This cnf format will then be passed to a miniSAT solver to be solved and the output of that will be parsed and put into the form listed above.

Requirments
------------

The operation of this program requires the miniSAT SATsolver to be installed in the same directory as the python file.

Librarys 
--------- 
The Program uses the OS , sys and re. 

How To Run 
----------

python sud2sat.py <inputfile> 
    
python sat2sud.py <cnfinputfile>






