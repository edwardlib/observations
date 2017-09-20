from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import shutil
import sys
import tempfile

from observations.r.prostitutes import prostitutes


def test_prostitutes():
  """Test module prostitutes.py by downloading
   prostitutes.csv and testing shape of
   extracted data has 516 rows and 5 columns
  """
  test_path = tempfile.mkdtemp()
  x_train, metadata = prostitutes(test_path)
  try:
    assert x_train.shape == (516, 5)
  except:
    shutil.rmtree(test_path)
    raise()
