# SIGEM - Sistemas de Gestión Empresarial 🚀

![Python](https://img.shields.io/badge/Python-3.x-blue?style=flat&logo=python)
![Odoo](https://img.shields.io/badge/Odoo-17-purple?style=flat&logo=odoo)
![Status](https://img.shields.io/badge/Estado-En_Desarrollo-green)
![Curso](https://img.shields.io/badge/Curso-2º_DAM-orange)

Este repositorio almacena las prácticas y proyectos realizados para la asignatura de **Sistemas de Gestión Empresarial (SIGEM)**. El contenido abarca desde la introducción al lenguaje Python (base de Odoo) hasta la implantación funcional de un ERP en un escenario empresarial real.

## 📂 Estructura del Repositorio

El repositorio se divide en dos bloques principales:

### 1. 🐍 Prácticas de Python
Colección de ejercicios para dominar la sintaxis y lógica de programación necesaria para el desarrollo de módulos en Odoo.

* **Fundamentos:** Ejercicios de lógica básica, bucles y condicionales (Cálculo de factoriales, números primos, tablas de multiplicar).
* **Estructuras de Datos:** Manejo de listas y diccionarios (Gestión de asignaturas, filtrado de abecedarios).
* **POO (Programación Orientada a Objetos):**
    * Simulación de un sistema de gestión de **Recursos Humanos**.
    * Clases `Empresa` y `Empleado` con funcionalidades para contratar, despedir y calcular costes salariales.

### 2. 🏢 Proyecto ERP Odoo - Depofibra S.L.
Documentación y configuración de la implantación de Odoo 17 para **Depofibra**, una empresa especializada en la fabricación de depósitos y piscinas de poliéster.

**Módulos Implementados y Configurados:**
* **Fabricación (MRP):** Gestión de Listas de Materiales (LdM) para productos como la *Piscina 'Oasis' 8x4m* y control de consumo de materias primas (Resina, Fibra).
* **Inventario y Compras:** Flujos de aprovisionamiento automatizados y valoración de stock.
* **Ventas y CRM:** Gestión del ciclo de vida del cliente, desde la oportunidad (lead) hasta el presupuesto y la venta final.
* **Sitio Web y E-commerce:** Integración de tienda online personalizada para la venta de productos y captación de clientes.
* **Gestión de Proyectos:** Control de tareas para servicios de instalación y mantenimiento.
* **Recursos Humanos y Gastos:** Gestión de empleados, nóminas y validación de gastos de viaje.

## 🛠️ Tecnologías Utilizadas

* **Lenguaje:** Python 3
* **ERP:** Odoo Community Edition (v17)
* **Base de Datos:** PostgreSQL
* **Entorno:** Ubuntu Server 24.04 (Virtualizado)

## 🚀 Ejecución de Scripts (Python)

Para probar los ejercicios de Python, simplemente clona el repositorio y ejecuta los archivos `.py`:

```bash
# Clonar repositorio
git clone [https://github.com/juanjo210106/SIGEM.git](https://github.com/juanjo210106/SIGEM.git)

# Ejecutar un ejercicio básico (ej. calculadora)
python "PRÁCTICA 1 - PYTHON JJGL/calculadora.py"

# Ejecutar la simulación de Empresa/Empleado
python "PRÁCTICA 4 - PYTHON JJGL/Main.py"
