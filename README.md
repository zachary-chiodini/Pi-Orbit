# pi-orbit
Visualizing N Digits of Pi as Motion in an Inverse Square Force Field with Linear Resistance

<p align="justify">
    The location of the Nth digit of Pi is denoted by <i>P<sub>n</sub>(x<sub>n</sub>, y<sub>n</sub>)</i>, with position vector <i>r̂<sub>n</sub>r<sub>n</sub></i>. The location of the particle is denoted by <i>P(x, y)</i>.
</p>
<p align="center">
    <img src="photos/graph.png">
</p>

<p align="center">
    <img src="photos/form1.png">
</p>

<p>
    Zero subscript denotes a constant value.
</p>

<p align="center">
    <img src="photos/form2.png">
</p>

<p align="center">
    <img src="photos/form3.png">
</p>
<h1>Algorithm</h1>
<p>
    Provided <i>Δt</i> is close enough to zero
</p>
<p align="center">
    <img src="photos/form4.png">
</p>

<p align="center">
    <img src="photos/form5.png">
</p>

<p align="center">
    <img src="photos/form6.png">
</p>

<p align="center">
    <img src="photos/form7.png">
</p>

<h1>Try It</h1>

```python
from piorbit import PiOrbit
```


```python
orbit = PiOrbit( n = 10, k = 10, c = 20, h = 0.01, lim = 0.1 )
orbit.start()
```
