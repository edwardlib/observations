from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import shutil
import sys
import tempfile

from observations.r.brambles import brambles


def test_brambles():
  """Test module brambles.py by downloading
   brambles.csv and testing shape of
   extracted data has 823 rows and 3 columns
  """
  test_path = tempfile.mkdtemp()
  x_train, metadata = brambles(test_path)
  try:
    assert x_train.shape == (823, 3)
  except:
    shutil.rmtree(test_path)
    raise()
