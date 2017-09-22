from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import shutil
import sys
import tempfile

from observations.r.gorsuch import gorsuch


def test_gorsuch():
  """Test module gorsuch.py by downloading
   gorsuch.csv and testing shape of
   extracted data has 10 rows and 10 columns
  """
  test_path = tempfile.mkdtemp()
  x_train, metadata = gorsuch(test_path)
  try:
    assert x_train.shape == (10, 10)
  except:
    shutil.rmtree(test_path)
    raise()
