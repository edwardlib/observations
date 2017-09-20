from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import shutil
import sys
import tempfile

from observations.r.cattell import cattell


def test_cattell():
  """Test module cattell.py by downloading
   cattell.csv and testing shape of
   extracted data has 12 rows and 12 columns
  """
  test_path = tempfile.mkdtemp()
  x_train, metadata = cattell(test_path)
  try:
    assert x_train.shape == (12, 12)
  except:
    shutil.rmtree(test_path)
    raise()
