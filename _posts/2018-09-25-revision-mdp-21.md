---
title: Programación dinámica para jugar 21 - Parte II
author: Ivan Moreno
layout: post
mathjax: true
---

En la clase de esta semana, que por cierto es de 3 horas seguidas, revisamos los avances del 21 de cada quien. Entre discusiones sobre las características buenas de Julia, decisiones dudosas
de su diseño, lo que significa una política tonta, y más, muchas otras cosas quedaron más claras.

## El diseño de Julia

En vez de hablar primero sobre los temas que realmente competen a la clase, prefiero empezar con unas opiniones acerca del diseño de Julia. A fin de cuentas, aprender un lenguaje novedoso
está escondido entre los objetivos principales del curso. Vaya que ha funcionado matar 2 pájaros de un tiro: al momento en que entiendes como funciona el lenguaje, también entiendes detalles
sobre como funcionan los algoritmos.

Como alguien que piensa que la ingeniería de software es fundamental, la documentación de Julia deja mucho que desear, y no es lenguaje. Julia tiene muchas herramientas nativas que facilitan
la escritura de código y de su documentación respectiva, pero muchos desarrolladores no se toman el tiempo de usarlas. Sin embargo, casi todos los contribuidores son voluntarios, y muchos no
tienen formación en computación. Espero que algún día se arregle.

Resulta que en Julia puedes hacer clases. Con todo y constructores. Pero en ninguna parte te dicen que el lenguaje es orientado a objetos. Y a veces no funcionan como crees que deberían. Todo
se debe a que puedes definir tipos abstractos y luego derivar un tipo concreto, ¿no suena parecida a cierta propiedad de lenguajes como C++ y Java? Pero su funcionamiento es extraño y todavía
estamos entendiendo estas características de Julia. Decidí no meterme en eso por lo pronto y me quedé con mis estructuras sencillas. Lo bueno es que si te interesa explorar más sobre estos tipos
abstractos, una compañera de clase esta implementando [aquí](https://github.com/chasil7/MDP/blob/master/MDP_Black_Jack.ipynb) el proyecto utilizando todo lo que la sintaxis ofrece.

## Nuevos algoritmos de programación dinámica

Después de muchas palabras sobre Julia, ahora si, a lo que realmente es de la clase: programación dinámica. La semana pasada, la libreta de Jupyter (que se puede ver [aquí](https://nbviewer.jupyter.org/github/rexemin/Topicos-IA-UNISON/blob/master/21/21-ProgramacionDinamica.ipynb)) solo tenía un algoritmo para encontrar políticas. ¡Ahora son 2! Aunque son 2 funciones nuevas, son parte del mismo
algoritmo de búsqueda. De hecho, las adiciones recientes debieron haber sido implementadas primero, por ser más sencillas, pero que va, lo importante es que ahora tenemos a la familia
completa.

## Retroalimentación sobre el MDP

Lo más relevante de la clase de esta semana fue la retroalimentación sobre mi planteamiento del proceso de decisión de Markov. Creí que sería más fácil si buscaba una política sin tomar
en cuenta las cartas del repartidor, pero después de que el grupo revisara cuidadosamente mi trabajo, quedó claro que es necesario modelar el problema completa desde el principio. Hay
dos razones para esto:

1. La política que es encontrada con el modelo simplificado resulta ser bastante tonta pero correcta. Como no hay incentivo por arriesgarse a conseguir un 21, casi siempre hace nada.
2. Si implemento todas las demás observaciones, será más difícil calcular una recompensa para estados finales si solo existe el jugador en el proceso.

Además, hay varias reglas del juego que implementé mal, así que esas también las tengo que arreglar para la siguiente sesión. Definitivamente siguen siendo resultados mixtos, pero todavía van
mejorando con cada iteración.
