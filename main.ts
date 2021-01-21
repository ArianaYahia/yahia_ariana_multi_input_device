while (true) {
    if (input.temperature(TemperatureUnit.Celsius) <= 40 || input.soundLevel() < 100) {
        music.baDing.playUntilDone()
    } else if (input.temperature(TemperatureUnit.Celsius) > 40 || input.soundLevel() > 100) {
        music.stopAllSounds()
    }
    
}
