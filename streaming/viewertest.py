import vlc


def reproducir(file_name):
    Instance = vlc.Instance("--fullscreen")
    player = Instance.media_player_new()
    Media = Instance.media_new(file_name)
    Media.get_mrl()
    player.set_media(Media)
    player.play()

    option = input("Ingrese stop para detener el video\n")
    if(option == "stop"):
        player.stop()
