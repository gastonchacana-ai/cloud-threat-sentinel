#!/bin/bash
    
    echo "🚀 1/2: Creando Grupo de Recursos en Azure (East US)..."
    az group create --name rg-seguridad-dev --location eastus
    
    echo "🌐 2/2: Creando Red Virtual y Subred privada..."
    az network vnet create \
      --resource-group rg-seguridad-dev \
      --name vnet-seguridad \
      --address-prefix 10.0.0.0/16 \
      --subnet-name snet-backend \
      --subnet-prefix 10.0.1.0/24
    
    echo "✅ ¡Infraestructura lista y operativa en Azure!"
