from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import shutil
import sys
import tempfile

from observations.r.fgl import fgl


def test_fgl():
  """Test module fgl.py by downloading
   fgl.csv and testing shape of
   extracted data has 214 rows and 10 columns
  """
  test_path = tempfile.mkdtemp()
  x_train, metadata = fgl(test_path)
  try:
    assert x_train.shape == (214, 10)
  except:
    shutil.rmtree(test_path)
    raise()
