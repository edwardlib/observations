from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import shutil
import sys
import tempfile

from observations.r.aspirin import aspirin


def test_aspirin():
  """Test module aspirin.py by downloading
   aspirin.csv and testing shape of
   extracted data has 7 rows and 4 columns
  """
  test_path = tempfile.mkdtemp()
  x_train, metadata = aspirin(test_path)
  try:
    assert x_train.shape == (7, 4)
  except:
    shutil.rmtree(test_path)
    raise()
