from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import shutil
import sys
import tempfile

from observations.r.respdis import respdis


def test_respdis():
  """Test module respdis.py by downloading
   respdis.csv and testing shape of
   extracted data has 111 rows and 5 columns
  """
  test_path = tempfile.mkdtemp()
  x_train, metadata = respdis(test_path)
  try:
    assert x_train.shape == (111, 5)
  except:
    shutil.rmtree(test_path)
    raise()
