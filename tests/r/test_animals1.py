from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import shutil
import sys
import tempfile

from observations.r.animals1 import animals1


def test_animals1():
  """Test module animals1.py by downloading
   animals1.csv and testing shape of
   extracted data has 28 rows and 2 columns
  """
  test_path = tempfile.mkdtemp()
  x_train, metadata = animals1(test_path)
  try:
    assert x_train.shape == (28, 2)
  except:
    shutil.rmtree(test_path)
    raise()
