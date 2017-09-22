from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import shutil
import sys
import tempfile

from observations.r.attenu import attenu


def test_attenu():
  """Test module attenu.py by downloading
   attenu.csv and testing shape of
   extracted data has 182 rows and 5 columns
  """
  test_path = tempfile.mkdtemp()
  x_train, metadata = attenu(test_path)
  try:
    assert x_train.shape == (182, 5)
  except:
    shutil.rmtree(test_path)
    raise()
