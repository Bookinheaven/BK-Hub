fun add(a: Int, b: Int): Int {
    return a + b
}

fun main() {
    val sum = add(5, 3)
    println("Sum: $sum")
    fun sub (a : Int, b: Int) : Int = if(a > b) a-b else b-a
    println("Sub: ${sub(10,40)}")
    }
//tailrec function for preventing stack overflow by doing actions internally