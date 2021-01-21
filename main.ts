while (true) {
    if (input.temperature(TemperatureUnit.Fahrenheit) <= 68 || input.soundLevel() > 100) {
        music.magicWand.playUntilDone() && light.rainbowAnimation
    } else {
        music.stopAllSounds()
    }
    
}
