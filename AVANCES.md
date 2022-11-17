**BITÁCORA DE AVANCES**
===
<br>

## Avance 1
---
- **Fecha:** 03/Oct/2022

- **Descripción:** Realización del lexer y parser iniciales, donde se definen los tokens y reglas de sintaxis a usarse en el lenguaje ALi.

- **Estado:**

    Lexer - COMPLETO y FUNCIONANDO

    Parser - Las reglas de sintaxis para el estatuto *`else`* no están funcionando al 100%. Existe un Shift/Reduce conflict.

<br>

## Avance 0
---
- **Fecha:** 08/Oct/2022

- **Descripción:** Entrega de propuesta inicial

- **Estado:** Completo

<br>

## Avance 2
---
- **Fecha:** 11/Oct/2022

- **Descripción:** Correción de parser, para incluir las funciones especiales. Se agregó el cubo semántico y la primera versión de la tabla de variables.

- **Estado:**

    Lexer - COMPLETO y FUNCIONANDO

    Parser - COMPLETO Y FUNCIONANDO

    Cubo semántico - COMPLETO, falta probarlo al generar las reglas semánticas

    Tabla de variables - COMPLETO (la versión básica que se ha visto a la fecha en clase)

<br>

## Avance 3
---
- **Fecha:** 17/Oct/2022

- **Descripción:** Añadimiento de puntos neurales iniciales, para expresiones y estatutos lineales

- **Estado:**
    
    Generación de código intermedio para expresiones - INCOMPLETO (Se identificaron puntos neurales por añadir, sin embargo, falta pulir las acciones a realizar)
        
<br>

## Avance 4
---
- **Fecha:** 04/Nov/2022

- **Descripción:** Generación de códgo intermedio para estatutos condicionales y cíclicos.

- **Estado:**
    Reglas semánticas y generación de código intermedio:
    - Expresiones - COMPLETO
    - Condiciones - COMPLETO
    - Ciclos - COMPLETO
        
<br>

## Avance 5
---
- **Fecha:** 07/Nov/2022

- **Descripción:** Creación de directorio de funciones con sus correspondientes datos almacenados (id, recursos, parametros).
\
Se identificaron Issues.

- **Estado:**
    - Issue 10 (Terminado): Añadimiento de tokens *`true`* y *`false`*
    - Issue 11 (Por hacer): Memoria Virtual no maneja rango para variables globales
    - Issue 12 (Por hacer): Sintaxis de expresiones no permite manejar negativos
    - Issue 14 (En progreso): La sintaxis forza a tener estatutos en la función main, fuera de las funciones especiales _**start**_ y _**update**_.
        
<br>

## Avance 6.
---
- **Fecha:** 15/Nov/2022

- **Descripción:** Maquina Virtual y 

- **Estado:**
    - Maquina Virtual: COMPLETO -> Ejecucion de estatutos condicionales, ciclos, y expresiones aritemticas y lógicas.
    - Arreglos: COMPLETO -> Declaración de arreglos válida. Almacenamiento de arreglos en tabla de variables y asignación de memoria correspondiente
    - Arreglos: EN PROGRESO -> generación de cuádruplos para indexamiento.

<br>

## Avance #.
---
- **Fecha:** 00/month/0000

- **Descripción:**

- **Estado:**

        
<br>