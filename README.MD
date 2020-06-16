#Dynatrace reboot process

## Desarrollo para saber cuando un proceso esta solicitando reinicio para ser actualizado

**Programa en python** sencillo para cuando tienes una infraestructura muy grande y que necesitas saber que servicios necesitan ser reiniciados.

Solo necesitas crear tú archivo **config.json** y agregar dos variables, el tenant y el token.

- dynatrace_base_url: 'https://{tuTenant}.live.dynatrace.com/api/v1/entity/infrastructure/"' 

- dynatrace_token: "{tuToken}"

__By CarlosJacob__

16/06/2020 copyright