# 1. Le decimos a Terraform qué versión mínima y qué driver necesitamos
    terraform {
      required_version = ">= 1.5.0"

      required_providers {
        azurerm = {
          source  = "hashicorp/azurerm"
          version = "~> 3.100"
        }
      }
    }

    # 2. Activamos el driver de Azure con su configuración estándar
    provider "azurerm" {
      features {}
    }
