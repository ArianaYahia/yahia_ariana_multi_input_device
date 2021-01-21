while (true) {
    if (input.temperature(TemperatureUnit.Fahrenheit) <= 68 || input.soundLevel() > 100) {
        music.magicWand.playUntilDone() && light.showAnimation(light.rainbowAnimation, 100)
    } else {
        music.stopAllSounds() && light.clear()
    }
    
}
