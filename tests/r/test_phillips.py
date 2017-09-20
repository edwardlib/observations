from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import shutil
import sys
import tempfile

from observations.r.phillips import phillips


def test_phillips():
  """Test module phillips.py by downloading
   phillips.csv and testing shape of
   extracted data has 56 rows and 7 columns
  """
  test_path = tempfile.mkdtemp()
  x_train, metadata = phillips(test_path)
  try:
    assert x_train.shape == (56, 7)
  except:
    shutil.rmtree(test_path)
    raise()
