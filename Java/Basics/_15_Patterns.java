public class _15_Patterns {
    private static void rightTriangle(int num){
        for (int i = 0; i <= num; i++){
            for (int j = 0; j <= i; j++){
                System.out.print("* ");    
            }
            System.out.println();
        }
    }

    private static void rightTriangleShallow(int num){
        for (int i = 0; i <= num; i++){
            for (int j = 0; j <= i; j++){
                System.out.print((j == 0 || j == i || i == num) ? "* ": "  ");
            }
            System.out.println();
        }
    }
    private static void invertedRightTriangel(int num){
        for (int i = num; i >= 0; i--){
            for (int j = 0 ; j <= i; j++ ){
                System.out.print("* ");   
            }
            System.out.println();
        }
    }
    private static void invertedRightTriangelShallow(int num){
        for (int i = num; i >= 0; i--){
            for (int j = 0; j <= i; j++){
                System.out.print((j == 0 || j == i || i == num) ? "* ": "  ");
            }
            System.out.println();
        }
    }

    private static void pyramid(int num) {
        for (int i = 0; i <= num; i++){
            for (int j = 0; j <= num - i; j++){
                System.out.print(" ");
            }
            for (int k = 0; k <= i; k++){
                System.out.print("* ");
            }
            System.out.println();
        }
    }

    private static void pyramidShallow(int num){
        for (int i = 0; i <= num; i++){
            for (int j = 0; j <= num - i; j++){
                System.out.print(" ");
            }
            for (int k = 0; k <= i; k++){
                System.out.print((k == 0 || k == i || i == num) ? "* ": "  ");
            }
            System.out.println();
        }
    }
    private static void diamond(int num){
        for (int i = 0; i <= num; i++){
            for (int j = 0; j <= num - i; j++){
                System.out.print(" ");
            }
            for (int k = 0; k <= i; k++){
                System.out.print("* ");
            }
            System.out.println();
        }
        for (int i = num; i >= 0; i--){
            for (int j = -1; j <= num - i; j++){
                System.out.print(" ");
            }
            for (int k = 1; k <= i; k++){
                System.out.print("* ");
            }
            System.out.println();
        }

    }
    private static void diamondShallow(int num){
        for (int i = 0; i <= num; i++){
            for (int j = 0; j <= num - i; j++){
                System.out.print(" ");
            }
            for (int k = 0; k <= i; k++){
                System.out.print((k == 0 || k == i) ? "* ": "  ");
            }
            System.out.println();
        }
        for (int i = num; i >= 0; i--){
            for (int j = -1; j <= num - i; j++){
                System.out.print(" ");
            }
            for (int k = 1; k <= i; k++){
                System.out.print((k == 1 || k == i) ? "* ": "  ");
            }
            System.out.println();
        }
    }
    private static void square(int num){
        for (int i =0; i <= num;i++){
            for (int j = 0; j<= num; j++){
                System.out.print("* ");
            }
            System.out.println();
        }
    }
    private static void squareShallow(int num){
        for (int i =0; i <= num;i++){
            for (int j = 0; j<= num; j++){
                System.out.print((i == 0 || i == num || j == num || j == 0)? "* ": "  ");
            }
            System.out.println();
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
        System.out.println();
        pyramid(5);
        System.out.println();
        pyramidShallow(5);
        System.out.println();
        diamond(5);
        System.out.println();
        diamondShallow(5);
        System.out.println();
        square(5);
        System.out.println();
        squareShallow(5);
    }    
}
