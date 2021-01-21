while True:
    if input.temperature(TemperatureUnit.CELSIUS) < 7 or input.sound_level() > 100:
        light.show_animation(light.rainbow_animation, 100)
        music.magic_wand.play_until_done()
    else: 
        music.stop_all_sounds() 
        light.clear()
    