from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import shutil
import sys
import tempfile

from observations.r.attend import attend


def test_attend():
  """Test module attend.py by downloading
   attend.csv and testing shape of
   extracted data has 680 rows and 11 columns
  """
  test_path = tempfile.mkdtemp()
  x_train, metadata = attend(test_path)
  try:
    assert x_train.shape == (680, 11)
  except:
    shutil.rmtree(test_path)
    raise()
