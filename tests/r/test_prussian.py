from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import shutil
import sys
import tempfile

from observations.r.prussian import prussian


def test_prussian():
  """Test module prussian.py by downloading
   prussian.csv and testing shape of
   extracted data has 280 rows and 3 columns
  """
  test_path = tempfile.mkdtemp()
  x_train, metadata = prussian(test_path)
  try:
    assert x_train.shape == (280, 3)
  except:
    shutil.rmtree(test_path)
    raise()
