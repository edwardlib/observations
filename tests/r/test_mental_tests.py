from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import shutil
import sys
import tempfile

from observations.r.mental_tests import mental_tests


def test_mental_tests():
  """Test module mental_tests.py by downloading
   mental_tests.csv and testing shape of
   extracted data has 32 rows and 6 columns
  """
  test_path = tempfile.mkdtemp()
  x_train, metadata = mental_tests(test_path)
  try:
    assert x_train.shape == (32, 6)
  except:
    shutil.rmtree(test_path)
    raise()
