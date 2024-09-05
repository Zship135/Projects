package src.main.java;
import java.io.BufferedReader;
import java.io.FileNotFoundException;
import java.io.FileReader;
import java.io.IOException;
import java.util.ArrayList;

public class Lexer {

    Token token;
    ArrayList<Token> tokenList = new ArrayList<>();
    StringBuilder input = new StringBuilder();
    String line;
    private String text;
    private int pos = 0;
    private char currentChar;

    public Lexer() {}

    public void readInput(String fileName) {
        try (FileReader file = new FileReader(fileName);
             BufferedReader br = new BufferedReader(file)) {
            while ((line = br.readLine()) != null) {
                input.append(line).append("\n");
            }
            text = input.toString();
            currentChar = text.charAt(pos);
        } catch (FileNotFoundException e) {
            System.out.println("ERROR: FILE NOT FOUND");
        } catch (IOException e) {
        }
    }

    public void analyze() {
        readInput("src/main/java/test.txt");
        while (pos < text.length()) {
            tokenize();
        }
        System.out.println(tokenList);
    }

    public void advance() {
        pos++;
        if (pos < text.length()) {
            currentChar = text.charAt(pos);
        } else {
            currentChar = '\0'; // Null character to signify the end of input
        }
    }

    public void createToken(Token.TokenType tokenType, String value) {
        token = new Token(tokenType, value);
        tokenList.add(token);
    }

    public void tokenize() {
        StringBuilder keyword = new StringBuilder();
        while (pos < text.length()) {
            if (Character.isWhitespace(currentChar)) {
                checkWhiteSpace();
            } else if (Character.isAlphabetic(currentChar)) {
                checkKeyword(keyword);
            } else if (Character.isDigit(currentChar)) {
                checkDigit(keyword);
            } else if (isOperator(currentChar)) {
                checkOperator(keyword);
            } else if (isSeparator(currentChar)) {
                checkSeparator(keyword);
            } else if (currentChar == '\"' || currentChar == '\'') {
                checkStringLiteral(keyword);
            } else {
                System.out.println("NONE FOUND");
                advance();
            }
            keyword.setLength(0); // Clear keyword after processing
        }
    }

    public void checkToken(StringBuilder keyword) {
        switch (keyword.toString()) {
            case "+" -> {createToken(Token.TokenType.PLUS, keyword.toString());}
            case "-" -> {createToken(Token.TokenType.MINUS, keyword.toString());}
            case "*" -> {createToken(Token.TokenType.TIMES, keyword.toString());}
            case "/" -> {createToken(Token.TokenType.SLASH, keyword.toString());}
            case "=" -> {createToken(Token.TokenType.EQUALS, keyword.toString());}
            case "->" -> {createToken(Token.TokenType.ARROW, keyword.toString());}
            case "&&" -> {createToken(Token.TokenType.AND, keyword.toString());}
            case "&" -> {createToken(Token.TokenType.BIT_AND, keyword.toString());}
            case "||" -> {createToken(Token.TokenType.OR, keyword.toString());}
            case "|" -> {createToken(Token.TokenType.BIT_OR, keyword.toString());}
            case "!" -> {createToken(Token.TokenType.NOT, keyword.toString());}
            case "^" -> {createToken(Token.TokenType.BIT_XOR, keyword.toString());}
            case "(" -> {createToken(Token.TokenType.OPEN_PAREN, keyword.toString());}
            case ")" -> {createToken(Token.TokenType.CLOSED_PAREN, keyword.toString());}
            case "[" -> {createToken(Token.TokenType.OPEN_SQUARE_BRACK, keyword.toString());}
            case "]" -> {createToken(Token.TokenType.CLOSED_SQUARE_BRACK, keyword.toString());}
            case "{" -> {createToken(Token.TokenType.OPEN_SQUIGGLE_BRACE, keyword.toString());}
            case "}" -> {createToken(Token.TokenType.CLOSED_SQUIGGLE_BRACE, keyword.toString());}
            case ";" -> {createToken(Token.TokenType.SEMICOLON, keyword.toString());}
            case "<" -> {createToken(Token.TokenType.LESSTHAN, keyword.toString());}
            case ">" -> {createToken(Token.TokenType.GREATERTHAN, keyword.toString());}
            case ":=" -> {createToken(Token.TokenType.BECOMES, keyword.toString());}
            case "," -> {createToken(Token.TokenType.COMMA, keyword.toString());}
            case "." -> {createToken(Token.TokenType.PERIOD, keyword.toString());}
            case "String" -> {createToken(Token.TokenType.SYM_STRING, keyword.toString());}
            case "int" -> {createToken(Token.TokenType.SYM_INT, keyword.toString());}
            case "double" -> {createToken(Token.TokenType.SYM_DOUBLE, keyword.toString());}
            case "long" -> {createToken(Token.TokenType.SYM_LONG, keyword.toString());}
            case "var" -> {createToken(Token.TokenType.SYM_VAR, keyword.toString());}
            case "if" -> {createToken(Token.TokenType.SYM_IF, keyword.toString());}
            case "else" -> {createToken(Token.TokenType.SYM_ELSE, keyword.toString());}
            case "void" -> {createToken(Token.TokenType.SYM_VOID, keyword.toString());}
            case "static" -> {createToken(Token.TokenType.SYM_STATIC, keyword.toString());}
            case "public" -> {createToken(Token.TokenType.SYM_PUBLIC, keyword.toString());}
            case "private" -> {createToken(Token.TokenType.SYM_PRIVATE, keyword.toString());}
            case "class" -> {createToken(Token.TokenType.SYM_CLASS, keyword.toString());}
            case "Main" -> {createToken(Token.TokenType.SYM_MAIN, keyword.toString());}
            case "return" -> {createToken(Token.TokenType.SYM_RETURN, keyword.toString());}
            case "print" -> {createToken(Token.TokenType.CMD_PRINT, keyword.toString());}
            case "" -> {advance();}
            default -> createToken(Token.TokenType.IDENTIFIER, keyword.toString());
        }
    }

    private void checkDigit(StringBuilder keyword) {
        while (Character.isDigit(currentChar)) {
            keyword.append(currentChar);
            advance();
        }
        createToken(Token.TokenType.INT, keyword.toString());
    }

    private void checkOperator(StringBuilder keyword) {
        keyword.append(currentChar);
        advance();
        if (keyword.toString().equals("=") && currentChar == '=') {
            keyword.append(currentChar);
            advance();
        }
        checkToken(keyword);
    }

    private void checkKeyword(StringBuilder keyword) {
        while (pos < text.length() && Character.isAlphabetic(currentChar)) {
            keyword.append(currentChar);
            advance();
        }
        checkToken(keyword);
    }

    private void checkSeparator(StringBuilder keyword) {
        keyword.append(currentChar);
        advance();
        checkToken(keyword);
    }

    private void checkWhiteSpace() {
        while (Character.isWhitespace(currentChar) && pos < text.length()) {
            advance();
        }
    }

    private void checkStringLiteral(StringBuilder keyword) {
        if (currentChar == '\"') {
            keyword.append(currentChar);
            advance();
            while (currentChar != '\"') {
                keyword.append(currentChar);
                advance();
            }
            keyword.append(currentChar);
            advance();
            createToken(Token.TokenType.STRINGLITERAL, keyword.toString());
            
        }
    }

    private boolean isSeparator(char ch) {
        return ";(){}[],<>.".indexOf(ch) >= 0;
    }

    private boolean isOperator(char ch) {
        return "=+-*/&|^!".indexOf(ch) >= 0;
    }
}
