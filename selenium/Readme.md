# Automatización Web con Selenium

## Herramienta
Selenium con Python

## Flujo automatizado
- Abrir la página
- Click en "Contacto"
- Scroll a la sección tab-contact
- Validar visibilidad
- Verificar email

## Problema encontrado
Se presentó un error "element click intercepted" debido a un preloader que bloqueaba la interacción.

## Solución
Se implementó:

wait.until(EC.invisibility_of_element_located((By.ID, "preloader")))

y uso de JavaScript para el click.

## Aprendizajes
- Manejo de elementos dinámicos
- Uso de WebDriverWait
- Identificación de problemas reales de UI

## Mejoras futuras
- Page Object Model
- Integración con pytest
- CI/CD
