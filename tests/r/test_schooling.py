from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import shutil
import sys
import tempfile

from observations.r.schooling import schooling


def test_schooling():
  """Test module schooling.py by downloading
   schooling.csv and testing shape of
   extracted data has 3010 rows and 28 columns
  """
  test_path = tempfile.mkdtemp()
  x_train, metadata = schooling(test_path)
  try:
    assert x_train.shape == (3010, 28)
  except:
    shutil.rmtree(test_path)
    raise()
