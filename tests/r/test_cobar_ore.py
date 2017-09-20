from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import shutil
import sys
import tempfile

from observations.r.cobar_ore import cobar_ore


def test_cobar_ore():
  """Test module cobar_ore.py by downloading
   cobar_ore.csv and testing shape of
   extracted data has 38 rows and 3 columns
  """
  test_path = tempfile.mkdtemp()
  x_train, metadata = cobar_ore(test_path)
  try:
    assert x_train.shape == (38, 3)
  except:
    shutil.rmtree(test_path)
    raise()
