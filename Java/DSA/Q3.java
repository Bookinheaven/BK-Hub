public class Q3 {
    public static boolean  palindromeChecker(String value){
        int n = value.length();
        char[] stack = new char[n];
        int top = -1;
        for (char c : value.toCharArray()){
            stack[++top] = c;
        }
        StringBuilder checker = new StringBuilder();
        while (top >= 0) { 
            checker.append(stack[top--]);
        }
        return value.equals(checker.toString());
    }
    public static void main(String[] args) {
        System.out.println(palindromeChecker("malayalam"));
    }    
}
