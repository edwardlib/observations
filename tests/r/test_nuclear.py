from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import shutil
import sys
import tempfile

from observations.r.nuclear import nuclear


def test_nuclear():
  """Test module nuclear.py by downloading
   nuclear.csv and testing shape of
   extracted data has 32 rows and 11 columns
  """
  test_path = tempfile.mkdtemp()
  x_train, metadata = nuclear(test_path)
  try:
    assert x_train.shape == (32, 11)
  except:
    shutil.rmtree(test_path)
    raise()
