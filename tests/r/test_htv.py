from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import shutil
import sys
import tempfile

from observations.r.htv import htv


def test_htv():
  """Test module htv.py by downloading
   htv.csv and testing shape of
   extracted data has 1230 rows and 23 columns
  """
  test_path = tempfile.mkdtemp()
  x_train, metadata = htv(test_path)
  try:
    assert x_train.shape == (1230, 23)
  except:
    shutil.rmtree(test_path)
    raise()
