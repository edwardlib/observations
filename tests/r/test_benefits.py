from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import shutil
import sys
import tempfile

from observations.r.benefits import benefits


def test_benefits():
  """Test module benefits.py by downloading
   benefits.csv and testing shape of
   extracted data has 4877 rows and 18 columns
  """
  test_path = tempfile.mkdtemp()
  x_train, metadata = benefits(test_path)
  try:
    assert x_train.shape == (4877, 18)
  except:
    shutil.rmtree(test_path)
    raise()
