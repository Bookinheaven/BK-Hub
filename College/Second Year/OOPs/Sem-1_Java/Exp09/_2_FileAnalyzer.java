import java.io.File;
import java.util.Scanner;

public class _2_FileAnalyzer {

    private int spaceCount = 0;
    private int wordCount = 0;
    private int punctuationCount = 0;

    public void analyzeFile(String filename) {
        try {
            File file = new File(filename);
            Scanner fileSc = new Scanner(file);

            while (fileSc.hasNextLine()) {
                String line = fileSc.nextLine();

                String[] wordsArray = line.split("\\s+");
                wordCount += wordsArray.length;

                for (char letter : line.toCharArray()) {
                    if (letter == ' ') {
                        spaceCount++;
                    } else if (",.?!;:'\"-".indexOf(letter) >= 0) {
                        punctuationCount++;
                    }
                }
            }
            fileSc.close();
        } catch (Exception e) {
            e.printStackTrace();
        }
    }

    public void displayCounts() {
        System.out.println("Number of spaces: " + spaceCount);
        System.out.println("Number of words: " + wordCount);
        System.out.println("Number of punctuation marks: " + punctuationCount);
    }

    public static void main(String[] args) {
        _2_FileAnalyzer analyzer = new _2_FileAnalyzer();
        String filename = "Sample.txt";
        
        analyzer.analyzeFile(filename);
        analyzer.displayCounts();
    }
}
