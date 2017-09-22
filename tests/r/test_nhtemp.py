from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import shutil
import sys
import tempfile

from observations.r.nhtemp import nhtemp


def test_nhtemp():
  """Test module nhtemp.py by downloading
   nhtemp.csv and testing shape of
   extracted data has 60 rows and 2 columns
  """
  test_path = tempfile.mkdtemp()
  x_train, metadata = nhtemp(test_path)
  try:
    assert x_train.shape == (60, 2)
  except:
    shutil.rmtree(test_path)
    raise()
