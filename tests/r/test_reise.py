from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import shutil
import sys
import tempfile

from observations.r.reise import reise


def test_reise():
  """Test module reise.py by downloading
   reise.csv and testing shape of
   extracted data has 16 rows and 16 columns
  """
  test_path = tempfile.mkdtemp()
  x_train, metadata = reise(test_path)
  try:
    assert x_train.shape == (16, 16)
  except:
    shutil.rmtree(test_path)
    raise()
