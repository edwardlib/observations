from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import shutil
import sys
import tempfile

from observations.r.uk_driver_deaths import uk_driver_deaths


def test_uk_driver_deaths():
  """Test module uk_driver_deaths.py by downloading
   uk_driver_deaths.csv and testing shape of
   extracted data has 192 rows and 2 columns
  """
  test_path = tempfile.mkdtemp()
  x_train, metadata = uk_driver_deaths(test_path)
  try:
    assert x_train.shape == (192, 2)
  except:
    shutil.rmtree(test_path)
    raise()
