from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import shutil
import sys
import tempfile

from observations.r.weightgain import weightgain


def test_weightgain():
  """Test module weightgain.py by downloading
   weightgain.csv and testing shape of
   extracted data has 40 rows and 3 columns
  """
  test_path = tempfile.mkdtemp()
  x_train, metadata = weightgain(test_path)
  try:
    assert x_train.shape == (40, 3)
  except:
    shutil.rmtree(test_path)
    raise()
