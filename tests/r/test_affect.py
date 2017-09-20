from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import shutil
import sys
import tempfile

from observations.r.affect import affect


def test_affect():
  """Test module affect.py by downloading
   affect.csv and testing shape of
   extracted data has 330 rows and 20 columns
  """
  test_path = tempfile.mkdtemp()
  x_train, metadata = affect(test_path)
  try:
    assert x_train.shape == (330, 20)
  except:
    shutil.rmtree(test_path)
    raise()
