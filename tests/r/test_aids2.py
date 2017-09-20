from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import shutil
import sys
import tempfile

from observations.r.aids2 import aids2


def test_aids2():
  """Test module aids2.py by downloading
   aids2.csv and testing shape of
   extracted data has 2843 rows and 7 columns
  """
  test_path = tempfile.mkdtemp()
  x_train, metadata = aids2(test_path)
  try:
    assert x_train.shape == (2843, 7)
  except:
    shutil.rmtree(test_path)
    raise()
