# Observations

Observations provides a minimalistic collection of Python functions
for loading standard data sets in machine learning. It automates the
process from downloading, extracting, loading, and preprocessing data.
Observations helps keep the workflow reproducible and follow sensible
standards.

It can be used in two ways.

## 1. As a package

Install it.
```bash
pip install observations
```
Import it.
```python
from observations import svhn

(x_train, y_train), (x_test, y_test) = svhn("~/data")
```
All functions take as input a filepath and optional preprocessing
arguments. They return a tuple in the form of training data, test
data, and validation data (if available). Each element in the tuple
is typically a NumPy array, a tuple of NumPy arrays (e.g., features
and labels), or a string (text). See the docstrings for details.

## 2. As source code

Copy and paste functions inside the codebase relevant for your
experiments.

```python
def enwik8(path):
  ...

x_train, x_test, x_valid = enwik8("~/data")
```

Each function has minimal dependencies. For example,
[`enwik8.py`](observations/enwik8.py) only depends on core libraries and
the external function ``maybe_download_and_extract`` in
[`util.py`](observations/util.py). The functions are designed to be easy to
read and hack at.

# FAQ

### Which approach should I take?

It depends on your use case.

1. As a package, dozens of data sets are at your disposal. The package establishes sensible standards for conveniently loading in data and thus quickly experimenting with them.
2. As source code, you have complete flexibility—from the initial download all the way to preprocessing the data as NumPy arrays.

### How do I use minibatches of data?

The data loading functions return the full data. It's up to your needs
to generate batches.

One helpful utility is
```python
def generator(array, batch_size):
  """Generate batch with respect to array's first axis."""
  start = 0  # pointer to where we are in iteration
  while True:
    stop = start + batch_size
    diff = stop - array.shape[0]
    if diff <= 0:
      batch = array[start:stop]
      start += batch_size
    else:
      batch = np.concatenate((array[start:], array[:diff]))
      start = diff
    yield batch
```
To use it, simply write
```python
from observations import cifar10
(x_train, y_train), (x_test, y_test) = cifar10("~/data")
x_train_data = generator(x_train, 256)

for batch in x_train_data:
  ...  # operate on batch

batch = next(x_train_data)  # alternatively, increment the iterator
```
There's also an extended version. It takes a list of arrays as input
and yields a list of batches.
```python
def generator(arrays, batch_size):
  """Generate batches, one with respect to each array's first axis."""
  starts = [0] * len(arrays)  # pointers to where we are in iteration
  while True:
    batches = []
    for i, array in enumerate(arrays):
      start = starts[i]
      stop = start + batch_size
      diff = stop - array.shape[0]
      if diff <= 0:
        batch = array[start:stop]
        starts[i] += batch_size
      else:
        batch = np.concatenate((array[start:], array[:diff]))
        starts[i] = diff
      batches.append(batch)
    yield batches
```
To use it, simply write
```python
from observations import cifar10
(x_train, y_train), (x_test, y_test) = cifar10("~/data")
train_data = generator([x_train, y_train], 256)

for x_batch, y_batch in train_data:
  ...  # operate on batch

x_batch, y_batch = next(train_data)  # alternatively, increment the iterator
```

# Contributing

We'd like your help! Any pull requests which help maintain the
existing functions and/or add new ones are appreciated.
We follow [Edward's standards for style and documentation.](http://edwardlib.org/contributing)

Each function takes as input a filepath and optional preprocessing
arguments. All necessary packages that aren't from the Python Standard
Library, NumPy, or six are imported inside the function's body.
The functions proceed as follows:

1. Check if the extracted file(s) exist in the filepath. If it does,
   skip to step 4.
2. Check if the compressed file(s) exist in the filepath. If it doesn't,
   download it.
3. Extract the compressed file(s).
4. Load the data into memory.
   + For data sets larger than 1 GB, the function will terminate with
     a message advising to load the files as batches.
5. Preprocess the data.
6. Return a tuple in the form of training data, test data, and
   validation data (if available). Each element in the tuple
    is typically a NumPy array, a tuple of NumPy arrays (e.g., features
    and labels), or a string (text).
