while True:
    if input.temperature(TemperatureUnit.CELSIUS) < 5 or input.sound_level() > 100:
        music.ba_ding.play_until_done()
    else:
        music.stop_all_sounds()