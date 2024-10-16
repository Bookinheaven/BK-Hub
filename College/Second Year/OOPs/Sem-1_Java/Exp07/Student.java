import java.util.Scanner;
public class Student {
    public static void main(String args[]){
        System.out.println("Tanvik URK23CS1261");
        Scanner sc = new Scanner(System.in);
        System.out.println("Enter student name : ");
        try{
            if(sc.nextLine().length() > 7){
                throw new LengthException("length exceeded");
            }
        }catch(LengthException e){
            System.out.println(e);
        }
        System.out.println("enter the marks of three subjects : ");
        float avg = (sc.nextInt() + sc.nextInt() + sc.nextInt())/3;
        try{
            if (avg < 50){
                throw new FailedException("failed");
            }
            else if(avg>50 && avg<75){
                throw new NotFirstClassExecption("not a first class");
            }
            else if(avg>75){
                throw new FirstClassException("first class");
            }
        }catch(FailedException | NotFirstClassExecption | FirstClassException e){
            System.out.println(e);
        }

        sc.close();
    }
}


class LengthException extends Exception{
    LengthException(String msg){
        super(msg);
    }
}
class FailedException extends Exception{
    FailedException(String msg){
        super(msg);
    }
}
class NotFirstClassExecption extends Exception{
    NotFirstClassExecption(String msg){
        super(msg);
    }
}
class FirstClassException extends Exception{
    FirstClassException(String msg){
        super(msg);
    }
}
