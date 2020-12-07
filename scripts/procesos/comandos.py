"""
Modulo: procesos.comandos
Este modulo contiene funciones para leer y obtener la salida de retorno
de un comando de shell
"""
import subprocess


def cmd_output(cmd: str) -> str:
    """Devueve una cadena con la salida de un comando de shell.
    Si el comando no es valido, devuelve un string vacío.
    Parametros:
        cmd -> str: Comando a ejecutar
    Return:
        str: Candena con la salida del comando.
    """
    try:
        output = subprocess.run(
            cmd,
            stdout=subprocess.PIPE,
            stderr=subprocess.DEVNULL,
            shell=True,
            text=True,
        )
        if output.returncode == 0:
            return output.stdout[:-1]
        else:
            return ""
    except TypeError:
        raise TypeError("Tipo no valido")


def execute(cmd: str) -> bool:
    """Devueve una Booleano con la salida de un comando de shell.
    Parametros:
        cmd -> str: Comando a ejecutar
    Return:
        bool: Estado de ejecución del comando.
    """
    try:
        output = subprocess.run(
            cmd,
            stdout=subprocess.DEVNULL,
            stderr=subprocess.DEVNULL,
            shell=True,
            text=True,
        )
        if output.returncode == 0:
            return True
        else:
            return False
    except TypeError:
        raise TypeError("Tipo no valido")


def list_proc(program: str) -> list:
    """Función que retorna una lista con todos los procesos que
    ejecuta un programa.
    """
    awk = "'{print $1}'"
    return cmd_output(
        f"ps ax | grep {program} | grep -v grep | awk  {awk}"
    ).split("\n")


def kill_proc(proc: str) -> bool:
    """
    Función que mata un proceso dado.
    """
    return execute(f"kill {proc}")
