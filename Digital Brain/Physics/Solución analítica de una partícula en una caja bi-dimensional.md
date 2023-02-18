#Cuántica 
#Soluciones/Analítica
#PartículaCaja

Para resolver este caso, necesitamos resolver la ecuación de Schrodinger de valores propios en 2 dimensiones. Para ello usaremos el método de separación de variables para poder encontrar los auto valores y los auto estados para este sistema.

La ecuación de Schrodinger para este sistema esta dado por:

$$
-\frac{\hbar^{2}}{2m} \left( \frac{\partial^{2} \psi}{\partial x^{2}}+ \frac{\partial^{2} \psi}{\partial y^{2}} \right) = E \; \psi(x, y)
$$
Con las condiciones de frontera:
$$
\begin{align}
\psi(0,y) &= 0 \\
\psi(L_{x},y) &= 0 \\
\psi(x,0) &= 0 \\
\psi(x,L_{y}) &= 0
\end{align}
$$
De modo que la partícula se encuentra confinada en la región:
$$
\begin{align}
&0 \leq x \leq A \\
&0 \leq y \leq B
\end{align}
$$

Arreglando un poco la ecuación:

$$
\frac{\partial^{2} \psi}{\partial x^{2}}+ \frac{\partial^{2} \psi}{\partial y^{2}} + \frac{2mE}{\hbar^{2}} \; \psi(x, y) = 0
$$

#### Separación de variables

Si suponemos como solución una función $\psi(x,y)$ como el producto de dos funciones de modo que solo dependan de $x$ y $y$ respectivamente:
$$
\psi(x,y) = f(x)\; g(y)
$$
Por lo tanto si sustituimos en la ecuación de Schrodinger y hacemos una separación de variables, obtenemos:
$$
\begin{align}
&\frac{\partial^{2} }{\partial x^{2}} \; f(x)\; g(y) + \frac{\partial^{2} }{\partial y^{2}}\;f(x)\; g(y) + \frac{2mE}{\hbar^{2}} \; f(x)\; g(y) = 0 \\
&\frac{d^{2} f}{d x^{2}} \; g(y) + f(x) \; \frac{d^{2} g}{d y^{2}} + \frac{2mE}{\hbar^{2}} \; f(x)\; g(y) = 0  \\
&\frac{1}{f(x)} \; \frac{d^{2} f}{d x^{2}} + \frac{1}{g(y)} \; \frac{d^{2} g}{d y^{2}} + \frac{2mE}{\hbar^{2}} = 0 \\
&-\frac{1}{f(x)} \; \frac{d^{2} f}{d x^{2}} -  \frac{1}{g(y)} \; \frac{d^{2} g}{d y^{2}} = \frac{2mE}{\hbar^{2}}
\end{align}
$$

Dado que los dos términos del primer miembros de la ecuación son independientes entre si, entonces podemos decir que son iguales a una cierta constante que llamaremos $\alpha^2$ y $\beta^2$ respectivamente, por lo tanto obtenemos dos ecuaciones diferenciales ordinarias de segundo orden:

$$
\begin{align}
-\frac{1}{f(x)} \; \frac{d^{2} f}{d x^{2}}  &= \alpha^2 \\
- \frac{1}{g(y)} \; \frac{d^{2} g}{d y^{2}} &= \beta^2
\end{align}
$$

de modo que se tiene que cumplir:
$$
E = \frac{\hbar^2}{2m}\left(\alpha^{2}+\beta^2\;\right)
$$
con las condiciones de frontera:
$$
\begin{align}
f(0) &= 0 \\
f(L_{x}) &= 0 \\
g(0) &= 0 \\
g(L_{y}) &= 0
\end{align}
$$
Procederemos a resolver la primera ecuación:
$$
-\frac{1}{f(x)} \; \frac{d^{2} f}{d x^{2}}  = \alpha^2
$$
Reescribiendo la ecuación:
$$
\frac{d^{2} f}{d x^{2}} + \alpha^{2}f(x) = 0
$$

Si suponemos como solución una función del tipo $f(x) = C \exp(\lambda x)$ entonces podemos sustituir en la ecuación anterior, tenemos:

$$
\lambda^2 + \alpha^{2} = 0
$$
Por lo tanto obtenemos dos valores para $\lambda$:
$$
\lambda = \pm i \alpha
$$

Por lo tanto la solución general esta formada por la función:
$$
f(x) = C \exp\left( i \alpha x\right) + D \exp\left( -i \alpha x\right)
$$
#### Aplicando condiciones de frontera

Por lo que si aplicamos las condiciones de frontera:

$$
\begin{align}
f(0) &= C + D \\
D &= -C 
\end{align}
$$
Por lo que obtenemos:
$$
f(x) = C \left[ \exp\left( i\alpha x\right) - \exp\left( -i\alpha x\right) \right]
$$
Aplicando la segunda condición:
$$
\begin{align}
0 &= C \left[ \exp\left( i\alpha L_{x}\right) - \exp\left( -i\alpha L_{x}\right) \right] \\
&= C \sin\left( \alpha L_{x} \right) \\
&= \sin\left( \alpha A \right)
\end{align}
$$
Por lo que para que se cumpla esta condición de frontera se tiene que satisfacer la igualdad:
$$
 \alpha L_{x} = n \pi
$$
Por lo tanto la constante $\alpha$ esta dada por:
$$
\alpha = \frac{n\pi}{L_{x}}
$$
De modo que para conocer por completo el espectro de la energía necesitamos determinar el valor de $\alpha^2$.

Por otra parte la solución de la ecuación esta dada por:
$$
f(x) = C \sin\left(\frac{n \pi x}{L_{x}} \right)
$$
Dado que la segunda ecuación tiene la misma forma, su solución esta dada por:

$$
g(y) = D \sin\left( \frac{m\pi y}{L_{y}} \right)
$$
con la contante $\beta$ dada por:
$$
\beta = \frac{m\pi}{L_{y}}
$$

Por lo tanto regresando a la función de onda $\psi(x, y) = f(x)\;g(y)$

$$
\psi_{n,m}(x, y) = E \; \sin\left( \frac{n\pi y}{L_{x}} \right)\;\sin\left( \frac{m\pi y}{L_{y}} \right)
$$
#### Normalización de los estados

Por último, solo nos quedaría normalizar la función de onda $\psi(x, y)$:

$$
\begin{align}
1 &= | E |^{2}\int_{0}^{L_{x}} \int _{0}^{L_{y}} \sin^{2}\left( \frac{n\pi y}{L_{x}} \right)\;\sin^{2}\left( \frac{m\pi y}{L_{y}} \right)  \, dx  \, dy \\
&= | E |^{2}\int_{0}^{L_{x}} \sin^{2}\left( \frac{n\pi y}{L_{x}} \right) \, dx \int _{0}^{L_{y}} \sin^{2}\left( \frac{m\pi y}{L_{y}} \right)  \, dy \\
&= | E |^{2}  \left[\frac{x}{2} - \frac{L_{x}}{n\pi} \sin\left( \frac{2n\pi y}{L_{x}} \right) \right]_{0}^{L_{x}} \; \left[\frac{y}{2} - \frac{L_{y}}{m\pi} \sin\left( \frac{2m\pi y}{L_{y}} \right) \right]_{0}^{L_{y}} \\
&= | E |^{2} \left[\frac{L_{x}}{2} - \frac{L_{x}}{n\pi} \sin\left( 2n\pi \right) \right] \; \left[\frac{L_{y}}{2} - \frac{L_{y}}{m\pi} \sin\left( 2m\pi \right) \right] \\
&= | E |^{2} \frac{L_{x}L_{y}}{4}
\end{align}
$$
Entonces podemos obtener la constante de normalización $E$:
$$
E = \sqrt{ \frac{4}{L_{x}L_{y}} }
$$

#### Solución
La función de onda para una partícula encerrada en una caja bi-dimensional esta dada por:
$$
\psi_{n,m}(x, y) = \sqrt{ \frac{4}{L_{x}L_{y}} } \; \sin\left( \frac{n\pi y}{L_{x}} \right)\;\sin\left( \frac{m\pi y}{L_{y}} \right)
$$
con el espectro de energía dado por:
$$
E_{n, m} = \frac{\hbar^{2}\pi^{2}}{2m} \left( \frac{n^{2}}{L_{x}^{2}}+\frac{m^{2}}{L_{y}^2} \right)
$$
