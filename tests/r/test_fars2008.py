from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import shutil
import sys
import tempfile

from observations.r.fars2008 import fars2008


def test_fars2008():
  """Test module fars2008.py by downloading
   fars2008.csv and testing shape of
   extracted data has 64881 rows and 24 columns
  """
  test_path = tempfile.mkdtemp()
  x_train, metadata = fars2008(test_path)
  try:
    assert x_train.shape == (64881, 24)
  except:
    shutil.rmtree(test_path)
    raise()
