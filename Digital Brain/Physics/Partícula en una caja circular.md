
Para resolver este sistema físico, primero necesitamos poder definir nuestro Hamiltoniano. 
$$
\hat{H} = - \frac{\hbar^{2}}{2m} \nabla^{2}  + V(\mathbf{r})
$$

Dado que en la partícula no tiene un potencial dentro de la caja, entonces $V(\mathbf{r}) = 0$, por lo que necesitamos resolver la siguiente ecuación de Schrodinger:

$$
- \frac{\hbar^{2}}{2m}\nabla^{2} \psi = E \; \psi
$$

Dado que la partícula se encuentra encerrada en un caja circular, entonces podemos resolver el sistema en coordenadas polares, de modo que $\psi = \psi(r, \theta)$, por lo que las condiciones de frontera están dadas por:
$$
\begin{align}
\psi(r,0) &= \psi(r, 2\pi)\\
\psi(L,\theta) &= 0
\end{align}
$$

Por lo que necesitamos representar el laplaciano en coordenadas polares:

$$
- \frac{\hbar^{2}}{2m} \left( \frac{1}{r} \frac{\partial}{\partial r} \left[ r \frac{\partial \psi}{\partial r} \right] + \frac{1}{r^{2}} \frac{\partial^{2} \psi}{\partial \theta^{2}}\right) = E \; \psi
$$

Por lo que si aplicamos el método de variables separables, de modo que $\psi(r,\theta) = R(r) \; Y(\theta)$

$$
\begin{align}
& - \frac{\hbar^{2}}{2m} \left( \frac{1}{r} \frac{\partial}{\partial r} \left[ r \frac{\partial \psi}{\partial r} \right] + \frac{1}{r^{2}} \frac{\partial^{2} \psi}{\partial \theta^{2}}\right) = E \; \psi \\
& - \frac{\hbar^{2}}{2m} \left( \frac{Y(\theta)}{r} \frac{d}{dr} \left[ r \frac{dR}{dr} \right] + \frac{R}{r^{2}} \frac{d^{2} Y}{d \theta^{2}}\right) = E \; R \; Y \\
& - \frac{\hbar^{2}}{2m} \left( \frac{1}{rR} \frac{d}{dr} \left[ r \frac{dR}{dr} \right] + \frac{1}{r^{2}Y} \frac{d^{2} Y}{d \theta^{2}}\right) = E \\
\end{align}
$$

Dado que los dos términos del miembro izquierdo son independientes entre si y están igualados a una contante, entonces podemos escribir:

$$
\begin{align}
& - \frac{\hbar^{2}}{2m} \frac{1}{rR} \frac{d}{dr} \left( r \frac{dR}{dr} \right) = \alpha^{2} \\
& - \frac{\hbar^{2}}{2m} \frac{1}{r^{2}Y} \frac{dY}{d\theta} = \beta^{2}.
\end{align}
$$

Con la condición:
$$
E = \alpha^{2} + \beta^{2}
$$

### Resolución de la parte radial

Nuestra ecuación de la parte radial es:

$$
\begin{align}
& \frac{d}{dr}\left( r \frac{dR}{dr} \right) + \frac{2m\alpha^{2} r}{\hbar^{2}} R = 0 \\
& r \frac{d^{2}R}{dr^{2}} + \frac{dR}{dr} + \frac{2m\alpha^{2} r}{\hbar^{2}} R = 0
\end{align}
$$

Dado que se trata de una ecuación diferencial de segundo orden de coeficientes variables, entonces podemos proponer como solución $R(r) = A \; r^\lambda$, por lo que:

$$
\begin{align}
& \lambda(\lambda-1) \; r^{\lambda-1} + \lambda \; r^{\lambda -1} + \frac{2m\alpha^{2}}{\hbar^{2}} r^{\lambda + 1} = 0
\end{align}
$$
