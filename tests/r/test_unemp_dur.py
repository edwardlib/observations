from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import shutil
import sys
import tempfile

from observations.r.unemp_dur import unemp_dur


def test_unemp_dur():
  """Test module unemp_dur.py by downloading
   unemp_dur.csv and testing shape of
   extracted data has 3343 rows and 11 columns
  """
  test_path = tempfile.mkdtemp()
  x_train, metadata = unemp_dur(test_path)
  try:
    assert x_train.shape == (3343, 11)
  except:
    shutil.rmtree(test_path)
    raise()
