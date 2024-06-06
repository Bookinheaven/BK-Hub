fun main() {
    val na = Indian()
}
// This will be visible inside the module (like the whole kotlin files currently working)
//internal fun run() {}
//internal class Person {}

// Originally the class or function is actually in public ie anyone can access the class or function from outside the class
//private fun run() {}
//private class Person {}

open class Person {
    private val a = 1 // Except for this no one can use this property
    protected val b = 1 // except inherited we can't use this property outside this class
    internal val c = 3
    val d = 10

}
class Indian: Person() {
    // a is not visible
    // b,c,d is visible
    init {
        println("${c}, ${b}, ${d}")
    }
}
