package com.example.learn

data class SongsModel(var SongTitle : String, var SongDuration: Double, var SongArtist: String, var ExtraField: String)

object TestSongs {
    val songs = listOf<SongsModel>(
        SongsModel("wanna be", 2.23, "BurnKnuckle", "Added 10 days back"),
        SongsModel("IDK", 3.23, "BurnKnuckles", "Added 20 days back")

    )
}