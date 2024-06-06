fun main() {
}
// Abstract class or function is open by nature (default)
abstract class Persons { // we cant create instances of this class
    abstract var dump : String
    abstract fun eat() // They are defined but they cant have initial values
    open fun getHeight() {}
    fun goToSchool() {}
}

class India : Persons() {
    override var dump: String
        get() = "Hello"
        set(value) {}

    override fun eat() {}
    override fun getHeight() {}
}