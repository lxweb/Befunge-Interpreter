"""Pruebas básicas para el intérprete de Befunge."""
import pytest
from befunge_interpreter import BefungeInterpreter


def test_initialization():
    """Prueba que el intérprete se inicializa correctamente."""
    interpreter = BefungeInterpreter()
    assert interpreter is not None
    assert hasattr(interpreter, 'run')


def test_empty_program():
    """Prueba que un programa vacío no produce salida."""
    interpreter = BefungeInterpreter()
    result = interpreter.run("")
    assert result == ""


def test_hello_world():
    """Prueba un programa 'Hola Mundo' simple."""
    interpreter = BefungeInterpreter()
    # Un programa simple que imprime "HI"
    result = interpreter.run('"!dlroW ,olleH" >:#,_@')
    # Invertir la cadena porque la pila es LIFO
    assert result == "Hello, World!\n"
