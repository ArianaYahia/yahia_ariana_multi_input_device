while (true) {
    if (input.temperature(TemperatureUnit.Fahrenheit) < 40 || input.soundLevel() > 150) {
        music.magicWand.playUntilDone()
    } else {
        music.stopAllSounds()
    }
    
}
