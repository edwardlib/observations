from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import shutil
import sys
import tempfile

from observations.r.fruitohms import fruitohms


def test_fruitohms():
  """Test module fruitohms.py by downloading
   fruitohms.csv and testing shape of
   extracted data has 128 rows and 2 columns
  """
  test_path = tempfile.mkdtemp()
  x_train, metadata = fruitohms(test_path)
  try:
    assert x_train.shape == (128, 2)
  except:
    shutil.rmtree(test_path)
    raise()
