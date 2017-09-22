from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import shutil
import sys
import tempfile

from observations.r.coleman import coleman


def test_coleman():
  """Test module coleman.py by downloading
   coleman.csv and testing shape of
   extracted data has 20 rows and 6 columns
  """
  test_path = tempfile.mkdtemp()
  x_train, metadata = coleman(test_path)
  try:
    assert x_train.shape == (20, 6)
  except:
    shutil.rmtree(test_path)
    raise()
