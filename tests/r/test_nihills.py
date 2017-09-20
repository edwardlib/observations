from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import shutil
import sys
import tempfile

from observations.r.nihills import nihills


def test_nihills():
  """Test module nihills.py by downloading
   nihills.csv and testing shape of
   extracted data has 23 rows and 4 columns
  """
  test_path = tempfile.mkdtemp()
  x_train, metadata = nihills(test_path)
  try:
    assert x_train.shape == (23, 4)
  except:
    shutil.rmtree(test_path)
    raise()
