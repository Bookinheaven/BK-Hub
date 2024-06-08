fun main() {
    val mynums: List<Int> = listOf(1,2,6,4,5)
    val check1: Boolean = mynums.all { it > 2 }
    println(check1)
    val check2: Boolean = mynums.any { it > 2 }
    println(check2)
    val check3 = mynums.count { it > 2 }
    println(check3)
    val check4 = mynums.find { it > 2 }
    println(check4)

}