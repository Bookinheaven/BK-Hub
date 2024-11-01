public class Q2 {
    public static String reversed(String value){
        char stack [] = new char[value.length()];
        int top = -1;
        for(char c : value.toCharArray()){
            stack[++top] = c;
        }
        StringBuilder rs = new StringBuilder(); 
        while(top >= 0){
            rs.append(stack[top--]);
        }
        return rs.toString();
    }
    public static void main(String[] args) {
        System.out.println(reversed("Hello"));
    }    
}
