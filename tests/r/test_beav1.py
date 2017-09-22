from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import shutil
import sys
import tempfile

from observations.r.beav1 import beav1


def test_beav1():
  """Test module beav1.py by downloading
   beav1.csv and testing shape of
   extracted data has 114 rows and 4 columns
  """
  test_path = tempfile.mkdtemp()
  x_train, metadata = beav1(test_path)
  try:
    assert x_train.shape == (114, 4)
  except:
    shutil.rmtree(test_path)
    raise()
