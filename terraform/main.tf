# 1. El Grupo de Recursos
    resource "azurerm_resource_group" "rg" {
      name     = "rg-seguridad-terraform"
      location = "eastus"
    
      tags = {
        Ambiente   = "Desarrollo"
        Proyecto   = "Operation-Cloud-Architect"
        Gestionado = "Terraform"
        Operador   = "Gaston"
      }
    }
    
    # 2. La Red Virtual (VNet)
    resource "azurerm_virtual_network" "vnet" {
      name                = "vnet-seguridad-tf"
      location            = azurerm_resource_group.rg.location
      resource_group_name = azurerm_resource_group.rg.name
      address_space       = ["10.10.0.0/16"]
    
      tags = azurerm_resource_group.rg.tags
    }
    
    # 3. La Subred Privada para el Backend
    resource "azurerm_subnet" "subnet" {
      name                 = "snet-backend-tf"
      resource_group_name  = azurerm_resource_group.rg.name
      virtual_network_name = azurerm_virtual_network.vnet.name
      address_prefixes     = ["10.10.1.0/24"]
    }
    
    # 4. Firewall en la Nube (Network Security Group) con puerto 8000 abierto
    resource "azurerm_network_security_group" "nsg" {
      name                = "nsg-seguridad-tf"
      location            = azurerm_resource_group.rg.location
      resource_group_name = azurerm_resource_group.rg.name

      security_rule {
        name                       = "Allow-API-8000"
        priority                   = 100
        direction                  = "Inbound"
        access                     = "Allow"
        protocol                   = "Tcp"
        source_port_range          = "*"
        destination_port_range     = "8000"
        source_address_prefix      = "*"
        destination_address_prefix = "*"
      }

      tags = azurerm_resource_group.rg.tags
    }
