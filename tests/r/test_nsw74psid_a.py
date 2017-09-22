from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import shutil
import sys
import tempfile

from observations.r.nsw74psid_a import nsw74psid_a


def test_nsw74psid_a():
  """Test module nsw74psid_a.py by downloading
   nsw74psid_a.csv and testing shape of
   extracted data has 252 rows and 10 columns
  """
  test_path = tempfile.mkdtemp()
  x_train, metadata = nsw74psid_a(test_path)
  try:
    assert x_train.shape == (252, 10)
  except:
    shutil.rmtree(test_path)
    raise()
