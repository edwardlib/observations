from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import shutil
import sys
import tempfile

from observations.r.bladder import bladder


def test_bladder():
  """Test module bladder.py by downloading
   bladder.csv and testing shape of
   extracted data has 340 rows and 7 columns
  """
  test_path = tempfile.mkdtemp()
  x_train, metadata = bladder(test_path)
  try:
    assert x_train.shape == (340, 7)
  except:
    shutil.rmtree(test_path)
    raise()
