while True:
    if input.temperature(TemperatureUnit.FAHRENHEIT) <= 68 or input.sound_level() > 100:
        music.magic_wand.play_until_done() and light.rainbow_animation
    else: 
        music.stop_all_sounds()
        