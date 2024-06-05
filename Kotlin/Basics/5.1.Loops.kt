fun main() {
    for (i in 1..5) {
        println(i)
    }
    var num: Byte = 10
    while (num>=1) {
        println(num)
        num--
    }
    val a = 6
    when (a) {
        in 1..6 -> println("its in 1 to 6")
        7 -> {
            println("its 7")
        }
        else -> println("its idk")

    }
}
