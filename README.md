# Handwritten Digit Recognition (An Implementation)

Website implementation of Handwritten Digit Recognition.

The model is trained using [MNIST Dataset](http://yann.lecun.com/exdb/mnist/) with [Artificial Neural Network](https://en.wikipedia.org/wiki/Artificial_neural_network) architecture.

## Getting Started

These instructions will get you a copy of project and run it on your local machine.

### Prerequisites

1. Install [python 3.8.0](https://www.python.org/downloads/release/python-380/) in your local machine.

2. Install **required packages** using **pip**.
```
pip install pandas==1.2.3
pip install torch==1.8.0
pip install flask==1.1.2
```

3. **Clone** this github repository.
```
git clone https://github.com/dimbay67/mnist-digit-ann
```

### Running

1. Open your **command prompt** and fire up `app.py` using **python**.
```
python app.py
```

2. Go to [this link](http://127.0.0.1:5000) using your **browser**.

## Model Architecture and Parameters

- The model architecture used in this project are **784**, **5**, and **10** for **input**, **hidden**, and **output neurons** respectively.
- **Activation function** for **hidden layer** and **output layer** are [sigmoid](https://en.wikipedia.org/wiki/Sigmoid_function) and [softmax](https://en.wikipedia.org/wiki/Softmax_function) respectively.
- **Optimizer** used in training phase is [adam](https://arxiv.org/abs/1412.6980) with **0.01 learning rate**.
- **Loss function** used in training phase is [cross entropy loss](https://pytorch.org/docs/stable/generated/torch.nn.CrossEntropyLoss.html).
- Model is trained with **batch size = 6000** for **200 epochs**.
- **Preprocessing** done only by [min-max normalization](https://en.wikipedia.org/wiki/Feature_scaling).

## Folder Structure

```
+ static
  + css
      style.css
  + js
      script.js
+ templates
    index.html
+ training
  + dataset
      mnist_train.csv
  + utils
      model.py
    mnist-digit-ann.ipynb
    model.py
  app.py
```

- The **website files** consists of ```index.html```, ```style.css```, and ```script.js```.
- The **dataset** used is in **csv format** since it's easier. You can download it [here](https://pjreddie.com/projects/mnist-in-csv/).
- The **model architecture** is in ```model.py```.
- To **train the model** from scratch run ```mnist-digit-ann.ipynb```.
- The **trained model** is saved as ```model.pt```.
- The **server handler** is in ```app.py```.

## Built With

* [FabricJS](http://fabricjs.com/docs/) - Library used for canvas.
* [PyTorch](https://pytorch.org/docs/stable/index.html) - Library used for training artificial neural network model.
* [Flask](https://flask.palletsprojects.com/en/1.1.x/) - Framework used for model deployment.

## Authors

**Dimas Bayu Nugraha** - [Dimbay](https://github.com/dimbay67)

## License

This project is licensed under the MIT License - see the [LICENSE.md](https://github.com/dimbay67/mnist-digit-ann/blob/main/LICENSE) file for details

## Acknowledgments

* [Abhinav Sagar](https://github.com/abhinavsagar/machine-learning-deployment)
* [Ishaan](https://www.geeksforgeeks.org/how-to-send-a-json-object-to-a-server-using-javascript/)