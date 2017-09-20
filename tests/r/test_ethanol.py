from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import shutil
import sys
import tempfile

from observations.r.ethanol import ethanol


def test_ethanol():
  """Test module ethanol.py by downloading
   ethanol.csv and testing shape of
   extracted data has 88 rows and 3 columns
  """
  test_path = tempfile.mkdtemp()
  x_train, metadata = ethanol(test_path)
  try:
    assert x_train.shape == (88, 3)
  except:
    shutil.rmtree(test_path)
    raise()
