fun main() {
    val mynum : List<Int> = listOf(2,3,4,5,6)

    val mysmallnum: List<Int> = mynum.filter { it > 4 } // { num -> num > 4}
    println(mysmallnum)
    val squares: List<Int> = mynum.map { it * it }
    println(squares)
}