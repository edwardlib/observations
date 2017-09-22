from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import shutil
import sys
import tempfile

from observations.r.kidrecurr import kidrecurr


def test_kidrecurr():
  """Test module kidrecurr.py by downloading
   kidrecurr.csv and testing shape of
   extracted data has 38 rows and 10 columns
  """
  test_path = tempfile.mkdtemp()
  x_train, metadata = kidrecurr(test_path)
  try:
    assert x_train.shape == (38, 10)
  except:
    shutil.rmtree(test_path)
    raise()
