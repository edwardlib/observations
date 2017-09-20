from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import shutil
import sys
import tempfile

from observations.r.va_deaths import va_deaths


def test_va_deaths():
  """Test module va_deaths.py by downloading
   va_deaths.csv and testing shape of
   extracted data has 5 rows and 4 columns
  """
  test_path = tempfile.mkdtemp()
  x_train, metadata = va_deaths(test_path)
  try:
    assert x_train.shape == (5, 4)
  except:
    shutil.rmtree(test_path)
    raise()
