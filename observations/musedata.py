from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import os
import six.moves.cPickle as pickle

from observations.util import maybe_download_and_extract


def musedata(path):
  """Load the MuseData library of music scores.
  It includes both orchestral and piano classical music. Data is
  loaded in the piano-roll representation [@boulanger2012modeling],
  i.e., a binary matrix specifying which notes occur at each time
  step.

  Args:
    path: str.
      Path to directory which either stores file or otherwise file will
      be downloaded and extracted there. Filename is
      `MuseData.pickle`.

  Returns:
    list of `x_train, x_test, x_valid`, where each is a list of
    sequences. Each sequence is itself a list of time steps, and each
    time step is a list of the non-zero elements in the piano-roll at
    this instant (in MIDI note numbers, between 21 and 108 inclusive).
  """
  path = os.path.expanduser(path)
  filename = 'MuseData.pickle'
  url = 'http://www-etud.iro.umontreal.ca/~boulanni/MuseData.pickle'
  if not os.path.exists(os.path.join(path, filename)):
    maybe_download_and_extract(path, url)
  with open(os.path.join(path, filename), 'rb') as f:
    data = pickle.load(f)
  return data['train'], data['test'], data['valid']
