from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import shutil
import sys
import tempfile

from observations.r.tms import tms


def test_tms():
  """Test module tms.py by downloading
   tms.csv and testing shape of
   extracted data has 2 rows and 4 columns
  """
  test_path = tempfile.mkdtemp()
  x_train, metadata = tms(test_path)
  try:
    assert x_train.shape == (2, 4)
  except:
    shutil.rmtree(test_path)
    raise()
