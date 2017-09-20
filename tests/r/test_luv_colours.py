from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import shutil
import sys
import tempfile

from observations.r.luv_colours import luv_colours


def test_luv_colours():
  """Test module luv_colours.py by downloading
   luv_colours.csv and testing shape of
   extracted data has 657 rows and 4 columns
  """
  test_path = tempfile.mkdtemp()
  x_train, metadata = luv_colours(test_path)
  try:
    assert x_train.shape == (657, 4)
  except:
    shutil.rmtree(test_path)
    raise()
