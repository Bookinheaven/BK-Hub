package com.example.burnknuckle

import android.annotation.SuppressLint
import android.app.DatePickerDialog
import android.icu.util.Calendar
import android.os.Bundle
import android.widget.Button
import android.widget.TextView
import android.widget.Toast
import androidx.activity.enableEdgeToEdge
import androidx.appcompat.app.AppCompatActivity
import androidx.core.view.ViewCompat
import androidx.core.view.WindowInsetsCompat
import java.text.SimpleDateFormat
import java.util.Locale

class MainActivity : AppCompatActivity() {
    @SuppressLint("SetTextI18n")
    private var tvselectedDate : TextView? = null
    private var tvmins : TextView? = null
    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        enableEdgeToEdge()
        setContentView(R.layout.activity_main)
        ViewCompat.setOnApplyWindowInsetsListener(findViewById(R.id.main)) { v, insets ->
            val systemBars = insets.getInsets(WindowInsetsCompat.Type.systemBars())
            v.setPadding(systemBars.left, systemBars.top, systemBars.right, systemBars.bottom)
            insets
        }
        val btnDatepicker : Button = findViewById(R.id.Date_Selector_button)
        tvselectedDate = findViewById(R.id.date1)
        btnDatepicker.setOnClickListener {
            clickDatePicker()
            tvmins = findViewById(R.id.mintsout)
            tvmins?.text = "Hlo"
        }

    }
    private fun clickDatePicker(){
        val myCalendar = Calendar.getInstance()
        val year = myCalendar.get(Calendar.YEAR)
        val month = myCalendar.get(Calendar.MONTH)
        val day = myCalendar.get(Calendar.DAY_OF_MONTH)
        val dpt = DatePickerDialog(this, { _, selectedYear, selectedMonth, selecteddayOfMonth ->
            Toast.makeText(this, "Year: $selectedYear, Month $selectedMonth Day $selecteddayOfMonth", Toast.LENGTH_LONG).show()
            val selectedDate = "$selecteddayOfMonth-$selectedMonth-$selectedYear"
            tvselectedDate?.text = selectedDate
            val sdf = SimpleDateFormat("dd-MM-yyyy", Locale.ENGLISH)
            val theDate = sdf.parse(selectedDate)
            theDate?.let {
                val selectedmins = theDate.time / 60000
                val current = sdf.parse(sdf.format(System.currentTimeMillis()))
                current?.let {
                    val difMin = (current.time / 60000) - selectedmins
                    tvmins?.text = difMin.toString()
                }
            }

                               }, year, month, day)
        dpt.datePicker.maxDate = System.currentTimeMillis() - 8640000
        dpt.show()



//        DatePickerDialog()

    }
}