from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import shutil
import sys
import tempfile

from observations.r.supreme_court import supreme_court


def test_supreme_court():
  """Test module supreme_court.py by downloading
   supreme_court.csv and testing shape of
   extracted data has 43 rows and 9 columns
  """
  test_path = tempfile.mkdtemp()
  x_train, metadata = supreme_court(test_path)
  try:
    assert x_train.shape == (43, 9)
  except:
    shutil.rmtree(test_path)
    raise()
