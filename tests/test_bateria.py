import pytest

from scripts.bateria import LEVEL, Battery


def fun_1(x):
    return [
        "Battery 0: Charging, 29%, 01:11:42 until charged",
        "Battery 0: design capacity 3800 mAh 1599 mAh = 42%",
        "Adapter 0: on-line",
    ]


def fun_2(x):
    return [
        "Battery 0: Charging, 10%, 01:11:42 until charged",
        "Battery 0: design capacity 3800 mAh 1599 mAh = 42%",
        "Adapter 0: off-line",
    ]


def fun_3(x):
    return [
        "Battery 0: Charging, 100%, 01:11:42 until charged",
        "Battery 0: design capacity 3800 mAh 1599 mAh = 42%",
        "Adapter 0: full",
    ]


@pytest.mark.parametrize(
    "raw_info_test, output_test",
    [(fun_1, 29), (fun_2, 10), (fun_3, 100)],
)
def test_charge(monkeypatch, raw_info_test, output_test):
    monkeypatch.setattr(Battery, "raw_info", raw_info_test)
    test_battery = Battery()
    assert test_battery.charge == output_test


@pytest.mark.parametrize(
    "raw_info_test, output_test",
    [(fun_1, "on-line"), (fun_2, "off-line"), (fun_3, "full")],
)
def test_state(monkeypatch, raw_info_test, output_test):
    monkeypatch.setattr(Battery, "raw_info", raw_info_test)
    test_battery = Battery()
    assert test_battery.state == output_test


@pytest.mark.parametrize(
    "raw_info_test",
    [(fun_1), (fun_2), (fun_3)],
)
def test_level(monkeypatch, raw_info_test):
    monkeypatch.setattr(Battery, "raw_info", raw_info_test)
    test_battery = Battery()
    assert test_battery.level() in LEVEL
