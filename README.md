# Hebb's rule of neuron learning
[[English]](README.md) [[Русский]](README.ru.md)

Program for training bipolar and binary neurons according to Hubb's rule.

The program considers one neuron, which receives the features of the example as input.

### Neuron parameters:
- number of neuron inputs ![equation](https://latex.codecogs.com/svg.image?x_{i}), ![equation](https://latex.codecogs.com/svg.image?i=1,...,n);
- weights ![equation](https://latex.codecogs.com/svg.image?w_{i}), ![equation](https://latex.codecogs.com/svg.image?i=1,...,n) corresponding to the input of the neuron ![equation](https://latex.codecogs.com/svg.image?x_{i});
- additional input to improve neuron tuning ![equation](https://latex.codecogs.com/svg.image?x_{0});
- additional weight to improve neuron tuning ![equation](https://latex.codecogs.com/svg.image?w_{0});
- neuron output ![equation](https://latex.codecogs.com/svg.image?y).

The output of a neuron, depending on the type of neuron, can take the following values:
- binary neuron – values 1 or 0;
- bipolar neuron – values 1 or -1.

The weights at the inputs of the neuron are calculated according to the Hebb's rule.

### Hebb's rule for a bipolar neuron

![equation](https://latex.codecogs.com/svg.image?w_{i}=w_{i}&plus;x_{i}^{k}y,i=0,...n),

where ![equation](https://latex.codecogs.com/svg.image?w_{i}) – weight of the ![equation](https://latex.codecogs.com/svg.image?i)-th connection of the neuron;

![equation](https://latex.codecogs.com/svg.image?i) – neuron input number;

![equation](https://latex.codecogs.com/svg.image?k) – number of the example fed to the neuron.

### Hebb's rule for a binary neuron

![equation](https://latex.codecogs.com/svg.image?w_{i}=w_{i}&plus;\partial_{i},i=0,...,n),

<img src="https://latex.codecogs.com/svg.image?\partial_{i}=\begin{Bmatrix}1,if\;x_{i}^{k}y=1&space;\\0,if\;x_{i}^{k}=0&space;\\-1,if\;(x_{i}^{k}\neq0)\&(y=0)\end{Bmatrix}" />

where ![equation](https://latex.codecogs.com/svg.image?w_{i}) – weight of the ![equation](https://latex.codecogs.com/svg.image?i)-th connection of the neuron;

![equation](https://latex.codecogs.com/svg.image?i) – neuron input number;

![equation](https://latex.codecogs.com/svg.image?k) – number of the example fed to the neuron;

![equation](https://latex.codecogs.com/svg.image?\partial_{i}) – corrective weights of the ![equation](https://latex.codecogs.com/svg.image?i)-th connection of the neuron.

Neuron training is carried out with a teacher, that is, according to precedents. Therefore, each training example is given a reference neuron response.
