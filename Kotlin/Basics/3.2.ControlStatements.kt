fun main() {
    val a = 2
    val b = 5

//    var maxval :Int = if (a>b) b else a
    var maxval :Int = if (a>b) {
        println("its b")
        b
    } else {
        println("its a")
        a
    }
    println(maxval)
}
