package com.example.learn

import android.os.Bundle
import androidx.activity.enableEdgeToEdge
import androidx.appcompat.app.AppCompatActivity
import androidx.recyclerview.widget.LinearLayoutManager
import androidx.recyclerview.widget.RecyclerView

class MusicLibraryActivity: AppCompatActivity() {
    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        setContentView(R.layout.activity_music_library)
        enableEdgeToEdge()
        val LayoutManager = LinearLayoutManager(this)
        LayoutManager.orientation = LinearLayoutManager.VERTICAL

        val recyclerView = findViewById<RecyclerView>(R.id.musicRecyclerView)
        recyclerView.layoutManager = LayoutManager

        val adpater = SongsAdapter(this, TestSongs.songs)
        recyclerView.adapter = adpater
    }
}
