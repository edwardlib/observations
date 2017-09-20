from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import shutil
import sys
import tempfile

from observations.r.volts import volts


def test_volts():
  """Test module volts.py by downloading
   volts.csv and testing shape of
   extracted data has 50 rows and 2 columns
  """
  test_path = tempfile.mkdtemp()
  x_train, metadata = volts(test_path)
  try:
    assert x_train.shape == (50, 2)
  except:
    shutil.rmtree(test_path)
    raise()
