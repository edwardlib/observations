from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import shutil
import sys
import tempfile

from observations.r.ddt_kale import ddt_kale


def test_ddt_kale():
  """Test module ddt_kale.py by downloading
   ddt_kale.csv and testing shape of
   extracted data has 15 rows and 1 columns
  """
  test_path = tempfile.mkdtemp()
  x_train, metadata = ddt_kale(test_path)
  try:
    assert x_train.shape == (15, 1)
  except:
    shutil.rmtree(test_path)
    raise()
