// with let run apply also


/** Scope Function: 'with'
Property 1: Refer to context object by using 'this'
Property 2: The return value is the 'lambda result'  */
fun main() {
    val person = Prson()

    val bio: String = with(person) {
        println(name)
        println(age)
        age + 5
        "He is a freak who loves to teach in his own way" // will be returned and stored in 'bio' String variable
    }

    /** Scope Function: 'apply'
    Property 1: Refer to context object by using 'this'
    Property 2: The return value is the 'context object'  */

    person.also {
        it.name = "Shreks from Smartherd"
        println("New name: ${it.name}")     // prints   New name: Shreks from Smartherd
    }
    /** Scope Function: 'also'              'ALSO PERFORM THE FOLLOWING EXTRA OPERATION'
    Property 1: Refer to context object by using 'it'
    Property 2: The return value is the 'context object'  */

    // Initialise numbersList
    val numbersList: MutableList<Int> = mutableListOf(1, 2, 3)

    // Some other code... may be a function call or program to swap numbers (doesn't matter what code)

    // Operations on the 'numbersList'
    val duplicateNumbers = numbersList.also {
        println("The list elements are: $it")
        it.add(4)
        println("The list elements after adding an element: $it")
        it.remove(2)
        println("The list elements after removing an element: $it")
    }

    // duplicateNumbers will be same as numbersList
    println("Original numbers: $numbersList")
    println("Duplicate numbers: $duplicateNumbers")

    /** Scope Function: 'let'
    Property 1: Refer to context object by using 'it'
    Property 2: The return value is the 'lambda result'  */

    // Use 'let' function to avoid NullPointerException

    val name: String? = "Hello"

    // Execute the lambda expression only if the 'name' variable is NOT NULL
    val stringLength = name?.let {
        println(it.reversed())
        println(it.capitalize())
        it.length       // Will be returned and stored within stringLength variable
    }

    println(stringLength)

    /** Scope Function: 'run'
    Property 1: Refer to context object by using 'this'
    Property 2: The return value is the 'lambda result'  */

    // 'run' is combination of 'with' and 'let'
    // If you want to operate on a Nullable object and avoid NullPointerException then use 'run'

    val person1: Prson? = Prson()

    val bios = person1?.run {
        println(name)
        println(age)
        age + 5
        "He is a freak who loves to teach in his own way"   // will be returned and stored in 'bio' variable
    }

    println(bios)
}
class Prson {
    var name: String = "Sriyank Siddhartha"
    var age: Int = 26
}

