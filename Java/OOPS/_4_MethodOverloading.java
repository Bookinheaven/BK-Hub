public class _4_MethodOverloading {
    public static void main(String[] args) {
        Animal myDog = new Dog();
        myDog.makeSound();
    }   
}
class Animal {
    public void makeSound() {
        System.out.println("This animal makes a sound.");
    }
}

class Dog extends Animal {
    @Override
    public void makeSound() {
        System.out.println("The dog barks.");
    }
}
