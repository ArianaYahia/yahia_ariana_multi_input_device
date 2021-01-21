while (true) {
    if (input.temperature(TemperatureUnit.Celsius) < 5 || input.soundLevel() > 100) {
        music.baDing.playUntilDone()
    } else {
        music.stopAllSounds()
    }
    
}
