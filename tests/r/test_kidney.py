from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import shutil
import sys
import tempfile

from observations.r.kidney import kidney


def test_kidney():
  """Test module kidney.py by downloading
   kidney.csv and testing shape of
   extracted data has 76 rows and 7 columns
  """
  test_path = tempfile.mkdtemp()
  x_train, metadata = kidney(test_path)
  try:
    assert x_train.shape == (76, 7)
  except:
    shutil.rmtree(test_path)
    raise()
