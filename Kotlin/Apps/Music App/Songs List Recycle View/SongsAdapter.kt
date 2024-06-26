package com.example.learn

import android.annotation.SuppressLint
import android.content.Context
import android.view.LayoutInflater
import android.view.View
import android.view.ViewGroup
import android.widget.ImageButton
import android.widget.TextView
import android.widget.Toast
import androidx.recyclerview.widget.RecyclerView

class SongsAdapter(private val context: Context, private val songs: List<SongsModel>) : RecyclerView.Adapter<SongsAdapter.SongsViewHolder>(){

    override fun onCreateViewHolder(parent: ViewGroup, viewType: Int): SongsViewHolder {
        val view = LayoutInflater.from(context).inflate(R.layout.songs_item, parent, false)
        return SongsViewHolder(view)
    }

    override fun getItemCount(): Int {
        return songs.size
    }

    override fun onBindViewHolder(holder: SongsViewHolder, position: Int) {
        val song = songs[position]
        holder.setData(song, position)
    }
    inner class SongsViewHolder(itemView: View) : RecyclerView.ViewHolder(itemView){
        private var currentSong : SongsModel? = null
        var currentPosition: Int = 0
        init {
            val songMenu : ImageButton = itemView.findViewById(R.id.songMenu)
            songMenu.setOnClickListener {
                Toast.makeText(context,  "${currentSong!!.SongTitle} Song Menu Clicked! ", Toast.LENGTH_SHORT).show()
            }
            itemView.setOnClickListener {
                Toast.makeText(context, currentSong!!.SongTitle + "Clicked! ", Toast.LENGTH_SHORT).show()
            }
        }
        @SuppressLint("SetTextI18n")
        fun setData(song : SongsModel?, position: Int){
            val songTitle : TextView = itemView.findViewById(R.id.songTitle)
            val songDescription : TextView = itemView.findViewById(R.id.SongDescription)
            songTitle.text = song!!.SongTitle
            songDescription.text = "${song.SongArtist} * ${song.SongDuration}"
            currentSong = song
            currentPosition = position
        }
    }

}