from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import shutil
import sys
import tempfile

from observations.r.mroz import mroz


def test_mroz():
  """Test module mroz.py by downloading
   mroz.csv and testing shape of
   extracted data has 753 rows and 18 columns
  """
  test_path = tempfile.mkdtemp()
  x_train, metadata = mroz(test_path)
  try:
    assert x_train.shape == (753, 18)
  except:
    shutil.rmtree(test_path)
    raise()
