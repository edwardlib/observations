from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import os
import six.moves.cPickle as pickle

from observations.util import maybe_download_and_extract


def jsb_chorales(path):
  """Load the corpus of 382 four-part harmonized chorales from J.S.
  Bach. There are 202 chorales in major keys of which 121 were used
  for training and 81 used for testing; and 180 chorales in minor keys
  split as 108 and 72 respectively [@allan2005harmonising]. Chorales are
  loaded in the piano-roll representation [@boulanger2012modeling],
  i.e., a binary matrix specifying which notes occur at each time
  step.

  Args:
    path: str.
      Path to directory which either stores file or otherwise file will
      be downloaded and extracted there. Filename is
      `JSB%20Chorales.pickle`.

  Returns:
    list of `x_train, x_test, x_valid`, where each is a list of tuples
    representing the notes played for each timestep. (It is the sparse
    representation of the binary matrix.)
  """
  path = os.path.expanduser(path)
  filename = 'JSB%20Chorales.pickle'
  url = 'http://www-etud.iro.umontreal.ca/~boulanni/JSB%20Chorales.pickle'
  if not os.path.exists(os.path.join(path, filename)):
    maybe_download_and_extract(path, url)
  with open(os.path.join(path, filename), "rb") as f:
    data = pickle.load(f)
  return data['train'], data['test'], data['valid']
