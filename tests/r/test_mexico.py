from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import shutil
import sys
import tempfile

from observations.r.mexico import mexico


def test_mexico():
  """Test module mexico.py by downloading
   mexico.csv and testing shape of
   extracted data has 1359 rows and 33 columns
  """
  test_path = tempfile.mkdtemp()
  x_train, metadata = mexico(test_path)
  try:
    assert x_train.shape == (1359, 33)
  except:
    shutil.rmtree(test_path)
    raise()
