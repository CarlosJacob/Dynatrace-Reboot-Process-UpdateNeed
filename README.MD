#Dynatrace reboot process for update version
---
## Desarrollo para saber cuando un proceso esta solicitando reinicio para ser actualizado

**Programa en python** sencillo para cuando tienes una infraestructura muy grande y que necesitas saber que servicios necesitan ser reiniciados.

Solo necesitas crear tú archivo **config.json** y agregar dos variables, tenant y token

- dynatrace_base_url: 'https://{tuTenant}.live.dynatrace.com/api/v1/entity/infrastructure/"' 

- dynatrace_token: "{tuToken}"


Formato: **config.json**
<pre><code>
{
    "dynatrace_base_url": "https://{tuTenant}live.dynatrace.com/api/v1/entity/infrastructure/",
    "dynatrace_token": "{tuToken}"
}
</code></pre>

__By CarlosJacob__

copyright