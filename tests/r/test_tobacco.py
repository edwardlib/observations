from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import shutil
import sys
import tempfile

from observations.r.tobacco import tobacco


def test_tobacco():
  """Test module tobacco.py by downloading
   tobacco.csv and testing shape of
   extracted data has 2724 rows and 9 columns
  """
  test_path = tempfile.mkdtemp()
  x_train, metadata = tobacco(test_path)
  try:
    assert x_train.shape == (2724, 9)
  except:
    shutil.rmtree(test_path)
    raise()
