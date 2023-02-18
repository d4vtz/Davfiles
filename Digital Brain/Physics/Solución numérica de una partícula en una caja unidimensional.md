#Cuántica 
#Ejemplos
#Solución/Numérica

Nuestra meta es obtener los auto valores $E_{n}$ y auto estados $\psi_{n}(x)$ para la ecuación de Schrodinger:
$$
-\frac{\hbar^{2}}{2m} \frac{d^{2} \psi}{dx^{2}} = E \; \psi(x)
$$
Para fines prácticos usaremos unidades naturales, es decir, $\hbar=1$. Por otro lado si dividimos  por $L^2$ toda la ecuación, obteniendo una ecuación a dimensional en el espacio de tal manera que podemos escribir:
$$
-\frac{d^{2} \psi}{dy^{2}} = 2 m E \; \psi(y) \;\;\;\;\;\;\;\;\;\;\; y=\frac{x}{L}
$$

dado que $y$ es una variable muda, entonces podemos volver a a cambiar a $x$, de modo que el intervalo de las condiciones de contorno cambian a:
$$
\begin{align}
\psi(0)&=0 \\
\psi(1)&=0.
\end{align}
$$


Para obtener la solución numérica, es necesario discretizar el operador Hamiltoniano $\hat{H}$, para ello necesitamos encontrar la forma que toman las derivadas. Para ello hacemos uso del [[método de diferencias finitas]].

De modo que si dividimos el espacio $0 \leq x \leq 1$ en $N$ sub intervalos equidistantes entonces la longitud de cada nodo estará dada por:
$$
\Delta x = \frac{1}{N}
$$
además para obtener la posición de cualquier nodo:
$$
x_{n} = n \Delta x
$$

Si hacemos uso de las derivada central para la segunda derivada, 
$$
\begin{align}
\frac{d^{2}\psi}{dx^{2}} &\approx \frac{\psi(x_{n} + \Delta x) - 2 \psi(x_{n}) + \psi(x_{n} - \Delta x)}{\Delta x^2}\\
 &\approx \frac{\psi(x_{n+1}) - 2 \psi(x_{n}) + \psi(x_{n-1})}{\Delta x^2}
\end{align}
$$


Por lo tanto, si aplicamos esto a nuestra ecuación de Schrodinger:
$$
\begin{align}
- \frac{\psi(x_{n+1}) - 2 \psi(x_{n}) + \psi(x_{n-1})}{\Delta x^{2}} &= 2 m E \; \psi(x_{n}) \\
- \frac{1}{\Delta x^{2}} \psi(x_{n+1}) + \frac{2}{\Delta x^{2}} \psi(x_{n}) -  \frac{1}{\Delta x^{2}} \psi(x_{n-1}) &= 2 m E \; \psi(x_{n})
\end{align}
$$
Esta expresión representa un sistema de $N+1$ ecuaciones, de modo que podemos representarlo como una ecuación matricial de la forma:

$$
\mathbf{H}\mathbf{\psi} = 2 m E \psi
$$
con $\mathbf{H}$ y $\psi$ dados por: 

$$
\mathbf{H} = \frac{1}{\Delta x^{2}}
\begin{pmatrix}
2 & -1 &  0 & 0 &\cdots & 0  \\
-1 & 2 & -1 & 0 & \dots & 0 \\
0 & -1 & 2 & \ddots & \cdots  & 0 \\
\vdots & 0 & \ddots & \ddots & \cdots & \vdots \\
\vdots & \vdots & \vdots & \vdots & 2 & -1 \\
0 & \cdots & \cdots & \cdots & -1 & 2
\end{pmatrix}
\;\;\;\;\;\;\;
\psi = \begin{pmatrix}
\psi(x_{1}) \\
\vdots \\
\vdots \\
\vdots \\
\vdots \\
\psi(x_{N+1})
\end{pmatrix}
$$

De modo que si encontramos los valores propios de la matriz $\mathbf{H}$ obtendremos los los posibles valores de la energía así como los auto estados de la partícula con esa energía asociada.

#### Implementación

Por lo que procederemos a resolver este sistema con ayuda de un script de python:

```python
import numpy as np
import matplotlib.pyplot as plt
import matplotlib
matplotlib.use("GTK3Agg")


class ParticleInAbox:
    N = 1000
    HBAR = 1.0
    M = 1.0
    L = 1.0
    h = L / N

    def __init__(self) -> None:
        # Create  vectors
        self.x = (1 / self.L) * np.linspace(0, self.L, self.N)
        self.hamiltonian = self._gen_hammiltonian()

        self.energy, self.psi = self._diagonalize()
```

Creando una clase para facilitar la estructura de la solución, en el constructor podemos ver que se define el mallado del espacio $0\leq x \leq 1$ con $N$ particiones con un espaciado uniforme de tamaño $h = \frac{1}{N}$.

#### Generar Hamiltoniano

Además generamos el operador Hamiltoniano $\mathbf{H}$ por medio del método:
```python
    def _gen_hammiltonian(self):
        main = (self.HBAR**2) / (self.M * self.h**2) * np.ones(self.N)
        secundary = -(self.HBAR**2) / (2 * self.M * self.h**2) * np.ones(self.N - 1)
        return np.diag(main, k=0) + np.diag(secundary, k=1) + np.diag(secundary, k=-1)
```

este método nos retorna una matriz tridiagonal de tamaño $N \times N$ con diagonal principal un array de tamaño $N$ con valor principal $\frac{1}{h^{2}}$ y dos diagonales secundarias de tamaño $N-1$ y valor $-\frac{1}{2h^{2}}$.

#### Resolución del sistema de valores propios

En el constructor de la clase, hacemos uso del método `self._diagonalize()` el cual retorna un array `energy` y `psi` los cuales son los valores propios y vectores propios del Hamiltoniano. 
```python
   def _diagonalize(self):
        # Diagonalize Hamiltonian
        energy, _psi = np.linalg.eigh(self.hamiltonian)
        psi = self._normalize(np.transpose(_psi))
        return energy, psi
```

Este método hace uso de la función `np.linal.eigh` el cual forma parte de el modulo `numpy` el cual es el encargado de resolver el sistema, toma como entrada una matriz hermitiana compleja a diagonalizar y nos retorna dos objetos:

- Un array con los valores propios ordenados de menor a mayor.
- Una matriz con los vectores columna como vectores propios. Dado que necesitamos los vectores columna, para poder acceder de una manera sencilla la tenemos que transponer.

#### Normalización de los auto estados 
Dado que los vectores propios no están normalizados es necesario hacerlo para preservar la densidad de probabilidad.

Para ello, sabemos que para que un auto estado $\psi_{n}(x)$ se encuentre normalizado, se tiene que cumplir con:
$$
\begin{equation}
1 = \int_{0}^{1} \psi_{n}^{*}(x) \psi_{n}(x)\, dx 
\end{equation}
$$
Por lo que si suponemos que las soluciones $\psi_{n}(x)$ encontradas se pueden escribir de la forma:
$$
\psi_{n}(x) = A_{n} \; \phi(x)
$$
de modo que su norma esta dada por:
$$
1 = | A_{n} |^{2} \int_{0}^{1}\phi_{n}^{*}(x) \phi_{n}(x) \, dx 
$$
Por lo que si despejamos $A$:
$$
| A_{n} | = \frac{1}{\sqrt{ \displaystyle\int_{0}^{1}\phi_{n}^{*}(x) \phi_{n}(x) \, dx }}
$$

Por lo que nos basta con multiplicar todos los auto estados por este factor para obtener estados normalizados.

Para aplicar esto tenemos el método `self._normalize()` el cual toma como entrada la matriz transpuesta de los auto estados.
```python
    def _normalize(self, psi):
        # Normalize self states
        for i in range(len(self.hamiltonian)):
            psi[i] = psi[i] / np.sqrt(np.trapz(psi[i] ** 2, self.x))
        return psi
```

De modo que recorremos cada vector de la matriz y la multiplicamos por el factor $|A_{n}|$, para ello usamos uso de la función `np.trapz` de numpy para calcular la integral de manera numérica.

#### Gráficas

Por último generaremos unas gráficas para poder visualizar mejor los resultados de la simulación con ayuda de unos métodos implementados con ayuda del modulo `matplotlib`.

```python
    def graph_energies(self, n):
        plt.figure(figsize=(6, 3), dpi=300)
        plt.bar(np.arange(n + 1), self.energy[: n + 1])
        plt.xlabel("$n$")
        plt.ylabel("Energía")
        plt.title("Niveles de energía $E_n$")
        plt.savefig("Energies.png", dpi=300)
        plt.show()

    def graph_state(self, n):
        plt.figure(figsize=(6, 3), dpi=300)
        plt.plot(self.x, self.psi[n - 1], label=f"$\\psi_{n}(x)$")
        plt.xlabel("$x$")
        plt.ylabel("$\\psi(x)$")
        plt.title(f"Auto estado $\\psi_{n}(x)$")
        plt.legend()
        plt.savefig(f"State_{n}.png", dpi=300)
        plt.show()

    def graph_states(self, n):
        plt.figure(figsize=(6, 3), dpi=300)
        for i in range(n):
            plt.plot(self.x, self.psi[i], label=f"$\\psi_{i + 1}(x)$")
            plt.legend()

        plt.xlabel("$x$")
        plt.ylabel("$\\psi(x)$")
        plt.title(f"Auto estados $\\psi_n(x)$")
        plt.savefig("States.png", dpi=300)
        plt.show()

    def graph_density(self, n):
        plt.figure(figsize=(6, 3), dpi=300)
        plt.plot(self.x, self.psi[n - 1] ** 2)
        plt.xlabel("x")
        plt.ylabel("$|\\psi(x)|^2$")
        plt.title(f"Densidad de probabilidad para el auto estado $\\psi_{n}(x)$")
        plt.savefig(f"Density_state_{n}.png", dpi=300)
        plt.show()

    def graph_multiple_density(self):
        _, ax = plt.subplots(nrows=2, ncols=2, figsize=(6, 8), dpi=300)
        n = 1
        for i in range(2):
            for j in range(2):
                ax[i, j].plot(self.x, self.psi[n - 1] ** 2)
                ax[i, j].set_title(f"$|\\psi_{n}(x)|^2$")
                n += 1
        plt.suptitle("Densidad de probabilidad para los auto estados")
        plt.savefig("Density_state.png", dpi=300)
```

![[filename.png]]
![[Energies.png]]
![[States.png]]
![[Density_state_2.png]]
![[Density_state 6.png]]