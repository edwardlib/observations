from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import shutil
import sys
import tempfile

from observations.r.openness import openness


def test_openness():
  """Test module openness.py by downloading
   openness.csv and testing shape of
   extracted data has 114 rows and 12 columns
  """
  test_path = tempfile.mkdtemp()
  x_train, metadata = openness(test_path)
  try:
    assert x_train.shape == (114, 12)
  except:
    shutil.rmtree(test_path)
    raise()
