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

## Executing Hebb's algorithm
### Example 1 (Bipolar neuron)
It's required to train a bipolar neuron to recognize images ![equation](https://latex.codecogs.com/svg.image?X^{1}) and ![equation](https://latex.codecogs.com/svg.image?X^{2}).

![image](https://i.imgur.com/HDagVL5.png)

The neuron is bipolar, so it will be required that the image ![equation](https://latex.codecogs.com/svg.image?X^{1}) corresponds to the output signal of neuron +1, and the image ![equation](https://latex.codecogs.com/svg.image?X^{2}) corresponds to the output signal of neuron -1.

#### Step 1. Setting initial values
A set ![equation](https://latex.codecogs.com/svg.image?M) is given that includes the description of the example and the target output value for the example.
The set ![equation](https://latex.codecogs.com/svg.image?M) describes the letters:

![equation](https://latex.codecogs.com/svg.image?X^{1}=(1,-1,1,1,1,1,-1,-1,1),)

![equation](https://latex.codecogs.com/svg.image?X^{2}=(1,1,1,1,-1,1,1,-1,1),)

the value of the additional input to improve the tuning of the neuron ![equation](https://latex.codecogs.com/svg.image?x_{0}=1), 
reference outputs are also described ![equation](https://latex.codecogs.com/svg.image?Y^{1}=1,Y^{2}=-1.)

Then the set ![equation](https://latex.codecogs.com/svg.image?M) has the form:

<img src="https://latex.codecogs.com/svg.image?M=\left\{(x_{0},X^{1},Y^{1});(x_{0},X^{2},Y^{2})\right\};" />

<img src="https://latex.codecogs.com/svg.image?M=\begin{Bmatrix}1,X^{1}=(1,-1,1,1,1,1,-1,-1,1),Y^{1}=1;\\1,X^{2}=(1,1,1,1,-1,1,1,-1,1),Y^{2}=-1;\end{Bmatrix}" />.

The weights of the connections of the neuron are initiated, but since this is the first step, the weights are unknown, so we set them to zero.

![equation](https://latex.codecogs.com/svg.image?w_{i}=0,i=0,...,9.)

#### Step 2. Initiation of inputs and output of the image neuron (Image 1)
<img src="https://latex.codecogs.com/svg.image?\begin{matrix}X^{1}=(x_{1}^{1},...,x_{9}^{1})=(1,-1,1,1,1,1,-1,-1,1)\\x_{0}=1,x_{i}=x_{i}^{1},i=1,...,9\end{matrix}." />

Got a set of elements:

![equation](https://latex.codecogs.com/svg.image?x_{0}=1,x_{1}=1,x_{2}=-1,x_{3}=x_{4}=x_{5}=x_{6}=1,x_{7}=x_{8}=-1,x_{9}=1.)


![equation](https://latex.codecogs.com/svg.image?y=Y^{1}=1.)

#### Step 3. Correction of the weight of the neuron connections according to Hebb's rule (Image 1)
![equation](https://latex.codecogs.com/svg.image?w_{i}=w_{i}&plus;x_{i}y,i=0,...,9.)

At the moment, the initial values of the weights are zero. Let's recalculate the values of the weight coefficients according to the Hebb's rule:

<img src="https://latex.codecogs.com/svg.image?\begin{matrix}w_{0}=w_{0}&plus;x_{0}y=0&plus;1*1=1;\\w_{1}=w_{1}&plus;x_{1}^{1}y=0&plus;1*1=1;\\w_{2}=w_{2}&plus;x_{2}^{1}y=0&plus;(-1)*1=-1;\\...\\w_{9}=w_{9}&plus;x_{9}^{1}y=0&plus;1*1=1.\end{matrix}" />

The vector of 10 weights is obtained ![equation](https://latex.codecogs.com/svg.image?w=(1,1,-1,1,1,1,1,-1,-1,1).)


#### Step 2. Initiation of inputs and output of the image neuron (Image 2)
<img src="https://latex.codecogs.com/svg.image?\begin{matrix}X^{2}=(x_{1}^{2},...,x_{9}^{2})=(1,1,1,1,-1,1,1,-1,1)\\x_{0}=1,x_{i}=x_{i}^{2},i=1,...,9\end{matrix}." />

![equation](https://latex.codecogs.com/svg.image?y=Y^{2}=-1.)

#### Step 3. Correction of the weight of the neuron connections according to Hebb's rule (Image 2)
Previously received values ![equation](https://latex.codecogs.com/svg.image?w=(1,1,-1,1,1,1,1,-1,-1,1).)

Let's recalculate the values of the weights:

<img src="https://latex.codecogs.com/svg.image?\begin{matrix}w_{0}=w_{0}&plus;x_{0}y=1&plus;1*(-1)=0\\w_{1}=w_{1}&plus;x_{1}^{2}y=1&plus;1*(-1)=0\\w_{2}=w_{2}&plus;x_{2}^{2}y=-1&plus;1*(-1)=-2\\...\\w_{9}=w_{9}&plus;x_{9}^{2}y=1&plus;1*(-1)=0.\end{matrix}" />

The vector of the weights is obtained ![equation](https://latex.codecogs.com/svg.image?w=(0,0,-2,0,0,2,0,-2,0,0).)

#### Step 4. Checking the quality of training
Checking the condition for stopping learning for the obtained values of the weights:

<img src="https://latex.codecogs.com/svg.image?\begin{matrix}y^{k}=\left\{\begin{matrix}1,if\:S^{k}>0,\\-1,if\:S^{k}\end{matrix}\right.\\S^{k}=\sum_{i=1}^{n}x_{i}^{k}w_{i}&plus;w_{0}\end{matrix}" />

##### First Image
![equation](https://latex.codecogs.com/svg.image?S^{1}=\sum_{i=1}^{9}x_{i}^{1}w_{i}&plus;w_{0}=1*0&plus;(-1)*(-2)&plus;1*0&plus;1*0&plus;1*2&plus;1*0&plus;(-1)*(-2)&plus;(-1)*0&plus;1*0&plus;0=6,)

The output of the neuron is ![equation](https://latex.codecogs.com/svg.image?y^{1}=1), since ![equation](https://latex.codecogs.com/svg.image?S^{1}>0.)

##### Second image
![equation](https://latex.codecogs.com/svg.image?S^{2}=\sum_{i=1}^{9}x_{i}^{2}w_{i}&plus;w_{0}=1*0&plus;1*(-2)&plus;1*0&plus;1*0&plus;(-1)*2&plus;1*0&plus;1*(-2)&plus;(-1)*0&plus;1*0&plus;0=-6,)

The output of the neuron is ![equation](https://latex.codecogs.com/svg.image?y^{2}=-1), since ![equation](https://latex.codecogs.com/svg.image?S^{2}<0.)

Vector ![equation](https://latex.codecogs.com/svg.image?(y^{1},y^{2})=(1,-1)) is equal to the target vector ![equation](https://latex.codecogs.com/svg.image?(Y^{1},Y^{2}),) the goal is achieved and the neuron correctly recognizes the given images.

If a match is not achieved, repeat steps 2-3 many times for each image until the required value of the output signals of the neuron is obtained ![equation](https://latex.codecogs.com/svg.image?(y^{1},y^{2})=(Y^{1},Y^{2}).)
