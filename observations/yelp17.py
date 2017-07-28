from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import json
import numpy as np
import os


def yelp17(path, categories=None):
  """Load Yelp reviews from the Yelp Dataset Challenge in 2017. It
  contains ~4.1 million reviews, ~1 million users, and ~144,000
  businesses from cities in the UK, Germany, Canada, and the US. We
  only load the review's text and its rating.

  Args:
    path: str.
      Path to directory which stores file. Filename is
      `yelp_dataset_challenge_round9/`.
    categories: str or list of str, optional.
      Business categories to include reviews from. It is case-sensitive,
      e.g., "Restaurants". Default is to include all categories.

  Returns:
    Tuple of list x_train and np.ndarray y_train. Each pair of
    elements corresponds to the review text and its rating.
  """
  if isinstance(categories, str):
    categories = [categories]
  path = os.path.expanduser(path)
  path = os.path.join(path, 'yelp_dataset_challenge_round9')
  if not os.path.exists(path):
    url = 'https://www.yelp.com/dataset_challenge'
    raise IOError("Files not found. Downloading requires explicit permission. "
                  "See {}".format(e, url))

  if categories is not None:
    business = {}
    with open(os.path.join(path, 'yelp_academic_dataset_business.json')) as f:
      for line in f:
        data = json.loads(line)
        business[data['business_id']] = data['categories']

  x_train = []
  y_train = []
  with open(os.path.join(path, 'yelp_academic_dataset_review.json')) as f:
    for line in f:
      data = json.loads(line)
      if categories is None:
        x_train.append(data['text'])
        y_train.append(data['stars'])
      else:
        business_categories = business.get(data['business_id'])
        if business_categories and \
                any(cat in categories for cat in business_categories):
          x_train.append(data['text'])
          y_train.append(data['stars'])

  y_train = np.array(y_train, dtype=np.int)
  return x_train, y_train
