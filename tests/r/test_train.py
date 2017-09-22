from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import shutil
import sys
import tempfile

from observations.r.train import train


def test_train():
  """Test module train.py by downloading
   train.csv and testing shape of
   extracted data has 2929 rows and 11 columns
  """
  test_path = tempfile.mkdtemp()
  x_train, metadata = train(test_path)
  try:
    assert x_train.shape == (2929, 11)
  except:
    shutil.rmtree(test_path)
    raise()
