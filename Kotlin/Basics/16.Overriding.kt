fun main() {
    val dog = Dog()
    dog.eat()
    println(dog.color)

    val animal = Animal()
    animal.eat()
    println(animal.color)
}

open class Animal{
    open val color: String = "White "

    open fun eat(){
        println("Animal is eating!")
    }
}
class Dog: Animal(){
    val breed: String = ""
    override val color = "Black"
    fun bark(){
        println("Bark!")
    }

    override fun eat() {
        super<Animal>.eat() // When we have an interface the compiler will think that eat fun is also present in the interface class so if we mention <Animal> it will only think super for Animal
        println("Dog is eating!")
    }
}