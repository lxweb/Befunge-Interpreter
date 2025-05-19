# 🧮 Intérprete de Befunge-93

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Python Version](https://img.shields.io/badge/python-3.8+-blue.svg)](https://www.python.org/downloads/)

Un intérprete completo para el lenguaje de programación esotérico [Befunge-93](https://esolangs.org/wiki/Befunge), implementado en Python. Este proyecto es una solución al desafío de CodeWars [Befunge Interpreter](https://www.codewars.com/kata/526c7b931666d07889000a3c).

## 🚀 Características

- Soporte completo para el conjunto de instrucciones de Befunge-93
- Ejecución paso a paso o completa
- Visualización del estado de la pila y el puntero
- Manejo de bordes (wrapping) del espacio 2D
- Modo depuración con seguimiento de ejecución

## 📋 Instalación

1. Clona el repositorio:
   ```bash
   git clone https://github.com/tu-usuario/Befunge-Interpreter.git
   cd Befunge-Interpreter
   ```

2. Crea un entorno virtual (recomendado):
   ```bash
   python -m venv venv
   source venv/bin/activate  # En Windows: venv\Scripts\activate
   ```

3. Instala las dependencias:
   ```bash
   pip install -r requirements.txt
   ```

## 🛠️ Uso

```python
from befunge_interpreter import BefungeInterpreter

# Crea una instancia del intérprete
interpreter = BefungeInterpreter()

# Código de ejemplo: imprime "Hello, World!"
code = '"">:v\n,^_@'


# Ejecuta el código
output = interpreter.interpret(code)
print(output)  # Salida: Hello, World!
```

## 📚 Instrucciones Soportadas

| Comando | Descripción |
|---------|-------------|
| `0-9` | Empuja el número a la pila |
| `+` | Suma: `a + b` |
| `-` | Resta: `b - a` |
| `*` | Multiplicación: `a * b` |
| `/` | División entera: `b // a` (0 si a=0) |
| `%` | Módulo: `b % a` (0 si a=0) |
| `!` | NOT lógico: 1 si a=0, si no 0 |
| `` ` `` | Mayor que: 1 si b>a, si no 0 |
| `>` | Mover puntero a la derecha |
| `<` | Mover puntero a la izquierda |
| `^` | Mover puntero arriba |
| `v` | Mover puntero abajo |
| `?` | Mover en dirección aleatoria |
| `_` | Pop, mover derecha si 0, izquierda si no |
| `\|` | Pop, mover abajo si 0, arriba si no |
| `"` | Alternar modo cadena |
| `:` | Duplicar tope de la pila |
| `\` | Intercambiar dos valores en el tope |
| `$` | Descartar tope de la pila |
| `.` | Imprimir número |
| `,` | Imprimir carácter ASCII |
| `#` | Trampolín: saltar siguiente celda |
| `p` | Put: almacenar valor en la cuadrícula |
| `g` | Get: obtener valor de la cuadrícula |
| `&` | Leer número de entrada |
| `~` | Leer carácter de entrada |
| `@` | Terminar programa |

## 🧪 Ejecutando Pruebas

```bash
pytest tests/
```

## 🤝 Contribución

¡Las contribuciones son bienvenidas! Por favor, lee las [pautas de contribución](CONTRIBUTING.md) para más detalles.

## 📄 Licencia

Este proyecto está bajo la Licencia MIT - ver el archivo [LICENSE](LICENSE) para más detalles.

## 📚 Recursos

- [Esolang Wiki - Befunge](https://esolangs.org/wiki/Befunge)
- [Befunge-93 Documentation](https://catseye.tc/view/befunge-93/doc/Befunge-93.markdown)
- [CodeWars Challenge](https://www.codewars.com/kata/526c7b931666d07889000a3c)
