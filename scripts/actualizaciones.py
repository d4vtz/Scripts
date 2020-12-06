#!/usr/bin/env python
"""
Autor: MedicenDav
Dotfiles: github.com/medicendav/Dotfiles
"""
import argparse

import requests
from bs4 import BeautifulSoup

from scripts.procesos.comandos import cmd_output

# Comandos para mostrar paquetes a actualizar.
PACMAN = "checkupdates"
AUR = "yay -Qum"


def args_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        description="Actualizaciones de Archlinux."
    )
    parser.add_argument(
        "--PACMAN",
        action="store_true",
        help="Actualizaciones de Pacman.",
    )
    parser.add_argument(
        "--AUR",
        action="store_true",
        help="Actualizaciones de AUR",
    )

    parser.add_argument(
        "--NEWS",
        type=str,
        dest="NEWS",
        help="Noticias de ArchLinux",
    )
    return parser.parse_args()


def update_kernel() -> bool:
    # Comprueba si hay actualización del kernel.
    updates_list = cmd_output(PACMAN).split("\n")
    for item in updates_list:
        if "linux-zen" in item.split():
            return True
        else:
            return False


def count_updates(update_type: str) -> int:
    # Retorna el número de paquetes a actualizar.
    updates_list = cmd_output(update_type).split("\n")
    counter = 0
    for item in updates_list:
        if "->" in item.split():
            counter += 1
    return counter


def news() -> tuple:
    url = "https://www.archlinux.org"
    page = requests.get(url, timeout=5)
    content = BeautifulSoup(page.content, "html.parser")
    title = content.find_all("a")[16].text
    date = content.find_all("p", class_="timestamp")[0]
    date = str(date.text).split("-")
    date = f"{date[2]}/{date[1]}/{date[0]}"

    return date, title


if __name__ == "__main__":
    args = args_parser()

    if args.PACMAN:
        print(count_updates(PACMAN))
    if args.AUR:
        print(count_updates(AUR))
    if args.NEWS:
        date, title = news()
        type_info = args.NEWS
        if type_info == "date":
            print(date)
        else:
            print(title)
