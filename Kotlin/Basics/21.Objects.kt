fun main() {
    val sp = HelloWorld.count
    println(sp)
    val sd = HelloWorld.typeOfCustomers()
    println(sd)
    HelloWorld.myMethod("BK")
}
open class Superclass {
    open fun myMethod(str: String){
        println("Up!")
    }
}
object HelloWorld : Superclass(){
    var count = -1
    fun typeOfCustomers() : String {
        return "Indian"
    }

    override fun myMethod(str: String) {
        super.myMethod(str)
        println("Object : $str")
    }
}
// inside the class we need to use companion object