
Para poder resolver la ecuación de Schrodinger para una partícula en una caja circular, primero necesitamos discretizar el laplaciano en coordenadas polares,

$$
\nabla^{2}f(r, \theta) = \frac{\partial^{2} f}{\partial r^{2}} + \frac{1}{r}\frac{\partial f}{\partial r} + \frac{1}{r^{2}} \frac{\partial^{2} f}{\partial \theta^{2}}
$$

Para ello haremos uso del [[método de diferencias finitas]] de modo que remplazando:
![[método de diferencias finitas#Derivada central]]
![[método de diferencias finitas#Segunda derivada central]]

Por lo tanto,
$$
\nabla^{2} f = \frac{f(r+h, \theta) - 2f(r, \theta) + f(r-h, \theta)}{\Delta r^{2}} + \frac{1}{r} \frac{f(r+h, \theta) - f(r-h, \theta)}{2\Delta r} + \frac{1}{r^{2}} \frac{f(r, \theta+h) - 2f(r, \theta) + f(r, \theta-h)}{\Delta \theta^{2}}
$$

Si separamos la parte radial y la parte angular y las nombramos $D_{rr}$ y $D_{\theta\theta}$ respectivamente obtenemos:

$$
\begin{align}
D_{rr} &= \frac{f(r+h, \theta) - 2f(r, \theta) + f(r-h, \theta)}{\Delta r^{2}} + \frac{1}{r} \frac{f(r+h, \theta) - f(r-h, \theta)}{2\Delta x} \\
&= \left( \frac{1}{\Delta r^{2}} + \frac{1}{2r \Delta r} \right) f(r+h, \theta) - \frac{2}{\Delta r^{2}} f(r, \theta) + \left( \frac{1}{\Delta r^{2}} - \frac{1}{2r \Delta r} \right)f(r - h, \theta) \\
&= \left( \frac{1}{\Delta r^{2}} + \frac{1}{2r_{n} \Delta r} \right) f(r_{n+1}, \theta_{n}) - \frac{2}{\Delta r^{2}} f(r_{n}, \theta_{n}) + \left( \frac{1}{\Delta r^{2}} - \frac{1}{2r_{n} \Delta r} \right)f(r_{n-1}, \theta_{n}) \\
&=  \frac{1}{\Delta r^{2}} \left[ \left( 1 + \frac{\Delta r}{2r_{n} } \right) f(r_{n+1}, \theta_{n}) - 2 f(r_{n}, \theta_{n}) + \left( 1 - \frac{\Delta r}{2r_{n}} \right)f(r_{n-1}, \theta_{n}) \right]. 
\end{align}
$$

$$
\begin{align}
D_{\theta \theta} &= \frac{1}{r^{2}} \frac{f(r, \theta+h) - 2f(r, \theta) + f(r, \theta-h)}{\Delta \theta^{2}} \\
&= \frac{1}{r^{2}\Delta \theta^{2}} ( f(r, \theta+h) - 2f(r, \theta) + f(r, \theta-h)) \\
&= \frac{1}{r_{n}^{2}\Delta \theta^{2}} ( f(r_{n}, \theta_{n+1}) - 2f(r_{n}, \theta_{n}) + f(r_{n}, \theta_{n-1})) 
\end{align}
$$