
data class User(val LOGID: Int, var NAME: String){

}
fun main(){
    val user1 = User(1, "Tanvik")
    val name = user1.NAME
    println(name)
    user1.NAME = "Burn"
    val user2 = User(2, "Knuckle")

    println(user1.equals(user2))

    println("User Details: $user1")
    val updatedName = user1.copy(NAME="bURN")
    println("${updatedName.component1()} ${updatedName.component2()}")
    val (id, nm) = user2
    println("$id $nm")


}
