from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import shutil
import sys
import tempfile

from observations.r.twins_lungs import twins_lungs


def test_twins_lungs():
  """Test module twins_lungs.py by downloading
   twins_lungs.csv and testing shape of
   extracted data has 14 rows and 3 columns
  """
  test_path = tempfile.mkdtemp()
  x_train, metadata = twins_lungs(test_path)
  try:
    assert x_train.shape == (14, 3)
  except:
    shutil.rmtree(test_path)
    raise()
