while True:
    if input.temperature(TemperatureUnit.FAHRENHEIT) <= 40 or input.sound_level() >= 150:
        music.magic_wand.play()
        