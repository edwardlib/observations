from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import shutil
import sys
import tempfile

from observations.r.claridge import claridge


def test_claridge():
  """Test module claridge.py by downloading
   claridge.csv and testing shape of
   extracted data has 37 rows and 2 columns
  """
  test_path = tempfile.mkdtemp()
  x_train, metadata = claridge(test_path)
  try:
    assert x_train.shape == (37, 2)
  except:
    shutil.rmtree(test_path)
    raise()
