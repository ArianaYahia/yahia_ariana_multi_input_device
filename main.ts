while (true) {
    if (input.temperature(TemperatureUnit.Fahrenheit) < 40 || input.soundLevel() > 100) {
        light.showAnimation(light.rainbowAnimation, 100) && music.magicWand.playUntilDone()
    } else {
        music.stopAllSounds() && light.clear()
    }
    
}
