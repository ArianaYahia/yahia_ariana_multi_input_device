while True:
    if input.sound_level() > 150:
        music.ba_ding.play_until_done()
    else:
        music.stop_all_sounds()