while True:
    if input.temperature(TemperatureUnit.FAHRENHEIT) < 40 or input.sound_level() > 100:
        light.show_animation(light.rainbow_animation, 100) and  music.magic_wand.play_until_done()
    else: 
        music.stop_all_sounds() and light.clear()
    