fun main() {
    val dog = Dogs("Black", "Pug")
}

private open class Animals {
    var color : String = ""
    constructor(color: String) {
        this.color = color
        println("This is Animal: $color")
    }
}
private class Dogs : Animals {
    var breed : String = ""
    constructor(color: String, breed: String): super(color) {
        this.breed = breed
        println("This is Dog: $color, $breed")
    }
}