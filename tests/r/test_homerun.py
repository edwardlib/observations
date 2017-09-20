from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import shutil
import sys
import tempfile

from observations.r.homerun import homerun


def test_homerun():
  """Test module homerun.py by downloading
   homerun.csv and testing shape of
   extracted data has 314 rows and 5 columns
  """
  test_path = tempfile.mkdtemp()
  x_train, metadata = homerun(test_path)
  try:
    assert x_train.shape == (314, 5)
  except:
    shutil.rmtree(test_path)
    raise()
