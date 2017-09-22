from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import shutil
import sys
import tempfile

from observations.r.hmda import hmda


def test_hmda():
  """Test module hmda.py by downloading
   hmda.csv and testing shape of
   extracted data has 2381 rows and 13 columns
  """
  test_path = tempfile.mkdtemp()
  x_train, metadata = hmda(test_path)
  try:
    assert x_train.shape == (2381, 13)
  except:
    shutil.rmtree(test_path)
    raise()
