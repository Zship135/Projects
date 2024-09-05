package src.main.java;
public class Token {
    
    TextColor textColor = new TextColor();

    public enum TokenType {
        // OPERATORS //
        PLUS,  //------------ "+"
        MINUS, //------------ "-"
        TIMES, //------------ "*"
        SLASH, //------------ "/" 
        EQUALS, //----------- "="
        ARROW, //------------ "->"
        BECOMES, //---------- ":="
        AND, //-------------- "&&"
        BIT_AND, //---------- "&"
        OR, //--------------- "||"
        BIT_OR, //----------- "|"
        NOT, //-------------- "!"
        BIT_XOR, //---------- "^"
        LESSTHAN, //--------- "<"
        GREATERTHAN, //------ ">" 

        // SEPARATORS //
        OPEN_PAREN, //----------- "("
        CLOSED_PAREN, //----------- ")"
        OPEN_SQUARE_BRACK, //---- "["
        CLOSED_SQUARE_BRACK, //---- "]"
        OPEN_SQUIGGLE_BRACE, //-- "{"
        CLOSED_SQUIGGLE_BRACE, //-- "}"
        COMMA, //------------- ","
        PERIOD, //------------ "."
        SEMICOLON, //------------ "."

        // KEYWORDS //
        SYM_STRING, //-------- "String"
        SYM_INT, //----------- "int"
        SYM_DOUBLE, //-------- "double"
        SYM_LONG, //---------- "long"
        SYM_VAR, //----------- "var"
        SYM_IF, //------------ "if"
        SYM_ELSE, //---------- "else"
        SYM_VOID, //---------- "void"
        SYM_PUBLIC, //-------- "public"
        SYM_PRIVATE, //------- "private"
        SYM_STATIC, //-------- "static"
        SYM_CLASS, //--------- "class"
        SYM_MAIN, //---------- "Main"
        SYM_RETURN,
        CMD_PRINT,
        STRINGLITERAL,
        INT,
        IDENTIFIER
    }

    private final TokenType tokenType;
    private final String value;

    public Token(TokenType tokenType, String value) {
        this.tokenType = tokenType;
        this.value = value;
    }

    @Override
    public String toString() {
        return "(" + textColor.BLUE + tokenType + textColor.RESET + ", " + textColor.GREEN + value + textColor.RESET + ")";
    }


}
