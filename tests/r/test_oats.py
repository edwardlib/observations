from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import shutil
import sys
import tempfile

from observations.r.oats import oats


def test_oats():
  """Test module oats.py by downloading
   oats.csv and testing shape of
   extracted data has 72 rows and 4 columns
  """
  test_path = tempfile.mkdtemp()
  x_train, metadata = oats(test_path)
  try:
    assert x_train.shape == (72, 4)
  except:
    shutil.rmtree(test_path)
    raise()
