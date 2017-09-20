from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import shutil
import sys
import tempfile

from observations.r.inven import inven


def test_inven():
  """Test module inven.py by downloading
   inven.csv and testing shape of
   extracted data has 37 rows and 13 columns
  """
  test_path = tempfile.mkdtemp()
  x_train, metadata = inven(test_path)
  try:
    assert x_train.shape == (37, 13)
  except:
    shutil.rmtree(test_path)
    raise()
