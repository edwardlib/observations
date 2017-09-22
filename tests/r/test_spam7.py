from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import shutil
import sys
import tempfile

from observations.r.spam7 import spam7


def test_spam7():
  """Test module spam7.py by downloading
   spam7.csv and testing shape of
   extracted data has 4601 rows and 7 columns
  """
  test_path = tempfile.mkdtemp()
  x_train, metadata = spam7(test_path)
  try:
    assert x_train.shape == (4601, 7)
  except:
    shutil.rmtree(test_path)
    raise()
