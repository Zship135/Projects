package src.main.java;

import java.io.IOException;







public class Main {
    public static void main(String[] args) throws IOException {
        
        Lexer lexer = new Lexer();

        lexer.analyze();
    }
}