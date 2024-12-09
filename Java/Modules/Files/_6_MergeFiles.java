/*
 * Write a Java program to do the following operations:

a) Write the following content into a file named first.txt. “A stream is a
communication channel that a program has with the outside world. It is used to
transfer data items in succession.”
b) Create another file named second.txt which contains the following content. “An
Input/Output (I/O) Stream represents an input source or an output destination.
A stream can represent many different kinds of sources and destinations,
including disk files, devices, other programs, and memory arrays.”
c) Now, merge the content of above two files and put the same into final.txt.
 */

import java.io.File;
import java.io.FileWriter;
import java.util.ArrayList;
import java.util.Scanner;

public class _6_MergeFiles {
    public static void createFileOne(String fileName, String data){
        try (FileWriter fw = new FileWriter(fileName);){
            fw.write(data);
        } catch (Exception e) {
            System.out.println("Error: %s".formatted(e.getMessage()));
        }   
    }
    public static void mergeFiles(String file1, String file2){
        File f1 = new File(file1);
        File f2 = new File(file2);
        try (Scanner fsc1 = new Scanner(f1);Scanner fsc2 = new Scanner(f2);FileWriter fw = new FileWriter("NewData.txt");){
            ArrayList newData = new ArrayList<String>();
            while(fsc1.hasNextLine()) {
                newData.add(fsc1.nextLine());
            }
            while(fsc2.hasNextLine()) {
                newData.add(fsc2.nextLine());
            }
            fw.write(String.join("\n", newData));
        } catch (Exception e) {
            System.out.println("Error: %s".formatted(e.getMessage()));
        }  
    }
    public static void main(String[] args) {
        createFileOne("first.txt", "A stream is a communication channel that a program has with the outside world. It is used to transfer data items in succession.");
        createFileOne("second.txt", "An Input/Output (I/O) Stream represents an input source or an output destination. A stream can represent many different kinds \nof sources and destinations, including disk files, devices, other programs, and memory arrays.");
        mergeFiles("first.txt", "second.txt");
        
    }
}
