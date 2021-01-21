while (true) {
    if (input.soundLevel() > 150) {
        music.baDing.playUntilDone()
    } else {
        music.stopAllSounds()
    }
    
}
