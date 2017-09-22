from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import shutil
import sys
import tempfile

from observations.r.nsw74demo import nsw74demo


def test_nsw74demo():
  """Test module nsw74demo.py by downloading
   nsw74demo.csv and testing shape of
   extracted data has 445 rows and 10 columns
  """
  test_path = tempfile.mkdtemp()
  x_train, metadata = nsw74demo(test_path)
  try:
    assert x_train.shape == (445, 10)
  except:
    shutil.rmtree(test_path)
    raise()
