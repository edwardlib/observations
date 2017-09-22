from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import shutil
import sys
import tempfile

from observations.r.psid import psid


def test_psid():
  """Test module psid.py by downloading
   psid.csv and testing shape of
   extracted data has 4856 rows and 8 columns
  """
  test_path = tempfile.mkdtemp()
  x_train, metadata = psid(test_path)
  try:
    assert x_train.shape == (4856, 8)
  except:
    shutil.rmtree(test_path)
    raise()
