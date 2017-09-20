from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import shutil
import sys
import tempfile

from observations.r.acme import acme


def test_acme():
  """Test module acme.py by downloading
   acme.csv and testing shape of
   extracted data has 60 rows and 3 columns
  """
  test_path = tempfile.mkdtemp()
  x_train, metadata = acme(test_path)
  try:
    assert x_train.shape == (60, 3)
  except:
    shutil.rmtree(test_path)
    raise()
