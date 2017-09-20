from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import shutil
import sys
import tempfile

from observations.r.austres import austres


def test_austres():
  """Test module austres.py by downloading
   austres.csv and testing shape of
   extracted data has 89 rows and 2 columns
  """
  test_path = tempfile.mkdtemp()
  x_train, metadata = austres(test_path)
  try:
    assert x_train.shape == (89, 2)
  except:
    shutil.rmtree(test_path)
    raise()
