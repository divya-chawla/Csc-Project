#Initial File

'''
Sudo Code For project: 


function From_puzzle_to_cnf(stdin){
 Read Input From Stdin 
 
 if (no input throw error){
 }
 // Load input into something and ignore newlines 
 
 
 
 
 /* 
 we intiat are data structure whatever it it to have all spots be wild cards then as we find non wild cards 
 we change the appropriate items in are datastructure to not include the new value ie tables stars like this: 
 
 000000000
 000000000
 000000000
 000000000
 000000000
 000000000
 000000000
 000000000
 000000000
 then after find a 2 in the input at the 1,2 position 
 we mark the 1,2 position as not everythiong except 2 
 
 020000000
 000000000
 000000000
 000000000
 000000000
 000000000
 000000000
 000000000
 000000000
 
 and we mark the first row and second column plus the 3x3 grid as not 2 
 
 
 */ 
 
 
 // a possible datastructure could be a 3d array 3x3x9 where possible values are stored in the 9 length array 
 
 
 while (more chars/ints){ 
    for the 9 ints/chars {
      
      IF (wildcard){
      continue 
      }
      else (not wild card){
            remove item from possible values of col
            remove item from possible values of row
            remove item from possible values of 3x3
      
        }//else 
        read  next int/ char
    } // for 
}// while 

// after done reading input into datastructure we have a function/method evalute are structure and spit it out in normal form 

output = Some_func(datastructure );
return output//Print? 
}

some_func(structure){
// convert from are datasctructure to the cnf form 
}





function convertfromcnftopuzzle(stdin){


} 
'''
