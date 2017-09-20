from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import shutil
import sys
import tempfile

from observations.r.nitrofen import nitrofen


def test_nitrofen():
  """Test module nitrofen.py by downloading
   nitrofen.csv and testing shape of
   extracted data has 50 rows and 5 columns
  """
  test_path = tempfile.mkdtemp()
  x_train, metadata = nitrofen(test_path)
  try:
    assert x_train.shape == (50, 5)
  except:
    shutil.rmtree(test_path)
    raise()
