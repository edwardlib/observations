from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import shutil
import sys
import tempfile

from observations.r.terrorism import terrorism


def test_terrorism():
  """Test module terrorism.py by downloading
   terrorism.csv and testing shape of
   extracted data has 46 rows and 25 columns
  """
  test_path = tempfile.mkdtemp()
  x_train, metadata = terrorism(test_path)
  try:
    assert x_train.shape == (46, 25)
  except:
    shutil.rmtree(test_path)
    raise()
