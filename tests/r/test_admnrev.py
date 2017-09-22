from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import shutil
import sys
import tempfile

from observations.r.admnrev import admnrev


def test_admnrev():
  """Test module admnrev.py by downloading
   admnrev.csv and testing shape of
   extracted data has 153 rows and 5 columns
  """
  test_path = tempfile.mkdtemp()
  x_train, metadata = admnrev(test_path)
  try:
    assert x_train.shape == (153, 5)
  except:
    shutil.rmtree(test_path)
    raise()
