from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import shutil
import sys
import tempfile

from observations.r.swahili import swahili


def test_swahili():
  """Test module swahili.py by downloading
   swahili.csv and testing shape of
   extracted data has 480 rows and 4 columns
  """
  test_path = tempfile.mkdtemp()
  x_train, metadata = swahili(test_path)
  try:
    assert x_train.shape == (480, 4)
  except:
    shutil.rmtree(test_path)
    raise()
