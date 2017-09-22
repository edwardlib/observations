from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import shutil
import sys
import tempfile

from observations.r.engin import engin


def test_engin():
  """Test module engin.py by downloading
   engin.csv and testing shape of
   extracted data has 403 rows and 17 columns
  """
  test_path = tempfile.mkdtemp()
  x_train, metadata = engin(test_path)
  try:
    assert x_train.shape == (403, 17)
  except:
    shutil.rmtree(test_path)
    raise()
