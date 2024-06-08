fun main() {
    // Elements   0    0    0    0    0
    // Index      0    1    2    3    4
    var myarray = Array<Int>(5) { 0 } // Mutable and fixed size
    myarray[3] = 12
    // Elements   0    0    0   12    0
    // Index      0    1    2    3    4

    var mylist = listOf<String>("Mds", "MUSIC") // Immutable, Fixed size ,Read only

    var mylist2 = mutableListOf<Int>(1,2,3,4,5,6) // mutable, no fixed size
    mylist2.add(8)
    mylist2.add(2, 10)
    mylist2.remove(4)

    // All are similar
//    var mylist3: MutableList<Int> = mutableListOf<Int>(1,2,3,4,5,6)
//    var mylist3: ArrayList<Int> = ArrayList<Int>(1,2,3,4,5,6)
//    var mylist3: ArrayList<Int> = arrayListOf<Int>(1,2,3,4,5,6)

    var mymap = mapOf<Int, String>(1 to "Hello", 2 to " GTA") // Immutable
    println(mymap.keys) // [1,2]
    println(mymap[1])// or mymap.get(1)

    var myhash = hashMapOf<Int, String>() // Mutable, no fixed size
    myhash.put(1, "Hello")
    myhash[2] = "GTA"

    var mymuthash = mutableMapOf<Int, String>() // returns a linked hash map
    // set contains unique elements
    // Hashset contains unique elements but not in sequence is not same every time
    var myset = setOf<Int>(1,2,3,4) // Immutable and Read only
    var myset1 = mutableSetOf<Int>(1,2,3,4) // mutable, read and write
}