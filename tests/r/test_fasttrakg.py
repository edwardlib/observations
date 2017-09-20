from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import shutil
import sys
import tempfile

from observations.r.fasttrakg import fasttrakg


def test_fasttrakg():
  """Test module fasttrakg.py by downloading
   fasttrakg.csv and testing shape of
   extracted data has 15 rows and 9 columns
  """
  test_path = tempfile.mkdtemp()
  x_train, metadata = fasttrakg(test_path)
  try:
    assert x_train.shape == (15, 9)
  except:
    shutil.rmtree(test_path)
    raise()
