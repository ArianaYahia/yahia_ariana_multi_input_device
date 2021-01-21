while True:
    if input.temperature(TemperatureUnit.FAHRENHEIT) <= 40:
        music.magic_wand.play()
    if input.sound_level() >= 150:
        light.set_all(light.rgb(255, 255, 0 ))

        