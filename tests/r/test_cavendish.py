from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import shutil
import sys
import tempfile

from observations.r.cavendish import cavendish


def test_cavendish():
  """Test module cavendish.py by downloading
   cavendish.csv and testing shape of
   extracted data has 29 rows and 3 columns
  """
  test_path = tempfile.mkdtemp()
  x_train, metadata = cavendish(test_path)
  try:
    assert x_train.shape == (29, 3)
  except:
    shutil.rmtree(test_path)
    raise()
