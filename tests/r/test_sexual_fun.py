from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import shutil
import sys
import tempfile

from observations.r.sexual_fun import sexual_fun


def test_sexual_fun():
  """Test module sexual_fun.py by downloading
   sexual_fun.csv and testing shape of
   extracted data has 4 rows and 4 columns
  """
  test_path = tempfile.mkdtemp()
  x_train, metadata = sexual_fun(test_path)
  try:
    assert x_train.shape == (4, 4)
  except:
    shutil.rmtree(test_path)
    raise()
