fun main() {
    var person = Personss()
//    person.age = 18
//    person.name= "Who"
    with(person){
        name = "Who"
        age = 18
    }
    person.apply { // it can also call methods
        name = "Who"
        age = 18
    }.startRun()
}
class Personss {
    var name : String = ""
    var age: Int = -1

    fun startRun(){
        println("I am on run")
    }
}