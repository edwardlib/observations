from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import shutil
import sys
import tempfile

from observations.r.auto_pollution import auto_pollution


def test_auto_pollution():
  """Test module auto_pollution.py by downloading
   auto_pollution.csv and testing shape of
   extracted data has 36 rows and 4 columns
  """
  test_path = tempfile.mkdtemp()
  x_train, metadata = auto_pollution(test_path)
  try:
    assert x_train.shape == (36, 4)
  except:
    shutil.rmtree(test_path)
    raise()
