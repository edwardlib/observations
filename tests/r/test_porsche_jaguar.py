from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import shutil
import sys
import tempfile

from observations.r.porsche_jaguar import porsche_jaguar


def test_porsche_jaguar():
  """Test module porsche_jaguar.py by downloading
   porsche_jaguar.csv and testing shape of
   extracted data has 60 rows and 5 columns
  """
  test_path = tempfile.mkdtemp()
  x_train, metadata = porsche_jaguar(test_path)
  try:
    assert x_train.shape == (60, 5)
  except:
    shutil.rmtree(test_path)
    raise()
