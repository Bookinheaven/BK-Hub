//val pi : Float = 3.14f // if we dont use it memory waste
val pi : Float by lazy { // until we use, it will not be initialized. we can use val or var and it allows nullable
    3.14f
}

fun main (){
    val nam = Sam()
    nam.name = "BK"
    println(nam.name)
}

class Sam {
    lateinit var name: String // non nullable data type
}