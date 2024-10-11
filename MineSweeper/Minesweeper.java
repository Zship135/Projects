import java.awt.*;
import java.awt.event.*;
import java.util.ArrayList;
import java.util.Random;
import javax.swing.*;

public class Minesweeper {

    int tileSize = 40;
    public static int numRows = 12;
    public static int numCols = 12;
    public int boardWidth = numCols * tileSize;
    int boardHeight = numRows * tileSize;
    public static int mineCount = 15;
    int tilesClicked = 0;
    boolean gameOver = false;

    MineTile[][] board = new MineTile[numRows][numCols];
    ArrayList<MineTile> mineList = new ArrayList<>(); // Initialize mineList
    JFrame frame = new JFrame();
    JLabel textLabel = new JLabel();
    JButton resetButton = new JButton("Reset");
    JPanel textPanel = new JPanel();
    JPanel boardPanel = new JPanel();
    Random random = new Random();

    public class MineTile extends JButton {
        int r;
        int c;

        public MineTile(int r, int c) {
            this.r = r;
            this.c = c;
        }
    }

    Minesweeper() {

        frame.setSize(boardWidth, boardHeight + 50); // Increase height to accommodate reset button
        frame.setLocationRelativeTo(null);
        frame.setResizable(false);
        frame.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
        frame.setLayout(new BorderLayout());

        textLabel.setFont(new Font("Arial", Font.BOLD, 25));
        textLabel.setHorizontalAlignment(JLabel.CENTER);
        textLabel.setText("Minesweeper: " + mineCount);
        textLabel.setOpaque(true);

        textPanel.setLayout(new BorderLayout());
        textPanel.add(textLabel, BorderLayout.CENTER);
        textPanel.add(resetButton, BorderLayout.EAST);

        resetButton.setFocusable(false);
        resetButton.addActionListener(e -> resetGame());

        boardPanel.setLayout(new GridLayout(numRows, numCols));

        initializeBoard();

        frame.add(boardPanel, BorderLayout.CENTER);
        frame.add(textPanel, BorderLayout.NORTH);
        frame.setVisible(true);

        setMines();
    }

    void initializeBoard() {
        boardPanel.removeAll();
        mineList.clear();
        tilesClicked = 0;
        gameOver = false;
        textLabel.setText("Minesweeper: " + mineCount);

        for (int r = 0; r < numRows; r++) {
            for (int c = 0; c < numCols; c++) {
                MineTile tile = new MineTile(r, c);
                board[r][c] = tile;

                tile.setFocusable(false);
                tile.setMargin(new Insets(0, 0, 0, 0));
                tile.setFont(new Font("Arial Unicode MS", Font.PLAIN, tileSize / 2));

                tile.addMouseListener(new MouseAdapter() {
                    @Override
                    public void mousePressed(MouseEvent e) {
                        if (gameOver) {
                            return;
                        }
                        MineTile tile = (MineTile) e.getSource();

                        // Left click
                        if (e.getButton() == MouseEvent.BUTTON1) {
                            if (tile.getText().equals("")) {
                                if (mineList.contains(tile)) {
                                    revealMines();
                                    textLabel.setText("GAME OVER");
                                } else {
                                    checkMine(tile.r, tile.c);
                                }
                            }
                        } else if (e.getButton() == MouseEvent.BUTTON3) {
                            if (tile.getText().equals("") && tile.isEnabled()) {
                                tile.setText("🚩");
                            } else if (tile.getText().equals("🚩")) {
                                tile.setText("");
                            }
                        }
                    }
                });

                boardPanel.add(tile);
            }
        }
        boardPanel.revalidate();
        boardPanel.repaint();
    }

    void setMines() {
        int mineLeft = mineCount;

        while (mineLeft > 0) {
            int r = random.nextInt(numRows);
            int c = random.nextInt(numCols);

            MineTile tile = board[r][c];
            if (!mineList.contains(tile)) {
                mineList.add(tile);
                mineLeft--;
            }
        }
    }

    void revealMines() {
        for (MineTile tile : mineList) {
            tile.setText("💣");
        }
        gameOver = true;
    }

    void checkMine(int r, int c) {
        if (r < 0 || r >= numRows || c < 0 || c >= numCols) {
            return;
        }

        MineTile tile = board[r][c];

        if (!tile.isEnabled()) {
            return;
        }

        tile.setEnabled(false);
        tilesClicked++;

        int minesFound = 0;

        // top 3
        minesFound += countMine(r - 1, c - 1); // top left
        minesFound += countMine(r - 1, c);     // top center
        minesFound += countMine(r - 1, c + 1); // top right

        // left and right
        minesFound += countMine(r, c - 1); // left
        minesFound += countMine(r, c + 1); // right

        // bottom 3
        minesFound += countMine(r + 1, c - 1); 
        minesFound += countMine(r + 1, c);
        minesFound += countMine(r + 1, c + 1);

        if (minesFound > 0) {
            tile.setText(Integer.toString(minesFound));
        } else {
            tile.setText("");

            // top 3
            checkMine(r - 1, c - 1);
            checkMine(r - 1, c);
            checkMine(r - 1, c + 1);

            // left and right
            checkMine(r, c + 1);
            checkMine(r, c - 1);

            // bottom 3
            checkMine(r + 1, c - 1);
            checkMine(r + 1, c);
            checkMine(r + 1, c + 1);
        }

        if (tilesClicked == numRows * numCols - mineList.size()) {
            gameOver = true;
            textLabel.setText("Mines Clear!");
            revealMines();
        }
    }

    int countMine(int r, int c) {
        if (r < 0 || r >= numRows || c < 0 || c >= numCols) {
            return 0;
        }
        if (mineList.contains(board[r][c])) {
            return 1;
        }
        return 0;
    }

    void resetGame() {
        initializeBoard();
        setMines();
    }
}
