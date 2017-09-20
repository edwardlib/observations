from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import shutil
import sys
import tempfile

from observations.r.cushny import cushny


def test_cushny():
  """Test module cushny.py by downloading
   cushny.csv and testing shape of
   extracted data has 10 rows and 7 columns
  """
  test_path = tempfile.mkdtemp()
  x_train, metadata = cushny(test_path)
  try:
    assert x_train.shape == (10, 7)
  except:
    shutil.rmtree(test_path)
    raise()
