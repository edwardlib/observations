from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import shutil
import sys
import tempfile

from observations.r.watervoles import watervoles


def test_watervoles():
  """Test module watervoles.py by downloading
   watervoles.csv and testing shape of
   extracted data has 14 rows and 14 columns
  """
  test_path = tempfile.mkdtemp()
  x_train, metadata = watervoles(test_path)
  try:
    assert x_train.shape == (14, 14)
  except:
    shutil.rmtree(test_path)
    raise()
