
Este es un método numérico para poder calcular la derivada $f^{\prime}(x_{0})$ un un punto $x_{0}$ dado. Para ello hacemos uso del polinomio de Taylor:

$$
f(x + h) = \sum_{n=0}^{\infty} \frac{h^n}{n!} f^{(n)}(x)
$$

### Primera derivada

Analizaremos el método de diferencias finitas para la primera derivada:

#### Derivada hacia delante

Si aproximamos la función a primer orden,
$$
f(x + h) \approx f(x) + h f^{\prime}(x),
$$
obteniendo:
$$
f^{\prime}(x) \approx \frac{f(x + h) - f(x)}{h}
$$
La cual seria le conoce como derivada hacia delante, ya que el incremento $h$ se realiza hacia la derecha del punto $x$.

#### Derivada hacia atrás

Por otro lado, si calculamos la función $f(x - h)$ a primer orden obtenemos,
$$
f(x - h)  \approx f(x) - h f^{\prime}(x),
$$
de modo que,
$$
 f^{\prime}(x) \approx \frac{f(x) - f(x-h)}{h}
$$
Expresión que se conoce como derivada hacia atrás.

#### Derivada central

Por otro lado, si sumamos ambas derivadas hacia delante y hacia atrás podemos calcular:
$$
f^{\prime}(x) \approx \frac{f(x+h) -f(x-h)}{2h}
$$
### Segunda derivada

De igual manera, si calculamos la aproximación de la función $f(x \pm h)$ a primer segundo orden,
$$
f(x \pm h) \approx f(x) \pm h f^{\prime}(x) + \frac{h^2}{2} f^{\prime \prime }(x),
$$
#### Derivada hacia delante
Para ello usaremos la aproximación de la función $f(x + 2h)$, además usaremos la aproximación de la primera derivada hacia delante:
$$
\begin{align}
f(x + 2h) &\approx f(x) + 2h f^{\prime}(x) + \frac{4h^2}{2} f^{\prime \prime }(x), \\
f^{\prime \prime }(x) &\approx \frac{f(x+2h)-f(x)}{2h^{2}} - \frac{f^{\prime}(x)}{h}, \\
f^{\prime \prime }(x) &\approx \frac{f(x+2h)-f(x)}{2h^{2}} - \frac{2f(x + h) - 2f(x)}{2h^2},  \\
f^{\prime \prime }(x) &\approx \frac{f(x+2h) -2 f(x+h) +f(x)}{h^{2}}.
\end{align}
$$

#### Derivada hacia atrás
Usaremos s la aproximación de la función $f(x - 2h)$, además usaremos la aproximación de la primera derivada hacia atrás:
$$
\begin{align}
f(x - 2h) &\approx f(x) - 2h f^{\prime}(x) + \frac{4h^2}{2} f^{\prime \prime }(x), \\
f^{\prime \prime }(x) &\approx \frac{f(x-2h)-f(x)}{2h^{2}} + \frac{f^{\prime}(x)}{h}, \\
f^{\prime \prime }(x) &\approx \frac{f(x-2h)-f(x)}{2h^{2}} + \frac{2f(x) - 2f(x - h)}{2h^2},  \\
f^{\prime \prime }(x) &\approx \frac{f(x-2h) - 2 f(x) + f(x-1)}{h^{2}}.
\end{align}
$$

#### Segunda derivada central
Sumando las derivadas hacia delante y hacia atrás obtenemos:
$$
f^{\prime \prime }(x) \approx \frac{f(x+h) - f(x) + f(x-h)}{h^2}
$$
