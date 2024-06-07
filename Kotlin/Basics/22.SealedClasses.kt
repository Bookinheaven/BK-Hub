sealed class Shape { // By default its private and abstract
    class Circle(var radius: Float): Shape() // we can keep them outside too but not outside the file or packages
    class Square(var side: Float): Shape()

    object NotShape : Shape()
//    sealed class Lines: Shape() {}
//    sealed interface Draw

}
class Rectangle(var length: Float,var breadth: Float): Shape()
fun main() {
    val circle = Shape.Circle(3.0F)
    val square = Shape.Square(20f)
    val rectangle = Rectangle(20.0f, 20.0f)
    val notShap = Shape.NotShape
    checkShape(notShap)
}
fun checkShape(shape: Shape) {
    when(shape) {
        is Shape.Square -> println("Square area is ${shape.side*shape.side}")
        is Shape.Circle -> println("Circle area is ${shape.radius*shape.radius}")
        is Rectangle -> println("Rectangle area is ${shape.breadth*shape.length}")
        Shape.NotShape -> println("Shape Not Found")
        else -> {}
    }
}
