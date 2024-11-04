public class Q4 {
    public static boolean checkBrackets(String value){
        int n = value.length();
        char[] stack = new char[n];
        int top = -1;
        for(char ch : value.toCharArray()){
            if (ch == '(' || ch == '{' || ch == '[') {
                stack[++top] = ch;
            }
            else if (ch == ')' || ch == '}' || ch == ']') {
                if (top == -1 || !isMatchingPair(stack[top--], ch)) {
                    return false;
                }
            }
        }
        return top == -1;
    }
    private static boolean isMatchingPair(char opening, char closing) {
        return (opening == '(' && closing == ')') ||
               (opening == '{' && closing == '}') ||
               (opening == '[' && closing == ']');
    }
    public static void main(String[] args) {
        String expression1 = "{[()]}";
        String expression2 = "{[(])}";
        
        System.out.println("Expression 1 is " + (checkBrackets(expression1) ? "balanced" : "not balanced"));
        System.out.println("Expression 2 is " + (checkBrackets(expression2) ? "balanced" : "not balanced"));
    }
}