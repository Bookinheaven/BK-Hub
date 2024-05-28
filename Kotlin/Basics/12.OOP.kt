fun main() {
    var a = Dumper(fist = "false", kick = "true", dump = "true")
    a.meth1()
    println()
}

class Dumper(fist:String = "true", kick:String= "true"){
    lateinit var star : String
    var dump : String? = "true"
        set(value){
            field = "SET $value"
        }
        get() {
            return "GET $field"
        }
    var dark : String? = "True"
        private set

    init{
        this.star = "HEHE"
        println("Fist: $fist, Kick: $kick")
    }
    constructor(fist: String, kick: String, dump: String = "false"): this(fist, kick) {
        this.dump = dump
        println("Fist: $fist, Kick: $kick, Dump: $dump")
    }
    fun meth1(){
        println(this.dump)
    }

}