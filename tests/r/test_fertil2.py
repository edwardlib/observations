from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import shutil
import sys
import tempfile

from observations.r.fertil2 import fertil2


def test_fertil2():
  """Test module fertil2.py by downloading
   fertil2.csv and testing shape of
   extracted data has 4361 rows and 27 columns
  """
  test_path = tempfile.mkdtemp()
  x_train, metadata = fertil2(test_path)
  try:
    assert x_train.shape == (4361, 27)
  except:
    shutil.rmtree(test_path)
    raise()
