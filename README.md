# QA Automation Test – CatFact API

## Descripción
Este proyecto contiene pruebas automatizadas de API utilizando Postman para la API pública CatFact.ninja.

## Requests incluidos
- Fact aleatorio
- Fact con longitud máxima
- Listado de razas
- Paginación de razas

## Validaciones implementadas
- Status code
- Tiempo de respuesta
- Campos obligatorios
- Tipos de datos
- Estructura de arrays
- Validación de paginación

## Variables
Se utilizó la variable `max_length` para validar dinámicamente la longitud del fact.

## Ejecución
1. Importar `collection.json` en Postman
2. Ejecutar la colección desde el Collection Runner

## Evidencia
Ver archivo `reporte.png`

## Mejoras futuras
- Integración con Newman para CI/CD
- Validación de esquemas JSON
- Manejo de casos negativos

## Tiempo invertido
Aproximadamente 2-3 horas
