import pytest

import scripts.actualizaciones as actualizaciones


@pytest.mark.parametrize(
    "update_type_test, output_test",
    [
        ("PACMAN", 9),
        ("AUR", 0),
    ],
)
def test_count_updates(monkeypatch, update_type_test, output_test):
    monkeypatch.setattr(
        actualizaciones, "count_updates", lambda x: output_test
    )
    assert actualizaciones.count_updates(update_type_test) == output_test


def kernel(update_list):
    if "linux" in update_list:
        return True
    else:
        return False


@pytest.mark.parametrize(
    "update_list_test, output_test",
    [
        (["asdf", "134", "True", "{}", "()", "[]"], False),
        (["123", "linux", "False", "{}", "()", "[]"], True),
    ],
)
def test_update_kernel(monkeypatch, update_list_test, output_test):
    monkeypatch.setattr(actualizaciones, "update_kernel", kernel)
    assert actualizaciones.update_kernel(update_list_test) == output_test
