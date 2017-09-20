from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import shutil
import sys
import tempfile

from observations.r.uk_gas import uk_gas


def test_uk_gas():
  """Test module uk_gas.py by downloading
   uk_gas.csv and testing shape of
   extracted data has 108 rows and 2 columns
  """
  test_path = tempfile.mkdtemp()
  x_train, metadata = uk_gas(test_path)
  try:
    assert x_train.shape == (108, 2)
  except:
    shutil.rmtree(test_path)
    raise()
