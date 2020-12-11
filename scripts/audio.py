#!/usr/bin/env python
"""
 Author: MeDicenDav
 https://github.com/medicendav/Dotfiles

   Parametros:
   -Puerto
   -Silencio
   -Subir
   -Bajar
   -Polybar
"""
import argparse

from pulsectl import Pulse

HEADPHONES = "analog-output-headphones"
SPEAKERS = "analog-output-speaker"
SINK_ID = 0


def args_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        description="Manipulación del sonido por medio de una API pulseaudio."
    )
    parser.add_argument(
        "--PORT",
        action="store_true",
        help="Cambiar la salida de puerto.",
    )
    parser.add_argument(
        "--MUTE",
        action="store_true",
        help="Silenciar.",
    )

    parser.add_argument(
        "--UP",
        action="store_true",
        help="Subir volumen",
    )

    parser.add_argument(
        "--DOWN",
        action="store_true",
        help="Bajar volumen",
    )
    return parser.parse_args()


if __name__ == "__main__":
    pulse = Pulse()
    sink = pulse.sink_list()[SINK_ID]
    active_port = sink.port_active.name
    volume = round(sink.volume.value_flat * 100)
    is_muted = sink.mute == 1

    args = args_parser()

    if args.PORT:
        if active_port == SPEAKERS:
            pulse.port_set(sink, HEADPHONES)
        else:
            pulse.port_set(sink, SPEAKERS)

    if args.MUTE:
        if is_muted:
            pulse.mute(sink, mute=False)
        else:
            pulse.mute(sink, mute=True)

    if args.UP:
        if volume < 150:
            pulse.volume_change_all_chans(sink, +0.05)
            volume = round(sink.volume.value_flat * 100)

    if args.DOWN:
        pulse.volume_change_all_chans(sink, -0.05)
        volume = round(sink.volume.value_flat * 100)

    volume = round(sink.volume.value_flat * 100)
    if not is_muted:
        if active_port == SPEAKERS:
            print(f"   {volume}%")
        else:
            print(f"   {volume}%")
    else:
        print("Mute")
