while True:
    if input.temperature(TemperatureUnit.FAHRENHEIT) <= 40 or input.sound_level() >= 100:
        music.ba_ding.play_until_done()
    elif input.temperature(TemperatureUnit.FAHRENHEIT) > 40 or input.sound_level() < 100:
        music.stop_all_sounds()