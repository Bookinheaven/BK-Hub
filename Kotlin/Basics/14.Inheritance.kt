open class Car(val name: String, val Brand: String){
     open var range: Double = 0.0
    fun extendRange(amount: Double){
        if (amount > 0)
            range += amount
    }
    open fun drive(distance: Double){
        println("Drove for $distance KM")
    }
}
class ElectricCar(name: String, Brand: String, batterylife: Double) : Car(name, Brand){
    override var range = batterylife * 6
    override fun drive(distance: Double) {
        //super.drive(distance)
        println("Drove for $distance KM on Electricity")
    }
    fun drive(){
        println("Drove for $range KM on Electricity")
    }
}

fun main() {
    var car1 = Car("A3", "Audi")
    var car2 = ElectricCar("S-Model", "Tesla", 85.0)
    car2.extendRange(200.0)
    car1.drive((200.0))
    car2.drive((200.0))
    car2.drive()

}
