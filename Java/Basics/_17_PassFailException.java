class PassException extends Exception {

    public PassException(String message) {
        super(message);   
    }   
}
class FailException extends Exception {

    public FailException(String message) {
        super(message);   
    }   
}
public class _17_PassFailException {
    public static void main(String[] args) throws PassException, FailException {
        int marks = 50;
        try {
            if (marks < 30){
                throw new FailException("Failed");
            } else {
                throw new PassException("passed");
            }
        } catch (FailException | PassException e){
            System.out.println(e.getMessage());
        }   
    }    
}
