# pi-orbit
Visualizing N Digits of Pi as Orbital Motion with Linear Resistance

<p align="center">
    <img src="photos/graph.png">
</p>

<p align="center">
    <img src="photos/form1.png">
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
