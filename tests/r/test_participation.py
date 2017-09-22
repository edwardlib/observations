from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import shutil
import sys
import tempfile

from observations.r.participation import participation


def test_participation():
  """Test module participation.py by downloading
   participation.csv and testing shape of
   extracted data has 872 rows and 7 columns
  """
  test_path = tempfile.mkdtemp()
  x_train, metadata = participation(test_path)
  try:
    assert x_train.shape == (872, 7)
  except:
    shutil.rmtree(test_path)
    raise()
