import kotlinx.coroutines.*
import kotlin.concurrent.thread
//    implementation("org.jetbrains.kotlinx:kotlinx-coroutines-core:1.3.9")
suspend fun main() {
    println("Main program starts: ${Thread.currentThread().name}")
    // worker thread
    thread {
        println("Worker Thread starts: ${Thread.currentThread().name}")
        Thread.sleep(1000)
        println("Worker Thread ends: ${Thread.currentThread().name}")
    }

    var job: Job = GlobalScope.launch {
        println("Worker Thread starts: ${Thread.currentThread().name}")
        delay(  1000)
        println("Worker Thread ends: ${Thread.currentThread().name}")
    }

//    delay(2000) we can't use delay outside because it is a suspend function ie it will work only inside the coroutine or when suspend keyword is present
    runBlocking { // it creates a new coroutine and blocks the thread. it directly blocks the main thread
        delay(2000)
    }
    addDelay()
    job.join() // better way for thread to stop
    println("Main program ends: ${Thread.currentThread().name}")
}

suspend fun addDelay() {
    delay(2000)
}

