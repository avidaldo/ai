# Neural Networks from the Outside

A **neural network** is a model built from many simple units, loosely inspired by the neurons of a brain and connected in layers. It is the model behind **deep learning**, and so behind most of the image, speech and language systems of the last fifteen years, [language models](language_models.md) included. How a network learns, step by step, and how to build and train one, are explained in the topic on neural networks *(coming)*.

## Historical Milestones

### Early Foundations (1943–1998)

- 1943: McCulloch and Pitts propose the first mathematical model of a neuron.
- 1958: Frank Rosenblatt develops the **perceptron**, a model neuron that learns its weights from examples.
- 1969: Minsky and Papert publish "Perceptrons," demonstrating the limitations of the simple perceptron, which contributed to a long decline of research on neural networks.
- 1980: Kunihiko Fukushima's **Neocognitron**, the first convolutional architecture, inspired by the visual cortex.
- 1986: Rumelhart, Hinton and Williams popularise **backpropagation**, which **allows training multilayer neural networks**. The method itself had earlier roots: Seppo Linnainmaa (1970) and Paul Werbos (1974).
- 1989: LeCun et al. train a convolutional network with backpropagation to read handwritten zip codes.
- 1997: Hochreiter & Schmidhuber introduce **LSTMs** (Long Short-Term Memory), fundamental for processing sequences and time series.
- 1998: LeCun et al. publish **LeNet-5** and the **MNIST** dataset of handwritten digits.

### The AI Boom (2012–present)

Its causes, more data, GPUs and better ways to train deep networks, are in [what is artificial intelligence?](what_is_ai.md#a-brief-history-of-ai). The main milestones:

- 2012: **AlexNet** (Krizhevsky, Sutskever, and Hinton) reduces the top-5 error on **ImageNet** to 15.3% (from 26%), demonstrating the power of CNNs and marking the beginning of the boom.
- 2014: Facebook's **DeepFace** achieves near-human accuracy (97.35%) in facial recognition.
- 2014: Ian Goodfellow introduces **GANs** (Generative Adversarial Networks), revolutionising content generation.
- 2015: **ResNet** from Microsoft Research introduces residual connections, allowing the training of networks with over 100 layers.
- 2016: DeepMind's **AlphaGo** defeats world champion Lee Sedol using deep neural networks trained with supervised and reinforcement learning with advanced Monte Carlo tree search techniques. ([Documentary](https://www.youtube.com/watch?v=WXuK6gekU1Y)).
- 2017: The **Transformer** architecture appears with the publication of "**Attention is all you need**" by Google Brain, transforming language processing.
- 2018: Google's **BERT** sets new records in natural language understanding.
- 2020: OpenAI's **GPT-3** shows that a large enough language model can do a new task from a few examples written in its prompt, without further training.
- 2021–2022: **Diffusion models** take over image generation: OpenAI's GLIDE (December 2021), DALL-E 2 and Stable Diffusion (2022). The first DALL-E (January 2021) was not a diffusion model, but a transformer that generated images token by token.
- 2022: OpenAI's **ChatGPT** (GPT-3.5) popularises conversational assistants.
- 2023: OpenAI's **GPT-4** (March), announced as a **multimodal** model that accepts images as well as text.
- 2024: OpenAI's **GPT-4o** (May) handles text, images and audio in one model, and **o1** (September) is the first of the *reasoning* models, which generate a long chain of reasoning before answering.
- 2025: **DeepSeek-R1**, an *open-weights* reasoning model, reports results comparable to o1 at a much lower cost.

## What a Network Is

> [What is a Neural Network? Part 1: The Neuron | DotCSV](https://www.youtube.com/watch?v=MRIv2IwFTPg&list=PL-Ogd76BhmcC_E2RjgIIJZd1DQdYHcVf0&index=7) (in Spanish)

> [3Blue1Brown - But what is a neural network?](https://www.youtube.com/watch?v=aircAruvnKk&list=PLZHQObOWTQDNU6R1_67000Dx_ZCJB-3pi)

![A perceptron: inputs multiplied by weights, summed with a bias, passed through a non-linear activation to give the output](./img/perceptron.png)

*Slide from MIT 6.S191, [Introduction to Deep Learning](https://introtodeeplearning.com/), by Alexander Amini.*

Each unit, an **artificial neuron**, multiplies each of its inputs by a **weight**, adds the results together with a **bias**, and passes the sum through an **activation function**. The weights and biases are the network's [parameters](machine_learning_paradigms.md): the numbers that training adjusts. The first such unit, the perceptron, could only separate two classes with a straight line (a plane, or a hyperplane, with more inputs). So it fails at a problem as small as XOR: answering 1 when exactly one of two inputs is 1.

A **multilayer network** stacks units in layers: an input layer that receives the data, one or more **hidden layers**, and an output layer that gives the prediction, a class or a number. Each hidden layer combines the patterns found by the layer before into more complex ones, and that is what lets a network learn curved boundaries and complex relations. It only works because the activation functions are not linear: without them, any number of layers would add up to a single linear model.

![MLP](./img/mlp.gif)

## How It Learns

> [3Blue1Brown - Gradient descent, how neural networks learn](https://www.youtube.com/watch?v=IHZwWFHWa-w&list=PLZHQObOWTQDNU6R1_67000Dx_ZCJB-3pi&index=2)

> [What is Gradient Descent? Artificial Intelligence Algorithm | DotCSV](https://www.youtube.com/watch?v=A6FiCDoz8_4) (in Spanish)

Training starts from random weights. The network predicts for a small batch of training examples, a **loss function** measures how far the predictions are from the targets, and every weight is moved a small step in the direction that reduces the loss: that is **gradient descent**. **Backpropagation** is the algorithm that computes that direction for every weight at once, working back from the output layer to the input. Repeated over many batches, and many passes over the data, these small steps fit the network to its examples.

Gradient descent is explained step by step in [supervised learning](../../supervised-learning/ml-fundamentals/gradient_descent.ipynb), because simpler models are trained with it too, and backpropagation in the topic on neural networks *(coming)*.

## Deep Learning

*Deep learning* refers to neural networks with many hidden layers (hence "deep"). Their layers learn representations of the data at several levels of abstraction: in an image, edges first, then textures and shapes, then parts of objects.

![Deep Learning](./img/deep_learning.jpg)

What depth buys:

1. **Features learned from raw data.** In other machine learning, people design the features by hand (*feature engineering*); a deep network learns them from the pixels, the sound or the text.
2. **Complex relations in unstructured data,** such as images, text and sound, where hand-made features fall short.
3. **Transfer learning.** What a network learned on one task can be reused for another, so a powerful model can be built from little data.

It is not always worth it. On a table of features, such as the houses of [valuing a home](machine_learning_paradigms.md#regression), gradient-boosted trees are a strong default: often as accurate as a network, and faster to train and to tune ([Grinsztajn et al., 2022](https://arxiv.org/abs/2207.08815)). Networks make the difference where the features have to be learned.

## Families of Networks

| Family | The data it fits | What it does |
| --- | --- | --- |
| **Multilayer networks** (MLP) | Tables of features; also a building block inside every other family | The layers described above |
| **Convolutional networks** (CNN) | Images, and other data on a grid | Detect local patterns (edges, textures, shapes) anywhere in the image, and combine them |
| **Recurrent networks** (RNN, LSTM, GRU) | Sequences: time series, text | Read the sequence in order, with a memory of what came before; for text, largely replaced by transformers |
| **Transformers** | Text, and now images and audio | *Attention* weighs every part of the input against every other; almost all of today's [language models](language_models.md) are transformers |
| **Autoencoders** | Any | Compress the data into a few numbers and rebuild it; for dimensionality reduction and anomaly detection |
| **Generative image models** (GANs, diffusion models) | Images, audio | Generate new data like the training data. GANs pit a generator against a discriminator; diffusion models, which learn to remove noise step by step, power most of today's image generators |

Multilayer and convolutional networks, and reusing a pretrained network, are the topic on neural networks *(coming)*; transformers are the topic on how language models work *(coming)*.
