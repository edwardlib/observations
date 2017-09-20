from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import shutil
import sys
import tempfile

from observations.r.happiness import happiness


def test_happiness():
  """Test module happiness.py by downloading
   happiness.csv and testing shape of
   extracted data has 17137 rows and 33 columns
  """
  test_path = tempfile.mkdtemp()
  x_train, metadata = happiness(test_path)
  try:
    assert x_train.shape == (17137, 33)
  except:
    shutil.rmtree(test_path)
    raise()
