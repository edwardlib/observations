from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import shutil
import sys
import tempfile

from observations.r.goldenrod import goldenrod


def test_goldenrod():
  """Test module goldenrod.py by downloading
   goldenrod.csv and testing shape of
   extracted data has 1055 rows and 9 columns
  """
  test_path = tempfile.mkdtemp()
  x_train, metadata = goldenrod(test_path)
  try:
    assert x_train.shape == (1055, 9)
  except:
    shutil.rmtree(test_path)
    raise()
