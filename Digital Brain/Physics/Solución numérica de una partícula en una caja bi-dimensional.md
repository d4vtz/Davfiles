#Cuántica 
#Ejemplos
#Solución/Numérica 

Para obtener una solución numérica para una partícula confinada en una caja bi-dimensional, necesitamos discretizar la región que confina a la partícula:
$$
\begin{align}
& 0 \leq x \leq L_{x} \\
& 0 \leq y \leq L_{y}
\end{align}
$$
Por lo que si dividimos las coordenadas $x$ y $y$ en $N$ y $M$ sub intervalos con longitud $\Delta x$ y $\Delta y$ respectivamente obtenemos:
$$
\begin{align}
x_{n} &= n \Delta x \\
y_{m} &= m \Delta y
\end{align}  
$$ 

Por otro lado, dado que los estado $\psi(x, y)$ al momento de discretizar el espacio, estos estados forman una matriz $\psi$ de tamaño $N \times M$ con elementos $\psi_{n,m} = \psi(x_{n}, y_{m})$, por lo que al discretizar la ecuación de Schrodinger y obtener un sistema de ecuaciones de valores propios. Es necesario expresar a la matriz $\psi$ como un vector de modo que las $N$ columnas  se apilen una tras otra, por lo que se formaría un vector de tamaño $NM$:

$$
\psi =
\begin{pmatrix}
\psi_{1,1} \\
\psi_{1,2} \\
\psi_{1,3} \\
\vdots \\
\psi_{n,m} \\
\vdots \\
\psi_{N,M} \\
\end{pmatrix}
$$
De modo que para para obtener el elemento $\psi_{a}$ con $a = 1, \cdots,NM$ tenemos las siguientes expresiones:
$$
a = m q + r
$$
donde q y $r$ son la division entera y residuo entre $m$ y $n$ respectivamente.

Por lo que la ecuación de Schrodinger toma la forma:

$$
\mathbf{H} \psi = E \psi
$$
Donde la matriz $\mathbf{H}$ tiene tamaño $N \times M$. Por lo es necesario encontrar una forma de discretizar el Hamiltonano:
$$
\mathbf{H} = - \frac{\hbar^{2}}{2m}\mathbf{\nabla}^{2}  
$$
por lo que necesitamos discretizar el operador laplaciano en 2 dimensiones, por lo que utilizaremos [la suma de Kronecker para discretizar laplacianos](https://en.wikipedia.org/wiki/Kronecker_sum_of_discrete_Laplacians) el cual nos dice que:
$$
\begin{align}
\nabla^{2} &= {\mathbf {D_{{xx}}}}\oplus {\mathbf {D_{{yy}}}} \\
&= {\mathbf {D_{{xx}}}}\otimes {\mathbf {I}} +{\mathbf {I}}\otimes {\mathbf {D_{{yy}}}}
\end{align}
$$

dónde $\mathbf{D_{xx}}$ y $\mathbf{D_{yy}}$ representan laplacianos discretos en una dimensión.

### Discretización del Laplaciano

Para ello haremos uso de [[método de diferencias finitas]] de modo que podemos representar al laplaciano como:
$$
\begin{align}
\mathbf{D_{xx}} \; f &= \frac{d^{2}f}{d x^{2}} \\
&= \frac{f_{n+1} - 2 f_{n} + f_{n-1}}{\Delta x^{2}} \\
&= \frac{1}{\Delta x^{2}} f_{n+1} - \frac{2}{\Delta x^{2}} f_{n} + \frac{1}{\Delta x^{2}} f_{n-1} \\ \\
&= \frac{1}{\Delta x^{2}} \begin{pmatrix}
-2 & 1 & 0 & 0 & \cdots & 0 \\
1 & -2 & 1 & 0 & \cdots & 0 \\
0 & 1 & -2 & 1 & \cdots & 0 \\
0 & 0 & 1 & -2 &  \ddots & 0 \\
\vdots & \vdots & \vdots & \ddots & \ddots  & \vdots \\
0 & 0 & 0 & 0 & \cdots  & -2
\end{pmatrix}
\begin{pmatrix}
f_{1} \\
f_{2} \\
\vdots \\
f_{n} \\
\vdots \\
f_{N} \\
\end{pmatrix}
\end{align}
$$
Sea:
$$
\mathbf{D} = \begin{pmatrix}
-2 & 1 & 0 & 0 & \cdots & 0 \\
1 & -2 & 1 & 0 & \cdots & 0 \\
0 & 1 & -2 & 1 & \cdots & 0 \\
0 & 0 & 1 & -2 &  \ddots & 0 \\
\vdots & \vdots & \vdots & \ddots & \ddots  & \vdots \\
0 & 0 & 0 & 0 & \cdots  & -2
\end{pmatrix}
$$
Por lo tanto podemos escribir:

$$
\begin{align}
\mathbf{D_{xx}} &= \frac{1}{\Delta x^{2}} \; \mathbf{D}\\
\mathbf{D_{yy}} &= \frac{1}{\Delta y^{2}} \; \mathbf{D}
\end{align}
$$
Por lo tanto la discretización del laplaciano esta dada por:

$$
\begin{align}
\nabla^{2} &= {\mathbf {D_{{xx}}}}\otimes {\mathbf {I}} +{\mathbf {I}}\otimes {\mathbf {D_{{yy}}}} \\
&= \frac{1}{\Delta x^{2}} \left( \mathbf{D} \otimes \mathbf{I} \right) + \frac{1}{\Delta y^{2}} \left( \mathbf{I} \otimes \mathbf{D} \right)
\end{align}
$$
El cual seria una matriz de tamaño $NM \times NM$. De modo que el Hamiltoniano esta dado por:
$$
\mathbf{H}=  \frac{\hbar^{2}}{2m} \left[ \frac{1}{\Delta x^{2}} \left( \mathbf{D} \otimes \mathbf{I} \right) + \frac{1}{\Delta y^{2}} \left( \mathbf{I} \otimes \mathbf{D} \right) \right]
$$

### Implementación
