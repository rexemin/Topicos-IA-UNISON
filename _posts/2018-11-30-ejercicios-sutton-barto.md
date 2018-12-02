---
title: Aprendizaje por refuerzo - Parte 1
author: Ivan Moreno
layout: post
mathjax: true
---

Después de aprender programación dinámica nos pasamos a revisar los conceptos fundamentales
del aprendizaje por refuerzo. Para empezar, resolvimos tres problemas relativamente sencillos
con los dos algoritmos más conocidos: SARSA y Q-learning.

## Políticas con aprendizaje por refuerzo
Para aproximar el valor de una política ahora usaremos una idea llamada *temporal-difference learning*. Implementar esta idea nos permite aprender a través
de la experiencia que provoca una política \$ \pi \$ en cada paso de la simulación
del entorno. Así, también nos ahorramos tener que conocer y programar un entorno
en su totalidad, solo ocupamos crear una simulación que proporcione suficiente
información al agente.

Esto ocurre porque ahora aprendemos estimaciones en base a otras estimaciones. No
esperamos a ver resultados correctos y completos para decidir como mejoramos
nuestras acciones. Solo hay un detalle: **¿Cómo sabemos que estamos aprendiendo lo que queremos?**. Lo bueno es que está demostrado que métodos de este estilo
convergen al valor real de la política.

## SARSA
El primer algoritmo para aproximar buenas políticas es el SARSA. Con este,
desechamos la función estado-valor y mejor nos concentramos en aproximar una
función acción-valor \$ Q_\pi (S, A) \$. Aproximamos la función cada vez que
se itera un paso sobre el entorno si llegamos a un estado no final. Si el estado
es final, el valor de la función es 0 (\$ Q_\pi (S_f, A_{t+1}) = 0 \$).

Con esos detalles aclarados, les presento el algoritmo:
\\[ Q(S_t, A_t) \leftarrow Q(S_t, A_t) + \alpha \left( R_{t+1} + \gamma Q(S_{t+1}, A_{t+1}) - Q(S_t, A_t) \right) \\]

Donde \$ R_{t+1} \$ es la recompensa obtenida por la transición entre estados.
\$ \gamma \$ es nuestro confiable factor de descuento, y \$ \alpha \$ es nuestra
taza de aprendizaje.

Y así de fácil es aprender una política mientras vamos ejecutando episodios
sucesivamente siguiendo una política casi al pie de la letra.

## Q-learning
Mejor todavía que un algoritmo sencillo y eficaz, es otro algoritmo igual de
sencillo y más eficaz. SARSA es un algoritmo *on-policy* porque aprende la función
acción-estado a partir de una política. Q-learning, por otra parte, aprende la
misma función sin importar la política. A esto se le llama aprender *off-policy*.

La expresión que representa este algoritmo es la siguiente:
\\[ Q(S_t, A_t) \leftarrow Q(S_t, A_t) + \alpha \left( R_{t+1} + \gamma \max_a Q(S_{t+1}, a) - Q(S_t, A_t) \right) \\]

Formalmente, este algoritmo te da muchas cosas además de la convergencia.
Prácticamente, puede ser más rápido que SARSA.


## Ejercicios del libro de texto

Para probar el funcionamiento de los dos algoritmos anteriores, decidimos resolver 3
problemas sencillos:

- Windy Grid World
- Cliff Walking
- Mountain Car

Todos los problemas vienen descritos en el libro de texto sobre aprendizaje por
refuerzo de Sutton y Barto. Para ahorrarnos un poco de tiempo, también nos dimos
la libertad de traducir el [código utilizado en el libro](https://github.com/ShangtongZhang/reinforcement-learning-an-introduction)
(que está en Python) a Julia. Los 3 problemas están resueltos en [esta libreta de
Jupyter](https://nbviewer.jupyter.org/github/rexemin/Topicos-IA-UNISON/blob/master/AprendizajeRefuerzo/Ejercicios-SuttonBarto.ipynb).

Para explorar estados nuevos y evitar caer en una política estancada, todas las
implementaciones deciden qué acciones tomar mediante políticas \$ \epsilon \$
-greedy. Estas políticas toman la mejor acción en base a la función \$ Q \$ la
mayor parte del tiempo, y el resto deciden aleatoriamente.

Los métodos que estamos usando para aproximar políticas en este curso son un
subconjunto pequeño de todos los que hay. Si quieres saber más sobre cualquiera
deberías echarle un vistazo al libro de Sutton y Barto.
