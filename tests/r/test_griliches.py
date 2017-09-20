from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import shutil
import sys
import tempfile

from observations.r.griliches import griliches


def test_griliches():
  """Test module griliches.py by downloading
   griliches.csv and testing shape of
   extracted data has 758 rows and 20 columns
  """
  test_path = tempfile.mkdtemp()
  x_train, metadata = griliches(test_path)
  try:
    assert x_train.shape == (758, 20)
  except:
    shutil.rmtree(test_path)
    raise()
