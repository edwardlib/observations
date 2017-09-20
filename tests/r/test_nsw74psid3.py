from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import shutil
import sys
import tempfile

from observations.r.nsw74psid3 import nsw74psid3


def test_nsw74psid3():
  """Test module nsw74psid3.py by downloading
   nsw74psid3.csv and testing shape of
   extracted data has 313 rows and 10 columns
  """
  test_path = tempfile.mkdtemp()
  x_train, metadata = nsw74psid3(test_path)
  try:
    assert x_train.shape == (313, 10)
  except:
    shutil.rmtree(test_path)
    raise()
