from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import shutil
import sys
import tempfile

from observations.r.prminwge import prminwge


def test_prminwge():
  """Test module prminwge.py by downloading
   prminwge.csv and testing shape of
   extracted data has 38 rows and 25 columns
  """
  test_path = tempfile.mkdtemp()
  x_train, metadata = prminwge(test_path)
  try:
    assert x_train.shape == (38, 25)
  except:
    shutil.rmtree(test_path)
    raise()
