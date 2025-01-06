# Aplicación Flask (Python) con contenerización en Azure Container Registry y desplegado en una Azure Web App (App Service F1)

Template para una aplicación Flask, publicando en Azure Container Registry (ACR) y desplegando en una Azure App Service mediante container.

## Variables de entorno

* **CORS_ORIGIN:** URL desde donde se aceptarán peticiones separados por comas (,). Si no existe, se utilizará '*' por defecto.

*Se recomienda utilizar variables de entorno para las URLs base en donde se encuentran microservicios o APIs con los que interactuará la aplicación.*

## Secretos (Actions) de GitHub

Este proyecto incluye un pipeline para publicación mediante código en un Azure Web App.

* **AZUREAPPSERVICE_CLIENTID_DEV:** Id de cliente (UUID) de la aplicación registrada en Microsoft Entra con rol de contributor sobre el recurso.
* **AZUREAPPSERVICE_NAME_DEV:** Nombre dado al recurso (WebApp).
* **AZUREAPPSERVICE_SUBSCRIPTIONID:** Id de la subscripción (UUID) asociada al recurso.
* **AZUREAPPSERVICE_TENANTID:** Id de inquilino (UUID) de la organización.
* **AZURE_RESOURCE_GROUP:** Nombre del grupo de recursos al que pertenece la WebApp.
* **ACR_NAME:** Nombre del Azure Container Registry.
* **ACR_APP_NAME:** Nombre del repositorio para la imagen (usualmente el nombre de la misma App).
* **ACR_USERNAME:** Usuario administrador del Azure Container Registry (Configuración/Claves de acceso).
* **ACR_PASSWORD:** Contraseña del usuario administrador.

## Páginas estáticas

El proyecto incluye una página estática para indicar error cuando se intenta entrar a la URL del servidor, una dirección incorrecta o acceder a un endpoint con el método HTTP incorrecto.
