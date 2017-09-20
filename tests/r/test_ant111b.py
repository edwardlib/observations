from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import shutil
import sys
import tempfile

from observations.r.ant111b import ant111b


def test_ant111b():
  """Test module ant111b.py by downloading
   ant111b.csv and testing shape of
   extracted data has 32 rows and 9 columns
  """
  test_path = tempfile.mkdtemp()
  x_train, metadata = ant111b(test_path)
  try:
    assert x_train.shape == (32, 9)
  except:
    shutil.rmtree(test_path)
    raise()
