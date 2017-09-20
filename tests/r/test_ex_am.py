from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import shutil
import sys
import tempfile

from observations.r.ex_am import ex_am


def test_ex_am():
  """Test module ex_am.py by downloading
   ex_am.csv and testing shape of
   extracted data has 12 rows and 2 columns
  """
  test_path = tempfile.mkdtemp()
  x_train, metadata = ex_am(test_path)
  try:
    assert x_train.shape == (12, 2)
  except:
    shutil.rmtree(test_path)
    raise()
