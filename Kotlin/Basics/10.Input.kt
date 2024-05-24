fun main(){
    println("Enter a list of numbers: ")
    val inputs = ((readlnOrNull())?.trim())?.split(" ")
    val final = mutableListOf<String>()
    if (!inputs.isNullOrEmpty()) {
        for (x in inputs) {
            if (x.isNotEmpty()) {
                final.add(x)
            }
        }
    }
    println(final)
}