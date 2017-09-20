from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import shutil
import sys
import tempfile

from observations.r.child_speaks import child_speaks


def test_child_speaks():
  """Test module child_speaks.py by downloading
   child_speaks.csv and testing shape of
   extracted data has 21 rows and 3 columns
  """
  test_path = tempfile.mkdtemp()
  x_train, metadata = child_speaks(test_path)
  try:
    assert x_train.shape == (21, 3)
  except:
    shutil.rmtree(test_path)
    raise()
