from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import shutil
import sys
import tempfile

from observations.r.corn import corn


def test_corn():
  """Test module corn.py by downloading
   corn.csv and testing shape of
   extracted data has 37 rows and 5 columns
  """
  test_path = tempfile.mkdtemp()
  x_train, metadata = corn(test_path)
  try:
    assert x_train.shape == (37, 5)
  except:
    shutil.rmtree(test_path)
    raise()
