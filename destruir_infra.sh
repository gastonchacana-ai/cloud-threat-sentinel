#!/bin/bash
    
    echo "🧹 Enviando orden de demolición a Azure..."
    az group delete --name rg-seguridad-dev --yes --no-wait
    
    echo "✅ Orden enviada. Azure está borrando todo en segundo plano."
    echo "💰 Tu cuenta quedó protegida y en cero."
