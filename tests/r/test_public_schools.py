from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import shutil
import sys
import tempfile

from observations.r.public_schools import public_schools


def test_public_schools():
  """Test module public_schools.py by downloading
   public_schools.csv and testing shape of
   extracted data has 51 rows and 2 columns
  """
  test_path = tempfile.mkdtemp()
  x_train, metadata = public_schools(test_path)
  try:
    assert x_train.shape == (51, 2)
  except:
    shutil.rmtree(test_path)
    raise()
