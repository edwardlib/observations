from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import shutil
import sys
import tempfile

from observations.r.waders import waders


def test_waders():
  """Test module waders.py by downloading
   waders.csv and testing shape of
   extracted data has 15 rows and 19 columns
  """
  test_path = tempfile.mkdtemp()
  x_train, metadata = waders(test_path)
  try:
    assert x_train.shape == (15, 19)
  except:
    shutil.rmtree(test_path)
    raise()
