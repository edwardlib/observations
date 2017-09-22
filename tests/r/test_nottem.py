from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import shutil
import sys
import tempfile

from observations.r.nottem import nottem


def test_nottem():
  """Test module nottem.py by downloading
   nottem.csv and testing shape of
   extracted data has 240 rows and 2 columns
  """
  test_path = tempfile.mkdtemp()
  x_train, metadata = nottem(test_path)
  try:
    assert x_train.shape == (240, 2)
  except:
    shutil.rmtree(test_path)
    raise()
