import java.io.File;
import java.io.IOException;
import java.util.ArrayList;
import java.util.List;
import java.util.Scanner;

public class _1_FileSystem {

    private static boolean createFile(String fileName) {
        File save = new File(fileName);
        try {
            return save.createNewFile();
        } catch (IOException e) {
            e.printStackTrace();
        }
        return false;
    }

    private static List<String> openFile(String fileName) {
        List<String> data = new ArrayList<>();
        try {
            File open = new File(fileName);
            Scanner fileSc = new Scanner(open);
            while (fileSc.hasNextLine()) {
                data.add(fileSc.nextLine());
            }
            fileSc.close();
        } catch (Exception e) {
            e.printStackTrace();
        }
        return data;
    }

    private static boolean renameFile(String fileName, String newFileName) {
        File original = new File(fileName);
        File rename = new File(newFileName);
        return original.renameTo(rename);
    }

    private static boolean deleteFile(String fileName) {
        File delete = new File(fileName);
        return delete.delete();
    }

    private static boolean createFolder(String dirName) {
        File file = new File(dirName);
        return file.mkdirs();
    }

    private static String getAbsolutePath(String fileName) {
        File file = new File(fileName);
        return file.getAbsolutePath();
    }

    private static List<String> fileNamesInDir(String dirName) {
        List<String> data = new ArrayList<>();
        File file = new File(dirName);
        File[] list = file.listFiles();
        if (list != null) {
            for (File f : list) {
                data.add(f.getName());
            }
        }
        return data;
    }

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        boolean out = true;

        while (out) {
            System.out.print("Menu:\n1. Create File\n2. Open File\n3. Rename File\n4. Delete File\n5. Create Directory\n6. Absolute Path\n7. Get File List\n8. Exit\nEnter your choice: ");
            int choice = sc.nextInt();
            sc.nextLine();
            switch (choice) {
                case 1 -> {
                    System.out.print("Enter the file name: ");
                    String fileName = sc.nextLine();
                    if (createFile(fileName)) {
                        System.out.println("File created!");
                    } else {
                        System.out.println("File not created!");
                    }
                }
                case 2 -> {
                    System.out.print("Enter the file name: ");
                    String fileName = sc.nextLine();
                    List<String> data = openFile(fileName);
                    data.forEach(System.out::println);
                }
                case 3 -> {
                    System.out.print("Enter the file name: ");
                    String fileName = sc.nextLine();
                    System.out.print("Enter the new file name: ");
                    String newFileName = sc.nextLine();
                    if (renameFile(fileName, newFileName)) {
                        System.out.println("Renamed Successfully!");
                    } else {
                        System.out.println("Failed to rename!");
                    }
                }
                case 4 -> {
                    System.out.print("Enter the file name: ");
                    String fileName = sc.nextLine();
                    if (deleteFile(fileName)) {
                        System.out.println("Deleted Successfully!");
                    } else {
                        System.out.println("Failed to Delete!");
                    }
                }
                case 5 -> {
                    System.out.print("Enter the directory name: ");
                    String dirName = sc.nextLine();
                    if (createFolder(dirName)) {
                        System.out.println("Directory created successfully!");
                    } else {
                        System.out.println("Failed to create directory!");
                    }
                }
                case 6 -> {
                    System.out.print("Enter the file name: ");
                    String fileName = sc.nextLine();
                    System.out.println("Absolute Path: " + getAbsolutePath(fileName));
                }
                case 7 -> {
                    System.out.print("Enter the directory name: ");
                    String dirName = sc.nextLine();
                    List<String> files = fileNamesInDir(dirName);
                    if (!files.isEmpty()) {
                        System.out.println("Files in directory:");
                        files.forEach(System.out::println);
                    } else {
                        System.out.println("No files found or directory does not exist.");
                    }
                }
                case 8 -> out = false;
                default -> System.out.println("Invalid choice. Please enter a valid option.");
            }
        }
        sc.close();
        System.out.println("Exited Program.");
    }
}
