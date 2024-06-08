fun main() {

    val pro = Prog()
//    pro.reverseDisplay("Hello") { s: String -> s.reversed() }
    pro.reverseDisplay("Hello") { it.reversed() } // only if we have one parameter
}

class Prog {
    fun reverseDisplay(str: String, action: (String) -> String){
        val result = action(str)
        println(result)
    }
}