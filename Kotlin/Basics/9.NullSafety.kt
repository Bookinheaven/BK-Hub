fun main(){
    var ull :String? = "Hello"
//    ull = null
//    val length: Int? = ull?.length
    val length: Int = ull?.length ?: 0
    println(length)
}