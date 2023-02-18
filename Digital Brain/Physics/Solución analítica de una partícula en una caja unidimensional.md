### Solución analítica

Este problema puede plantearse para cualquier número de dimensiones, pero nos concentraremos por simplicidad en una sola dimensión y podremos extenderla con facilidad a el caso de tres dimensiones.

Con ayuda de esta descripción, podemos escribir la [[ecuación de Schrodinger]] en una dimensión:

$$ 
	-\frac{\hbar^2}{2m} \frac{d^2 \psi}{dx^2} + V(x)\psi(x) = E \; \psi(x)
$$

Entonces podemos escribir la ecuación de Schrodinger para el potencial $V(x)=0$,
$$
-\frac{\hbar^{2}}{2m} \frac{d^{2} \psi}{dx^{2}} = E \; \psi(x)
$$
con $0<x<L$, en donde $L$ es la longitud de la caja. Junto con las condiciones de frontera:
$$
\begin{align}
	\psi(0) &= 0\\
	\psi(L) &= 0.
\end{align}
$$
#### Resolución de la ecuación

Reescribiendo la ecuación como:
$$
\frac{d^2 \psi}{dx^2} + \frac{2mE}{\hbar^2} \; \psi(x) = 0
$$

Dado que se trata de una ecuación diferencial de segundo orden homogénea, podemos suponer como solución:
$$
\psi(x) = A \; e^{\lambda x}
$$
De modo que si sustituimos esta solución en la ecuación diferencial, obtenemos:
$$
\left(\lambda^2 + \frac{2mE}{\hbar^2}\right) \psi(x) = 0
$$
Dado que esto expresión tiene que ser valida para cualquier función $\psi(x)$, la única opción es que el primer termino sea igual a cero. Si despejamos $\lambda$ obtenemos:
$$
\lambda = \pm \sqrt{\frac{2mE}{\hbar^2}} \; i
$$
De modo que la solución general de la ecuación tiene la forma,
$$
\psi(x) = A \; \exp\left(i\sqrt{\frac{2mE}{\hbar^{2} }} \;x\right) + B \; \exp\left(-i\sqrt{ \frac{2mE}{\hbar^{2} }} \; x\right)
$$
Para obtener la solución particular, necesitamos usar las condiciones de frontera. Para la primera: $\psi(0) = 0$, tenemos,
$$
\begin{align}
	0 &= A + B \\
	B &= -A
\end{align}
$$
Por lo que si sustituimos en la ecuación general
$$
\psi(x) = A\left[ \; \exp\left(i\sqrt{\frac{2mE}{\hbar^{2} }} \;x\right) - \; \exp\left(-i\sqrt{ \frac{2mE}{\hbar^{2} }} \; x\right) \right]
$$
#### Aplicando condiciones de frontera

Ahora si usamos la segunda condición de frontera: $\psi(L) = 0$, tenemos,

$$
\begin{align}
0 &= A\left[ \; \exp\left(i\sqrt{\frac{2mE}{\hbar^{2} }} \;L\right) - \; \exp\left(-i\sqrt{ \frac{2mE}{\hbar^{2} }} \; L\right) \right],\\
&= 2A \sin\left(\sqrt{ \frac{2mE}{\hbar^{2} }} \; L\right) 
\end{align}
$$
Por lo que esto se logra solo si el argumento de la función seno es igual a un múltiplo de $2\pi$, por lo tanto:
$$\begin{align}
n\pi &= \sqrt{\frac{2mE}{\hbar^{2} }} \; L \\
E_{n} &= \frac{\pi^2\hbar^{2}n^{2}}{2mL^2} \\
\end{align}
$$
Por lo tanto, obtenemos,
$$
\psi_{n}(x) = A\; \sin\left( \frac{n\pi x}{L} \right)
$$

#### Normalización de los estados
dado que las funciones de onda tienen que estar normalizadas, es decir $\int  | \psi(x)|^{2} \; dx = 1$, entonces,
$$
\begin{align}
1 &= A^2\int_{0}^{L} \sin^2\left( \frac{n\pi x}{L} \right) \, dx, \\
&= A^{2}\int _{0}^{L}\frac{1 - \cos\left( \frac{2n\pi x}{L} \right)}{2} \, dx, \\
&= A^{2}\left[ \frac{x}{2} - \frac{L}{4n\pi} \sin\left(\frac{2n\pi x}{L}\right) \right]_{0}^L, \\
&= \frac{A^{2}L}{2} \\
A &= \sqrt{ \frac{2}{L} }
\end{align}
$$

#### Solución

La solución de la partícula en una caja unidimensional esta dada por la función de onda y energías cuantizadas por:
$$\begin{align}
\psi_{n}(x) &= \sqrt{ \frac{2}{L} } \; \sin \left( \frac{n\pi x}{L} \right),\\
E_{n} &= \frac{\pi^2\hbar^{2}n^{2}}{2mL^2} \\
\end{align}
$$