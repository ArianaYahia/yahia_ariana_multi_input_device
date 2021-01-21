if (input.temperature(TemperatureUnit.Fahrenheit) < 40 || input.soundLevel() > 150) {
    music.baDing.playUntilDone()
} else {
    music.stopAllSounds()
}

