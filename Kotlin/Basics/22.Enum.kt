
//enum class CreditCardType { // to store same type of constant values
//    SILVER, //ordinal - 0 name = "SILVER"
//     GOLD, // 1
//    PLATINUM //2
//}

interface ICardCashBack {
    fun getCashback(): Float
}
enum class CreditCardType (var colors: String, var maxl : Int = 1000000): ICardCashBack{
    SILVER("gray",400000) {
        override fun getCashback(): Float {
            return 0.02f
        }
    },
    GOLD("gold"){
        override fun getCashback(): Float {
            return 0.04f
        }
    },

    PLATINUM("black"){
        override fun getCashback(): Float = 0.09f
    },
}
fun main() {
    var color : CreditCardType = CreditCardType.SILVER

    println(CreditCardType.GOLD.ordinal)
    println(CreditCardType.GOLD.name) //or
    println(CreditCardType.GOLD)

    val num : Array<CreditCardType> = CreditCardType.values()
    num.forEach { println(it) }

    println(CreditCardType.GOLD.colors)
    println(CreditCardType.GOLD.getCashback())
}

