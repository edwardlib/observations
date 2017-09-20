from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import shutil
import sys
import tempfile

from observations.r.mcycle import mcycle


def test_mcycle():
  """Test module mcycle.py by downloading
   mcycle.csv and testing shape of
   extracted data has 133 rows and 2 columns
  """
  test_path = tempfile.mkdtemp()
  x_train, metadata = mcycle(test_path)
  try:
    assert x_train.shape == (133, 2)
  except:
    shutil.rmtree(test_path)
    raise()
