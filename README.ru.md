# Правило обучения нейрона Хебба
[[English]](README.md) [[Русский]](README.ru.md)

Программа обучения биполярного и бинарного нейрона по правилу Хебба.

В программе рассматривается один нейрон, который получает в качестве входных данных признаки примера.

### Параметры нейрона:
- число входов ![equation](https://latex.codecogs.com/svg.image?x_{i}) нейрона, ![equation](https://latex.codecogs.com/svg.image?i=1,...,n);
- весовой коэффициент ![equation](https://latex.codecogs.com/svg.image?w_{i}), ![equation](https://latex.codecogs.com/svg.image?i=1,...,n), который соответствует каждому входу ![equation](https://latex.codecogs.com/svg.image?x_{i}) нейрона;
- дополнительный вход для улучшения подстройки нейрона ![equation](https://latex.codecogs.com/svg.image?x_{0});
- дополнительный вес для улучшения подстройки нейрона ![equation](https://latex.codecogs.com/svg.image?w_{0});
- выход нейрона ![equation](https://latex.codecogs.com/svg.image?y).

Выход нейрона, в зависимости от типа нейрона, может принимать следующие значения:
- бинарный нейрон – значения 1 или 0;
- биполярный нейрон – значения 1 или -1.

Весовые коэффициенты на входах нейрона рассчитываются по правилу Хебба.

### Правило Хебба для биполярного нейрона

![equation](https://latex.codecogs.com/svg.image?w_{i}=w_{i}&plus;x_{i}^{k}y,i=0,...n),

где ![equation](https://latex.codecogs.com/svg.image?w_{i}) – вес ![equation](https://latex.codecogs.com/svg.image?i)-ой связи нейрона;

![equation](https://latex.codecogs.com/svg.image?i) – номер входа нейрона;

![equation](https://latex.codecogs.com/svg.image?k) – номер примера, поданного на нейрон.

### Правило Хебба для бинарного нейрона

![equation](https://latex.codecogs.com/svg.image?w_{i}=w_{i}&plus;\partial_{i},i=0,...,n),

<img src="https://latex.codecogs.com/svg.image?\partial_{i}=\begin{Bmatrix}1,if\;x_{i}^{k}y=1&space;\\0,if\;x_{i}^{k}=0&space;\\-1,if\;(x_{i}^{k}\neq0)\&(y=0)\end{Bmatrix}" />

где ![equation](https://latex.codecogs.com/svg.image?w_{i}) – вес ![equation](https://latex.codecogs.com/svg.image?i)-ой связи нейрона;

![equation](https://latex.codecogs.com/svg.image?i) – номер входа нейрона;

![equation](https://latex.codecogs.com/svg.image?k) – номер примера, поданного на нейрон;

![equation](https://latex.codecogs.com/svg.image?\partial_{i}) – корректирующий вес ![equation](https://latex.codecogs.com/svg.image?i)-ой связи нейрона.

Обучение нейрона проводится с учителем, то есть по прецендентам. Поэтому каждому обучающему примеру задается эталонный ответ нейрона, которого нейрон должен достичь по окончании обучения.
