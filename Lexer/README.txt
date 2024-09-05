

-----------------------------------------------------------------------------
LEXICAL ANALYZER
-----------------------------------------------------------------------------

This project is built to be a basic, generic lexical analyzer (lexer). I built this to be general enough that it can be edited to fit any
compiler I would need in the future. It inlcudes a "test.txt" file which functions as the file to write the program in. WHen running this program,
the program written will be broken down into tokens which consist of a token type and a value. For example, if you write 
"int x = 5;"
then the expected output from this lexer would be as such:
[(SYM_INT, int) , (IDENTIFIER, x) , (EQUALS, =) , (INT, 5)]