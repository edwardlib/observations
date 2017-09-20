from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import shutil
import sys
import tempfile

from observations.r.ambient_noxch import ambient_noxch


def test_ambient_noxch():
  """Test module ambient_noxch.py by downloading
   ambient_noxch.csv and testing shape of
   extracted data has 366 rows and 14 columns
  """
  test_path = tempfile.mkdtemp()
  x_train, metadata = ambient_noxch(test_path)
  try:
    assert x_train.shape == (366, 14)
  except:
    shutil.rmtree(test_path)
    raise()
