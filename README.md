# 💻 Sistema de Gestión de Laboratorio de Informática (Odoo)

Bienvenido a nuestro proyecto! Aquí vas a poder gestionar aulas, equipos, software, incidencias y tecnicos.

El sistema se divide en dos módulos, `lab_equipo` la base, y `lab_mantenimiento` que depende de la primera.

---

## 1. Módulo Base: `lab_equipo` 🖥️

Este módulo es el núcleo del sistema. (realizado por Izaro)

### 🗂️ Modelos Principales
| Modelo | Descripción | Relaciones Clave |
| :--- | :--- | :--- |
| **Aula** | Registro de los espacios físicos (laboratorios, clases). | Uno-a-Muchos con Equipo |
| **Equipo** | Registro detallado del hardware (PCs, monitores, etc.). | Muchos-a-Uno con Aula |
| **Software** | Catálogo de software disponible. | Muchos-a-Muchos con Equipo |

### 📄 Informes PDF
El módulo incluye la generación automática de PDFs con información de un aula y un equipo

---

## 2. Módulo depentente: `lab_mantenimiento` 🛠️

### ⚠️ Dependencia
Este módulo depende de **`lab_equipo`**. (realizado por Juan David)

### 🗂️ Modelos Principales
| Modelo | Descripción | Relaciones Clave |
| :--- | :--- | :--- |
| **Técnico** | Registro del personal de soporte. Incluye un selector de especialidad (`Hardware` o `Software`). | Uno-a-Muchos con Incidencia |
| **Incidencia** | Sistema de tickets para reportar averías. | Muchos-a-Uno con Equipo (de `lab_equipo`) y con Técnico |


## ✒️ Autores

* **[Izaro Calvo Zubiela & Juan David Ivan]** 
