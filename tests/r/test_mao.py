from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import shutil
import sys
import tempfile

from observations.r.mao import mao


def test_mao():
  """Test module mao.py by downloading
   mao.csv and testing shape of
   extracted data has 340 rows and 19 columns
  """
  test_path = tempfile.mkdtemp()
  x_train, metadata = mao(test_path)
  try:
    assert x_train.shape == (340, 19)
  except:
    shutil.rmtree(test_path)
    raise()
