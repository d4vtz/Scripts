from scripts.procesos.comandos import cmd_output


def launcher(
    opcions: list,
    title: str = "",
    width: int = 25,
    lines: int = 5,
    location: int = 0,
) -> str:
    string = "\n".join(opcions)
    print(string)
    command = f'echo -e "{string}" | rofi -lines {lines} -width {width}\
     -location {location} -dmenu -p "{title}"'
    return cmd_output(command)
