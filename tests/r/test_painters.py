from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import shutil
import sys
import tempfile

from observations.r.painters import painters


def test_painters():
  """Test module painters.py by downloading
   painters.csv and testing shape of
   extracted data has 54 rows and 5 columns
  """
  test_path = tempfile.mkdtemp()
  x_train, metadata = painters(test_path)
  try:
    assert x_train.shape == (54, 5)
  except:
    shutil.rmtree(test_path)
    raise()
