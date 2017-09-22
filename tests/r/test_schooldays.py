from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import shutil
import sys
import tempfile

from observations.r.schooldays import schooldays


def test_schooldays():
  """Test module schooldays.py by downloading
   schooldays.csv and testing shape of
   extracted data has 154 rows and 5 columns
  """
  test_path = tempfile.mkdtemp()
  x_train, metadata = schooldays(test_path)
  try:
    assert x_train.shape == (154, 5)
  except:
    shutil.rmtree(test_path)
    raise()
