from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import shutil
import sys
import tempfile

from observations.r.wage2 import wage2


def test_wage2():
  """Test module wage2.py by downloading
   wage2.csv and testing shape of
   extracted data has 935 rows and 17 columns
  """
  test_path = tempfile.mkdtemp()
  x_train, metadata = wage2(test_path)
  try:
    assert x_train.shape == (935, 17)
  except:
    shutil.rmtree(test_path)
    raise()
