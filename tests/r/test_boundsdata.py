from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import shutil
import sys
import tempfile

from observations.r.boundsdata import boundsdata


def test_boundsdata():
  """Test module boundsdata.py by downloading
   boundsdata.csv and testing shape of
   extracted data has 1000 rows and 7 columns
  """
  test_path = tempfile.mkdtemp()
  x_train, metadata = boundsdata(test_path)
  try:
    assert x_train.shape == (1000, 7)
  except:
    shutil.rmtree(test_path)
    raise()
