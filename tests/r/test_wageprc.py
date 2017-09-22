from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import shutil
import sys
import tempfile

from observations.r.wageprc import wageprc


def test_wageprc():
  """Test module wageprc.py by downloading
   wageprc.csv and testing shape of
   extracted data has 286 rows and 20 columns
  """
  test_path = tempfile.mkdtemp()
  x_train, metadata = wageprc(test_path)
  try:
    assert x_train.shape == (286, 20)
  except:
    shutil.rmtree(test_path)
    raise()
