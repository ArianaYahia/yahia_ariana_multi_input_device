while (true) {
    if (input.temperature(TemperatureUnit.Fahrenheit) <= 40) {
        music.magicWand.play()
    }
    
    if (input.soundLevel() >= 150) {
        light.showAnimation(light.rainbowAnimation, 100)
    }
    
}
