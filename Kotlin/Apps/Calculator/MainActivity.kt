package com.example.calculator

import android.os.Bundle
import android.widget.Button
import android.widget.TextView
import androidx.activity.enableEdgeToEdge
import androidx.appcompat.app.AppCompatActivity
import androidx.core.text.isDigitsOnly
import androidx.core.view.ViewCompat
import androidx.core.view.WindowInsetsCompat
import javax.script.ScriptEngineManager
import javax.script.ScriptException
import android.util.Log
import android.widget.Toast

class MainActivity : AppCompatActivity() {
    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        enableEdgeToEdge()
        setContentView(R.layout.activity_main)
        ViewCompat.setOnApplyWindowInsetsListener(findViewById(R.id.main)) { v, insets ->
            val systemBars = insets.getInsets(WindowInsetsCompat.Type.systemBars())
            v.setPadding(systemBars.left, systemBars.top, systemBars.right, systemBars.bottom)
            insets
        }
        val textfield: TextView? = findViewById(R.id.textarea)
        val result: TextView? = findViewById(R.id.result)
        val delButton: Button = findViewById(R.id.delButton)

        val num0Button: Button = findViewById(R.id.num0Button)
        val num1Button: Button = findViewById(R.id.num1Button)
        val num2Button: Button = findViewById(R.id.num2Button)
        val num3Button: Button = findViewById(R.id.num3Button)
        val num4Button: Button = findViewById(R.id.num4Button)
        val num5button: Button = findViewById(R.id.num5Button)
        val num6button: Button = findViewById(R.id.num6Button)
        val num7button: Button = findViewById(R.id.num7Button)
        val num8button: Button = findViewById(R.id.num8Button)
        val num9button: Button = findViewById(R.id.num9Button)

        val addbutton: Button = findViewById(R.id.addButton)
        val subbutton: Button = findViewById(R.id.subButton)
        val mulbutton: Button = findViewById(R.id.mulButton)
        val divbutton: Button = findViewById(R.id.divButton)
        val acbutton: Button = findViewById(R.id.acButton)
        val equalButton : Button = findViewById(R.id.equalButton)

        var pastResult: String
        val listNum = listOf(
            num0Button, num1Button, num2Button, num3Button, num4Button,
            num5button, num6button, num7button, num8button, num9button
        )
        val operators = listOf(addbutton, subbutton, mulbutton, divbutton)


        equalButton.setOnClickListener {
            val currentString = textfield?.text.toString().trim()
//            Toast.makeText(this, currentString, Toast.LENGTH_LONG).show()
            if (result != null) {
                result.text= currentString
            }
        }
        fun findResult(): String {
            var currentString = textfield?.text.toString().trim()
                .replace('−', '-')
                .replace('×', '*')
                .replace('÷', '/')
                .replace('+', '+')

            if (currentString.isEmpty()) {
                Log.e("JavaScript", "Input string is empty")
                return "0"
            }

            if (currentString.last() in listOf('+', '-', '*', '/')) {
                currentString = currentString.substring(0, currentString.length - 1)
            }

            val engineManager = ScriptEngineManager()
            val engine = engineManager.getEngineByName("js")

            Toast.makeText(this, currentString, Toast.LENGTH_SHORT).show()

            return try {
                when (val fresult = engine.eval(currentString)) {
                    is Number -> {
                        val ffresult = fresult.toDouble()
                        if (ffresult == ffresult.toInt().toDouble()) {
                            ffresult.toInt().toString()
                        } else {
                            ffresult.toString()
                        }
                    }
                    else -> {
                        Toast.makeText(this, "Result is not a valid number: $fresult", Toast.LENGTH_SHORT).show()
                        Log.e("JavaScript", "Result is not a valid number: $fresult")
                        "0"
                    }
                }
            } catch (e: ScriptException) {
                Toast.makeText(this, "ScriptException during evaluation", Toast.LENGTH_SHORT).show()
                Log.e("JavaScript", "ScriptException during evaluation", e)
                " "
            } catch (e: Exception) {
                Toast.makeText(this, "Exception during evaluation", Toast.LENGTH_SHORT).show()
                Log.e("JavaScript", "Exception during evaluation", e)
                " "
            }
        }



        for (item in operators) {
            item.setOnClickListener {
                var currentString = textfield?.text.toString().trim()
                if (currentString.isNotEmpty()) {
                    if (currentString.last() != item.text.last()) {
                        if (currentString.last() !in listOf('+', '−', '×', '÷') ){
                            if (textfield != null) {
                                textfield.text = currentString.plus(item.text.last())
                            }
                            pastResult = findResult()
                            result?.text = pastResult
//                            result.text =
                        }
                        else {
                            currentString = currentString.substring(0, currentString.length - 1)
                            if (textfield != null) {
                                textfield.text = currentString.plus(item.text.last())
                            }
                        }
                    }
                }
            }
        }
        for (item in listNum) {
            item.setOnClickListener {
                if (item.text != null) {
                    if (item.text.isDigitsOnly()) {
                        textfield?.append(item.text)
                        pastResult = findResult()
                        result?.text = pastResult
                    }
                }
            }
        }

        delButton.setOnClickListener {
            val currentText = textfield?.text.toString()
            if (currentText.isNotEmpty()) {
                if (textfield != null) {
                    textfield.text = currentText.substring(0, currentText.length - 1)
                    pastResult = findResult()
                    result?.text = pastResult
                }
            }
        }

        acbutton.setOnClickListener {
            if (textfield != null) {
                textfield.text = ""
            }
            if (result != null) {
                result.text=""
            }
        }
    }
}
