from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import shutil
import sys
import tempfile

from observations.r.males import males


def test_males():
  """Test module males.py by downloading
   males.csv and testing shape of
   extracted data has 4360 rows and 12 columns
  """
  test_path = tempfile.mkdtemp()
  x_train, metadata = males(test_path)
  try:
    assert x_train.shape == (4360, 12)
  except:
    shutil.rmtree(test_path)
    raise()
