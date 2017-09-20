from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import shutil
import sys
import tempfile

from observations.r.auto import auto


def test_auto():
  """Test module auto.py by downloading
   auto.csv and testing shape of
   extracted data has 392 rows and 9 columns
  """
  test_path = tempfile.mkdtemp()
  x_train, metadata = auto(test_path)
  try:
    assert x_train.shape == (392, 9)
  except:
    shutil.rmtree(test_path)
    raise()
