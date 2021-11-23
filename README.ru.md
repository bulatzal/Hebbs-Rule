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

## Выполнение алгоритма Хебба
### Пример 1 (Биполярный нейрон)
Требуется обучить биполярный нейрон распознаванию изображений ![equation](https://latex.codecogs.com/svg.image?X^{1}) и ![equation](https://latex.codecogs.com/svg.image?X^{2}).

![image](https://i.imgur.com/HDagVL5.png)

Нейрон биполярный, поэтому потребуем, чтобы изображению ![equation](https://latex.codecogs.com/svg.image?X^{1}) соответствовал выходной сигнал нейрона +1, а изображению ![equation](https://latex.codecogs.com/svg.image?X^{2}) соответствовал выходной сигнал нейрона -1.

#### Шаг 1. Задание исходных значений
Задаётся множество ![equation](https://latex.codecogs.com/svg.image?M), которое включает описание примера и целевое значение выхода для примера.
В множестве ![equation](https://latex.codecogs.com/svg.image?M) описаны буквы:

![equation](https://latex.codecogs.com/svg.image?X^{1}=(1,-1,1,1,1,1,-1,-1,1),)

![equation](https://latex.codecogs.com/svg.image?X^{2}=(1,1,1,1,-1,1,1,-1,1),)

значение подстроечного нейрона ![equation](https://latex.codecogs.com/svg.image?x_{0}=1), также описаны эталонные выходы ![equation](https://latex.codecogs.com/svg.image?Y^{1}=1,Y^{2}=-1.)

Тогда множество ![equation](https://latex.codecogs.com/svg.image?M) имеет вид:

<img src="https://latex.codecogs.com/svg.image?M=\left\{(x_{0},X^{1},Y^{1});(x_{0},X^{2},Y^{2})\right\};" />

<img src="https://latex.codecogs.com/svg.image?M=\begin{Bmatrix}1,X^{1}=(1,-1,1,1,1,1,-1,-1,1),Y^{1}=1;\\1,X^{2}=(1,1,1,1,-1,1,1,-1,1),Y^{2}=-1;\end{Bmatrix}" />.

Инициируются весовые коэффициенты связей нейрона, но поскольку это первый шаг, то веса неизвестны, поэтому зададим их нулевыми.

![equation](https://latex.codecogs.com/svg.image?w_{i}=0,i=0,...,9.)

#### Шаг 2. Инициация входов и выхода нейрона изображения (Изображение 1)
<img src="https://latex.codecogs.com/svg.image?\begin{matrix}X^{1}=(x_{1}^{1},...,x_{9}^{1})=(1,-1,1,1,1,1,-1,-1,1)\\x_{0}=1,x_{i}=x_{i}^{1},i=1,...,9\end{matrix}." />

Получаем набор элементов:

![equation](https://latex.codecogs.com/svg.image?x_{0}=1,x_{1}=1,x_{2}=-1,x_{3}=x_{4}=x_{5}=x_{6}=1,x_{7}=x_{8}=-1,x_{9}=1.)


![equation](https://latex.codecogs.com/svg.image?y=Y^{1}=1.)

#### Шаг 3. Корректировка веса связей нейрона по правилу Хебба (Изображение 1)
![equation](https://latex.codecogs.com/svg.image?w_{i}=w_{i}&plus;x_{i}y,i=0,...,9.)

На данный момент исходные значения весовых коэффициентов равны нулю. Пересчитаем значения весовых коэффициентов по правилу Хебба:

<img src="https://latex.codecogs.com/svg.image?\begin{matrix}w_{0}=w_{0}&plus;x_{0}y=0&plus;1*1=1;\\w_{1}=w_{1}&plus;x_{1}^{1}y=0&plus;1*1=1;\\w_{2}=w_{2}&plus;x_{2}^{1}y=0&plus;(-1)*1=-1;\\...\\w_{9}=w_{9}&plus;x_{9}^{1}y=0&plus;1*1=1.\end{matrix}" />

Получен вектор из 10 весовых коэффициентов ![equation](https://latex.codecogs.com/svg.image?w=(1,1,-1,1,1,1,1,-1,-1,1).)


#### Шаг 2. Инициация входов и выхода нейрона изображения (Изображение 2)
<img src="https://latex.codecogs.com/svg.image?\begin{matrix}X^{2}=(x_{1}^{2},...,x_{9}^{2})=(1,1,1,1,-1,1,1,-1,1)\\x_{0}=1,x_{i}=x_{i}^{2},i=1,...,9\end{matrix}." />

![equation](https://latex.codecogs.com/svg.image?y=Y^{2}=-1.)

#### Шаг 3. Корректировка веса связей нейрона по правилу Хебба (Изображение 2)
Ранее были получены значения ![equation](https://latex.codecogs.com/svg.image?w=(1,1,-1,1,1,1,1,-1,-1,1).)

Пересчитаем значения весовых коэффициентов:

<img src="https://latex.codecogs.com/svg.image?\begin{matrix}w_{0}=w_{0}&plus;x_{0}y=1&plus;1*(-1)=0\\w_{1}=w_{1}&plus;x_{1}^{2}y=1&plus;1*(-1)=0\\w_{2}=w_{2}&plus;x_{2}^{2}y=-1&plus;1*(-1)=-2\\...\\w_{9}=w_{9}&plus;x_{9}^{2}y=1&plus;1*(-1)=0.\end{matrix}" />

Получен вектор весовых коэффициентов ![equation](https://latex.codecogs.com/svg.image?w=(0,0,-2,0,0,2,0,-2,0,0).)

#### Шаг 4. Проверка качества обучения
Проверяем условия остановки обучения для найденных значений весовых коэффициентов:

<img src="https://latex.codecogs.com/svg.image?\begin{matrix}y^{k}=\left\{\begin{matrix}1,if\:S^{k}>0,\\-1,if\:S^{k}\end{matrix}\right.\\S^{k}=\sum_{i=1}^{n}x_{i}^{k}w_{i}&plus;w_{0}\end{matrix}" />

##### Первое изображение
![equation](https://latex.codecogs.com/svg.image?S^{1}=\sum_{i=1}^{9}x_{i}^{1}w_{i}&plus;w_{0}=1*0&plus;(-1)*(-2)&plus;1*0&plus;1*0&plus;1*2&plus;1*0&plus;(-1)*(-2)&plus;(-1)*0&plus;1*0&plus;0=6,)

Выход нейрона ![equation](https://latex.codecogs.com/svg.image?y^{1}=1) равен , так как ![equation](https://latex.codecogs.com/svg.image?S^{1}>0.)

##### Второе изображение
![equation](https://latex.codecogs.com/svg.image?S^{2}=\sum_{i=1}^{9}x_{i}^{2}w_{i}&plus;w_{0}=1*0&plus;1*(-2)&plus;1*0&plus;1*0&plus;(-1)*2&plus;1*0&plus;1*(-2)&plus;(-1)*0&plus;1*0&plus;0=-6,)

Выход нейрона ![equation](https://latex.codecogs.com/svg.image?y^{2}=-1) равен , так как ![equation](https://latex.codecogs.com/svg.image?S^{2}<0.)

Вектор ![equation](https://latex.codecogs.com/svg.image?(y^{1},y^{2})=(1,-1)) равен целевому вектору ![equation](https://latex.codecogs.com/svg.image?(Y^{1},Y^{2}),) цель достигнута и нейрон правильно распознает заданные изображения.

Если совпадение не достигнуто, повторяем шаги 2-3 многократно для каждого изображения, пока не получим требуемое значение выходных сигналов нейрона ![equation](https://latex.codecogs.com/svg.image?(y^{1},y^{2})=(Y^{1},Y^{2}).)
