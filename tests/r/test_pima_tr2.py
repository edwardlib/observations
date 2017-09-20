from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import shutil
import sys
import tempfile

from observations.r.pima_tr2 import pima_tr2


def test_pima_tr2():
  """Test module pima_tr2.py by downloading
   pima_tr2.csv and testing shape of
   extracted data has 300 rows and 8 columns
  """
  test_path = tempfile.mkdtemp()
  x_train, metadata = pima_tr2(test_path)
  try:
    assert x_train.shape == (300, 8)
  except:
    shutil.rmtree(test_path)
    raise()
