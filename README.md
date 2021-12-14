# NORETURN
NORETURN is an esoteric programming language, based around the idea of not going back
# Concept
Program coded in noreturn runs over one array, using 2 pointers. As expected, the position of the pointers can only incremented, which makes coding real pleasant (if you hate yourself and have way too much time, that is). Also, user can control only one pointer at a time. Also, the value of array cells can only be increased and decreased by 1 at a time. Enjoy, and stay strong.
# Instructions
The whole instruction set consists of:  
**mv** -> move current pointer to the next cell.  
**sp** -> swap the current active pointer.  
**add** -> add 1 to array\[current_pointer\].  
**sub** -> subtract 1 from array\[current_pointer\].  
**cp** -> copy value from array\[other_pointer\] to array\[current_pointer\].  
**pr** -> print integer value of array\[current_pointer\].  
**prc** -> print array\[current_pointer\] as an ASCII char.  
**rd** -> read an integer into array\[current_pointer\].  
**ls** -> loop next commands (until corresponding loop end mark) for array\[current_pointer\] times.  
**le** -> marks the end of a loop  
That's all (comments might be added in the future)
# Other info
" ", "\t", "\n" are ignored in the code. However, logically, each command has to be separated by at least one space, newline or tab.  
Check multiply_explained to get a better understanding of coding in noreturn.  
To run your code, go into NORETURN directory and type "python3 (or whatever opens python) shell.py <relative_filepath>".  
^ This will obviously get improved. Work in progress.  
^^ Yes, I created a stupid interpreted programming language using a smart interpreted programming language. And also, you obviously need python to run this thing.  
To check if it all works, get into the directory with language code and type "python3 shell.py examples/helloworld.nr" 
Good luck!
