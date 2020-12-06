#!/usr/bin/env python
import notify2

from scripts.procesos.comandos import cmd_output

CRITICAL_CHARGE = 20


def notify_me(charge):
    if charge < CRITICAL_CHARGE:
        icon = "gtk-ok"
        time_out = 100
        title = "Bateria"
        description = "Bateria critica... Conecte por favor"
        try:
            notify2.init("wee-notifier")
            wn = notify2.Notification(title, description, icon)
            wn.set_urgency(notify2.URGENCY_CRITICAL)
            wn.set_timeout(time_out)
            wn.show()
        except Exception as error:
            raise Exception(f"{error}: No se pudo enviar la notificación")


class Battery:
    def __init__(self):
        state = cmd_output("acpi -V").split("\n")
        self.charge = int(state[0].split()[3].split("%")[0])
        self.state = state[2].split()[2]

    def level(self):
        if 80 <= self.charge < 100:
            return ""
        elif 60 <= self.charge < 80:
            return ""
        elif 40 <= self.charge < 60:
            return ""
        elif 20 <= self.charge < 40:
            return ""
        elif 0 <= self.charge < 20:
            return ""
        else:
            return ""


if __name__ == "__main__":
    battery = Battery()
    if battery.state == "on-line":
        print(f"   {battery.charge}%")
    elif battery.state == "full":
        print("   Carga completa")
    else:
        print(f"{battery.level()}  {battery.charge}%")
        notify_me(battery.charge)
