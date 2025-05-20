"""
Implementación del intérprete de Befunge-93.
"""
from typing import List, Tuple, Optional
import random


class BefungeInterpreter:
    """
    Intérprete para el lenguaje de programación esotérico Befunge-93.
    """

    def __init__(self):
        """Inicializa el intérprete con valores por defecto."""
        self.stack = []
        self.output = []
        self.grid = []
        self.width = 0
        self.height = 0
        self.pc = (0, 0)  # (x, y) - posición actual del puntero
        self.direction = (1, 0)  # Inicialmente se mueve a la derecha
        self.string_mode = False
        self.running = False

    def load_code(self, code: str) -> None:
        """
        Carga el código Befunge en la cuadrícula del intérprete.

        Args:
            code: Código fuente en formato de cadena con saltos de línea.
        """
        self.grid = [list(line) for line in code.splitlines()]
        self.height = len(self.grid)
        self.width = max(len(line) for line in self.grid) if self.height > 0 else 0
        
        # Asegurarse de que todas las filas tengan el mismo ancho
        for row in self.grid:
            row.extend([' '] * (self.width - len(row)))
        
        # Reiniciar el estado del intérprete
        self.stack = []
        self.output = []
        self.pc = (0, 0)
        self.direction = (1, 0)
        self.string_mode = False
        self.running = True

    def step(self) -> bool:
        """
        Ejecuta un solo paso del programa.

        Returns:
            bool: True si el programa debe continuar ejecutándose, False si ha terminado.
        """
        if not self.running:
            return False

        x, y = self.pc
        instruction = self.grid[y][x]

        if self.string_mode and instruction != '"':
            self.stack.append(ord(instruction))
        else:
            self._execute_instruction(instruction)

        # Mover el puntero
        dx, dy = self.direction
        self.pc = ((x + dx) % self.width, (y + dy) % self.height)
        
        return self.running

    def _execute_instruction(self, instruction: str) -> None:
        """
        Ejecuta una sola instrucción del código Befunge.

        Args:
            instruction: Carácter que representa la instrucción a ejecutar.
        """
        if instruction == '"':
            self.string_mode = not self.string_mode
        elif instruction == '@':
            self.running = False
        # Aquí implementaremos el resto de las instrucciones

    def run(self, code: Optional[str] = None) -> str:
        """
        Ejecuta el código Befunge hasta que termine.

        Args:
            code: Código opcional para cargar antes de ejecutar.
                 Si es None, usa el código ya cargado.

        Returns:
            str: La salida generada por el programa.
        """
        if code is not None:
            self.load_code(code)
        
        while self.running:
            self.step()
            
        return ''.join(self.output)

    def _pop(self) -> int:
        """Extrae un valor de la pila, retorna 0 si está vacía."""
        return self.stack.pop() if self.stack else 0

    def _pop_two(self) -> Tuple[int, int]:
        """Extrae dos valores de la pila, retorna (0, 0) si está vacía."""
        a = self._pop()
        b = self._pop()
        return a, b
