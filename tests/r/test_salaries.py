from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import shutil
import sys
import tempfile

from observations.r.salaries import salaries


def test_salaries():
  """Test module salaries.py by downloading
   salaries.csv and testing shape of
   extracted data has 397 rows and 6 columns
  """
  test_path = tempfile.mkdtemp()
  x_train, metadata = salaries(test_path)
  try:
    assert x_train.shape == (397, 6)
  except:
    shutil.rmtree(test_path)
    raise()
