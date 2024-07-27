
// Superclass
class Animal {
    public void eat() {
        System.out.println("This animal eats food.");
    }
}

// Subclass
class Dog extends Animal {
    public void bark() {
        System.out.println("The dog barks.");
    }
}

public class _2_Inheritance {
    public static void main(String[] args) {
        Dog dog = new Dog();
        dog.eat();
        dog.bark();
    }    
}
