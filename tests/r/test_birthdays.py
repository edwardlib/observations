from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import shutil
import sys
import tempfile

from observations.r.birthdays import birthdays


def test_birthdays():
  """Test module birthdays.py by downloading
   birthdays.csv and testing shape of
   extracted data has 372864 rows and 7 columns
  """
  test_path = tempfile.mkdtemp()
  x_train, metadata = birthdays(test_path)
  try:
    assert x_train.shape == (372864, 7)
  except:
    shutil.rmtree(test_path)
    raise()
