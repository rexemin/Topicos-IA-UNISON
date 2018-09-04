---
title: Aprendiendo a usar Julia 1.0
author: Ivan Moreno
layout: post
---

Para empezar el curso se decidió aprender a usar la versión 1.0 de [Julia](https://julialang.org/),
y que mejor forma de hacerlo que peléandonos con las libretas de Jupyter diseñadas para enseñarte
cada parte del lenguaje.

Llenar y ejecutar esas libretas debería ser trivial, pero estas se encuentran hechas para la versión
0.6. Con todos los cambios que se le hicieron a Julia, la traducción entre versiones no esta
tan directa.

**_¿Qué se le va a hacer ahora? Decidimos estar a la vanguardia._**

Como sea el caso: ya modifiqué las libretas. Las puse en un repositorio de GitHub para quien quiera
verlas y aprender; o copiarlas, también tengo de esos compañeros.

El repositorio se encuentra en esta [dirección](https://github.com/rexemin/Topicos-IA-UNISON/tree/master/Tutoriales-Julia-v1). Por lo pronto solo son las primeras 12 libretas de introducción al lenguaje.

Ahora, hay algunos detalles sobre los cambios de Julia:
 + Hay que tener cuidado con el backend de Plotly, ya no es tan fácil como usar el mismo código para cualquier librería de graficación

 + Muchas librerías ya no son cargadas por defecto. Las que encontré así son:
   - Statistics
   - Libdl
   - Pkg
 + Hay algunas que ni vienen instaladas desde el principio, como:
   - PyCall
   - Conda
