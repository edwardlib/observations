from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import shutil
import sys
import tempfile

from observations.r.cushings import cushings


def test_cushings():
  """Test module cushings.py by downloading
   cushings.csv and testing shape of
   extracted data has 27 rows and 3 columns
  """
  test_path = tempfile.mkdtemp()
  x_train, metadata = cushings(test_path)
  try:
    assert x_train.shape == (27, 3)
  except:
    shutil.rmtree(test_path)
    raise()
