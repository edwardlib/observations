from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import shutil
import sys
import tempfile

from observations.r.jtrain import jtrain


def test_jtrain():
  """Test module jtrain.py by downloading
   jtrain.csv and testing shape of
   extracted data has 471 rows and 30 columns
  """
  test_path = tempfile.mkdtemp()
  x_train, metadata = jtrain(test_path)
  try:
    assert x_train.shape == (471, 30)
  except:
    shutil.rmtree(test_path)
    raise()
