from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import shutil
import sys
import tempfile

from observations.r.antigua import antigua


def test_antigua():
  """Test module antigua.py by downloading
   antigua.csv and testing shape of
   extracted data has 288 rows and 7 columns
  """
  test_path = tempfile.mkdtemp()
  x_train, metadata = antigua(test_path)
  try:
    assert x_train.shape == (288, 7)
  except:
    shutil.rmtree(test_path)
    raise()
