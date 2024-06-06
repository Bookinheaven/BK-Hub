fun main() {

}

interface MyInterfaceListener { // we cant create instances of interface
    var aka : String // by default abstract
    fun onClick() { // Everything is open in nature and if a function contains body then it's not an abstract thought it is still open
    }
    fun onTouch() {} // this is an abstract because it doesn't have body
}
interface MySInterface { // we cant create instances of interface
    fun onClick()
    fun onTouch() {}
}
open class Test
class Buttons : Test(), MyInterfaceListener, MySInterface {
    override var aka: String = "Aka"
    override fun onClick() {
        super.onClick()
    }

    override fun onTouch() {
        super<MyInterfaceListener>.onTouch()
        super<MySInterface>.onTouch()
    }
}