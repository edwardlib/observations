from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import shutil
import sys
import tempfile

from observations.r.michelson1 import michelson1


def test_michelson1():
  """Test module michelson1.py by downloading
   michelson1.csv and testing shape of
   extracted data has 100 rows and 3 columns
  """
  test_path = tempfile.mkdtemp()
  x_train, metadata = michelson1(test_path)
  try:
    assert x_train.shape == (100, 3)
  except:
    shutil.rmtree(test_path)
    raise()
