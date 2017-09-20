from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import shutil
import sys
import tempfile

from observations.r.beav2 import beav2


def test_beav2():
  """Test module beav2.py by downloading
   beav2.csv and testing shape of
   extracted data has 100 rows and 4 columns
  """
  test_path = tempfile.mkdtemp()
  x_train, metadata = beav2(test_path)
  try:
    assert x_train.shape == (100, 4)
  except:
    shutil.rmtree(test_path)
    raise()
