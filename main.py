while True:
    if input.temperature(TemperatureUnit.FAHRENHEIT) <= 40:
        music.magic_wand.play()
    if input.sound_level() >= 150:
        light.show_animation(light.rainbowAnimation, 100)

        