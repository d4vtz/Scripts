import random

import pytest

import scripts.procesos.rofi as rofi


def fun_auxiliar(lista):
    return random.choice(lista)


@pytest.mark.parametrize(
    "test_lists",
    [
        ([1]),
        (["pwd", "PWD"]),
        ([1, 3.4]),
        ([False, True]),
        ([{}, ()]),
    ],
)
def test_rofi(monkeypatch, test_lists):
    monkeypatch.setattr(rofi, "launcher", fun_auxiliar)
    assert rofi.launcher(test_lists) in test_lists
