from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import shutil
import sys
import tempfile

from observations.r.abbey import abbey


def test_abbey():
  """Test module abbey.py by downloading
   abbey.csv and testing shape of
   extracted data has 31 rows and 1 columns
  """
  test_path = tempfile.mkdtemp()
  x_train, metadata = abbey(test_path)
  try:
    assert x_train.shape == (31, 1)
  except:
    shutil.rmtree(test_path)
    raise()
