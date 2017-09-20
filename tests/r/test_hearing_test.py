from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import shutil
import sys
import tempfile

from observations.r.hearing_test import hearing_test


def test_hearing_test():
  """Test module hearing_test.py by downloading
   hearing_test.csv and testing shape of
   extracted data has 96 rows and 3 columns
  """
  test_path = tempfile.mkdtemp()
  x_train, metadata = hearing_test(test_path)
  try:
    assert x_train.shape == (96, 3)
  except:
    shutil.rmtree(test_path)
    raise()
