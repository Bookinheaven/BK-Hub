
interface Drivable {
    val maxSpeed: Double
    fun drive(): String
    fun brake() {
        println("This drivable is braking")
    }
}

open class Cars(override val maxSpeed:Double, val name: String, val brand: String ): Drivable {
    open var range: Double = 0.0
    fun extendRange(amount: Double) {
        if (amount > 0)
            range += amount
    }

    open fun drive(distance: Double) {
        println("Drove for $distance KM")
    }

    override fun drive(): String {
        return "Drive"
    }
}
class ElectricCars(maxSpeed:Double, name: String, Brand: String, batterylife: Double) : Cars(maxSpeed,name, Brand) {
    override var range = batterylife * 6
    override fun drive(distance: Double) {
        //super.drive(distance)
        println("Drove for $distance KM on Electricity")
    }

    override fun drive(): String {
        return "Drove for $range KM on Electricity"
    }
}
fun main(){
    var car1 = Cars(200.0,"A3", "Audi")
    var car2 = ElectricCars(200.0,"S-Model", "Tesla", 85.0)
    car2.extendRange(200.0)
    car1.drive((200.0))
    car2.drive((200.0))
    car2.drive()
}