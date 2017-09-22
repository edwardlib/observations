from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import shutil
import sys
import tempfile

from observations.r.bird_nest import bird_nest


def test_bird_nest():
  """Test module bird_nest.py by downloading
   bird_nest.csv and testing shape of
   extracted data has 84 rows and 12 columns
  """
  test_path = tempfile.mkdtemp()
  x_train, metadata = bird_nest(test_path)
  try:
    assert x_train.shape == (84, 12)
  except:
    shutil.rmtree(test_path)
    raise()
