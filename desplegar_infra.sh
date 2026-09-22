#!/bin/bash
    
    echo "🚀 1/4: Creando Grupo de Recursos en Azure (East US)..."
    az group create --name rg-seguridad-dev --location eastus
    
    echo "🌐 2/4: Creando Red Virtual y Subred privada..."
    az network vnet create \
      --resource-group rg-seguridad-dev \
      --name vnet-seguridad \
      --address-prefix 10.0.0.0/16 \
      --subnet-name snet-backend \
      --subnet-prefix 10.0.1.0/24
    
    echo "📦 3/4: Creando Azure Container Registry (ACR)..."
    az acr create \
      --resource-group rg-seguridad-dev \
      --name acrseguridadgaston \
      --sku Basic \
      --admin-enabled true
    
    echo "🏷️ Subiendo imagen de Docker a la nube..."
    az acr login --name acrseguridadgaston
    docker tag api-seguridad:latest acrseguridadgaston.azurecr.io/api-seguridad:v1
    docker push acrseguridadgaston.azurecr.io/api-seguridad:v1

    echo "☁️ 4/4: Desplegando Contenedor en Azure (ACI)..."
    ACR_PASS=$(az acr credential show --name acrseguridadgaston --query "passwords[0].value" -o tsv)

    az container create \
      --resource-group rg-seguridad-dev \
      --name api-seguridad-cloud \
      --image acrseguridadgaston.azurecr.io/api-seguridad:v1 \
      --os-type Linux \
      --cpu 1 \
      --memory 1 \
      --registry-login-server acrseguridadgaston.azurecr.io \
      --registry-username acrseguridadgaston \
      --registry-password "$ACR_PASS" \
      --dns-name-label api-seguridad-gaston \
      --ports 8000

    echo "✅ ¡Infraestructura completa y API desplegada en Azure!"
    echo "👉 URL: http://api-seguridad-gaston.eastus.azurecontainer.io:8000/docs"

    