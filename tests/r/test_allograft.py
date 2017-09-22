from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import shutil
import sys
import tempfile

from observations.r.allograft import allograft


def test_allograft():
  """Test module allograft.py by downloading
   allograft.csv and testing shape of
   extracted data has 34 rows and 4 columns
  """
  test_path = tempfile.mkdtemp()
  x_train, metadata = allograft(test_path)
  try:
    assert x_train.shape == (34, 4)
  except:
    shutil.rmtree(test_path)
    raise()
