from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import shutil
import sys
import tempfile

from observations.r.benefits1 import benefits1


def test_benefits1():
  """Test module benefits1.py by downloading
   benefits1.csv and testing shape of
   extracted data has 1848 rows and 18 columns
  """
  test_path = tempfile.mkdtemp()
  x_train, metadata = benefits1(test_path)
  try:
    assert x_train.shape == (1848, 18)
  except:
    shutil.rmtree(test_path)
    raise()
