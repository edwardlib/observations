from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import shutil
import sys
import tempfile

from observations.r.murder import murder


def test_murder():
  """Test module murder.py by downloading
   murder.csv and testing shape of
   extracted data has 153 rows and 13 columns
  """
  test_path = tempfile.mkdtemp()
  x_train, metadata = murder(test_path)
  try:
    assert x_train.shape == (153, 13)
  except:
    shutil.rmtree(test_path)
    raise()
