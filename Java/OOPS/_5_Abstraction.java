abstract class Animal {

    public abstract void makeSound();

    // Regular method
    public void sleep() {
        System.out.println("This animal sleeps.");
    }
}

class Dog extends Animal {
    public void makeSound() {
        System.out.println("The dog barks.");
    }
}

public class _5_Abstraction {
    public static void main(String[] args) {
        Animal myDog = new Dog();
        myDog.makeSound();
        myDog.sleep();
    }
}
