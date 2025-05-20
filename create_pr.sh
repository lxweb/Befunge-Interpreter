#!/bin/bash

# Ruta al directorio del proyecto
PROJECT_DIR="/home/lisandro/codewars/kyu4/Befunge-Interpreter"

# Token de acceso personal de GitHub (reemplaza con tu token)
GITHUB_TOKEN="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"

# Nombre del repositorio (usuario/repo)
REPO="lxweb102/Befunge-Interpreter"

# Rama actual
BRANCH="feature/initial-interpreter"

# Título y cuerpo del PR
PR_TITLE="feat: Implementación inicial del intérprete de Befunge-93"
PR_BODY="## Cambios realizados
- Estructura inicial del proyecto
- Clase \`BefungeInterpreter\` con manejo básico de la cuadrícula
- Configuración de paquete Python
- Pruebas unitarias iniciales
- Documentación básica

## Próximos pasos
- Implementar instrucciones aritméticas
- Agregar soporte para entrada/salida
- Implementar modo cadena
- Agregar instrucciones de control de flujo

## Pruebas
- [x] Inicialización del intérprete
- [x] Manejo de programa vacío
- [ ] Pruebas de operaciones aritméticas
- [ ] Pruebas de E/S"

# Navegar al directorio del proyecto
cd "$PROJECT_DIR" || exit

# Asegurarse de estar en la rama correcta
git checkout "$BRANCH"

# Hacer pull para obtener los últimos cambios
git pull origin "$BRANCH"

# Añadir todos los cambios
git add .

# Hacer commit
git commit -m "feat: Implementación inicial del intérprete de Befunge-93"

# Hacer push a la rama
git push -u origin "$BRANCH"

# Crear el PR usando la API de GitHub
PR_RESPONSE=$(curl -X POST \
  -H "Authorization: token $GITHUB_TOKEN" \
  -H "Accept: application/vnd.github.v3+json" \
  "https://api.github.com/repos/$REPO/pulls" \
  -d "{\"title\":\"$PR_TITLE\",\"body\":\"$PR_BODY\",\"head\":\"$BRANCH\",\"base\":\"main\"}")

# Verificar si el PR se creó correctamente
if echo "$PR_RESPONSE" | grep -q "created_at"; then
  echo "✅ PR creado exitosamente"
  PR_URL=$(echo "$PR_RESPONSE" | grep -o '"html_url": "[^"]*' | grep -o '[^"]*$')
  echo "🔗 URL del PR: $PR_URL"
else
  echo "❌ Error al crear el PR"
  echo "Respuesta de la API:"
  echo "$PR_RESPONSE"
fi