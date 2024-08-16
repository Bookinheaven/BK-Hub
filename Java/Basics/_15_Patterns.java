public class _15_Patterns {
    private static void rightTriangle(int num){
        for (int i = 0; i <= num; i++){
            for (int j = 0; j <= i; j++){
                System.out.print("* ");    
            }
            System.out.println(" ");
        }
    }

    private static void rightTriangleShallow(int num){
        for (int i = 0; i <= num; i++){
            for (int j = 0; j <= i; j++){
                System.out.print((j == 0 || j == i || i == num) ? "* ": "  ");
            }
            System.out.println(" ");
        }
    }
    private static void invertedRightTriangel(int num){
        for (int i = num; i >= 0; i--){
            for (int j = 0 ; j <= i; j++ ){
                System.out.print("* ");   
            }
            System.out.println(" ");
        }
    }
    private static void invertedRightTriangelShallow(int num){
        for (int i = num; i >= 0; i--){
            for (int j = 0; j <= i; j++){
                System.out.print((j == 0 || j == i || i == num) ? "* ": "  ");
            }
            System.out.println(" ");
        }
    }

    public static void main(String[] args) {
        rightTriangle(5);
        System.out.println();
        rightTriangleShallow(5);
        System.out.println();
        invertedRightTriangel(5);
        System.out.println();
        invertedRightTriangelShallow(5);
    }    
}
