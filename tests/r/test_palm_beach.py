from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import shutil
import sys
import tempfile

from observations.r.palm_beach import palm_beach


def test_palm_beach():
  """Test module palm_beach.py by downloading
   palm_beach.csv and testing shape of
   extracted data has 67 rows and 3 columns
  """
  test_path = tempfile.mkdtemp()
  x_train, metadata = palm_beach(test_path)
  try:
    assert x_train.shape == (67, 3)
  except:
    shutil.rmtree(test_path)
    raise()
