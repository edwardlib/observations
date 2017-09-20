from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import shutil
import sys
import tempfile

from observations.r.political import political


def test_political():
  """Test module political.py by downloading
   political.csv and testing shape of
   extracted data has 59 rows and 9 columns
  """
  test_path = tempfile.mkdtemp()
  x_train, metadata = political(test_path)
  try:
    assert x_train.shape == (59, 9)
  except:
    shutil.rmtree(test_path)
    raise()
