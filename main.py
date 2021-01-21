while True:
    if input.temperature(TemperatureUnit.FAHRENHEIT) <= 40 or input.sound_level() >= 150:
        music.magic_wand.play()
    else:
        music.stop_all_sounds()