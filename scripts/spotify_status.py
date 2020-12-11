#!/usr/bin/env python
from os import path

import dbus

from scripts.lista_enlazada import CircularList

TEMP_FILE = "/tmp/spotify"
STRING_LIMIT = 50
ICONS = {"PLAY": " ", "PAUSE": " "}


def scroll_string(count, complete_string):
    string = ""

    circular_string = CircularList(complete_string)
    iterator_string = iter(circular_string)

    for i in range(STRING_LIMIT):
        string += next(iterator_string)
        string += " " + string
    last = count + STRING_LIMIT
    return string[count:last]


def save_status(string):
    if not path.isfile(TEMP_FILE):
        count = 0
        with open(TEMP_FILE, "w") as file:
            file.write(str(count) + "\n")
            file.write(string)
    else:
        with open(TEMP_FILE, "r") as file:
            data = file.readlines()
            count, string_data = data
            count = int(count)
        count += 1
        if string_data != string:
            string = string_data
            count = 0
        with open(TEMP_FILE, "w") as file:
            file.write(str(count) + "\n")
            file.write(string)
    return count, string


if __name__ == "__main__":

    try:
        session_bus = dbus.SessionBus()
        spotify_bus = session_bus.get_object(
            "org.mpris.MediaPlayer2.spotify", "/org/mpris/MediaPlayer2"
        )

        spotify_properties = dbus.Interface(
            spotify_bus, "org.freedesktop.DBus.Properties"
        )

        metadata = spotify_properties.Get(
            "org.mpris.MediaPlayer2.Player", "Metadata"
        )
        status = spotify_properties.Get(
            "org.mpris.MediaPlayer2.Player", "PlaybackStatus"
        )

    except Exception as error:
        if isinstance(error, dbus.exceptions.DBusException):
            print("  Spotify")
        else:
            print(error)

    if status == "Playing":
        play_pause = ICONS["PLAY"]
    elif status == "Paused":
        play_pause = ICONS["PAUSE"]
    else:
        play_pause = ""
    artist = metadata["xesam:artist"][0] if metadata["xesam:artist"] else ""
    song = metadata["xesam:title"] if metadata["xesam:title"] else ""
    album = metadata["xesam:album"] if metadata["xesam:album"] else ""

    output = f"{artist}   {song} {album}"
    count, string = save_status(output)
    scroll = scroll_string(count, output)
    print(scroll)
