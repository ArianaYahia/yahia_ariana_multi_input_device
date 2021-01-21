while True:
    if input.temperature(TemperatureUnit.FAHRENHEIT) <= 68 or input.sound_level() >= 150:
        music.magic_wand.play_until_done()
    else: 
        music.stop_all_sounds()
        