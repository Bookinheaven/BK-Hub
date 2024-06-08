fun main() {
    val pro = Program()
    var result = 0
    pro.addTwoNumbers(2, 7)
    pro.addTwoNumbers(1, 10, object : MyInterface {
        override fun execute(sum: Int) {
            println(sum)
        }
    })
    val mylmd: (Int) -> Unit = { s : Int -> println(s)} // lambda
                // parameter int and return unit(void)
    pro.addTwoNumbers(1,4, mylmd)

    pro.addTwoNumbers(12,4) { a, b -> result = a + b} // Closure: we can modify outside variable ie result.
    println(result)
}

class Program {
    fun addTwoNumbers(a: Int, b: Int, action : (Int, Int) -> Unit) { // higher order function
        action(a,b)

    }
    fun addTwoNumbers(a: Int, b: Int, action : (Int) -> Unit) { // higher order function
        val sum = a + b
        action(sum)
//        println(sum)
    }

    fun addTwoNumbers(a: Int, b: Int, action: MyInterface) {
        val sum = a + b
        action.execute(sum)
//        println(sum)
    }
    fun addTwoNumbers(a: Int, b: Int) {
        val sum = a + b
        println(sum)
    }
}
interface MyInterface {
    fun execute(sum: Int)
}
