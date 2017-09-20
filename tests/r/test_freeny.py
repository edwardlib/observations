from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import shutil
import sys
import tempfile

from observations.r.freeny import freeny


def test_freeny():
  """Test module freeny.py by downloading
   freeny.csv and testing shape of
   extracted data has 39 rows and 5 columns
  """
  test_path = tempfile.mkdtemp()
  x_train, metadata = freeny(test_path)
  try:
    assert x_train.shape == (39, 5)
  except:
    shutil.rmtree(test_path)
    raise()
