#!/bin/bash

# Nombre del contenedor creado por SAM local (puede cambiar)
CONTAINER_NAME="sam-flaskapifunction"

# Red Docker (puedes usar nombre o ID, aquí lo pasas como argumento si quieres)
DOCKER_NETWORK="${1:-bliss}"  # Por defecto usa 'apolonet', pero puedes pasar otro

# Ruta de logs
LOG_FILE="logs.txt"

echo "🧹 Verificando si hay contenedores SAM antiguos..."

# Buscar contenedor por nombre
OLD_CONTAINER_ID=$(docker ps -a -q --filter "name=${CONTAINER_NAME}")

if [ -n "$OLD_CONTAINER_ID" ]; then
  echo "⚠️  Contenedor viejo encontrado (${OLD_CONTAINER_ID}). Eliminando..."
  docker rm -f "$OLD_CONTAINER_ID"
else
  echo "✅ No hay contenedores anteriores activos."
fi

echo "🔨 Ejecutando SAM build..."
sam build --template-file template.test.yaml

echo "🚀 Iniciando SAM local API en el puerto 8081 y red '$DOCKER_NETWORK'..."
sam local start-api \
  --env-vars env.json \
  --docker-network "$DOCKER_NETWORK" \
  -p 8081 \
  --log-file "$LOG_FILE"
