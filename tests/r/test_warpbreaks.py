from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import shutil
import sys
import tempfile

from observations.r.warpbreaks import warpbreaks


def test_warpbreaks():
  """Test module warpbreaks.py by downloading
   warpbreaks.csv and testing shape of
   extracted data has 54 rows and 3 columns
  """
  test_path = tempfile.mkdtemp()
  x_train, metadata = warpbreaks(test_path)
  try:
    assert x_train.shape == (54, 3)
  except:
    shutil.rmtree(test_path)
    raise()
