from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import shutil
import sys
import tempfile

from observations.r.agefat import agefat


def test_agefat():
  """Test module agefat.py by downloading
   agefat.csv and testing shape of
   extracted data has 25 rows and 3 columns
  """
  test_path = tempfile.mkdtemp()
  x_train, metadata = agefat(test_path)
  try:
    assert x_train.shape == (25, 3)
  except:
    shutil.rmtree(test_path)
    raise()
