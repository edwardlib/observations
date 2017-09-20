from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import shutil
import sys
import tempfile

from observations.r.galton import galton


def test_galton():
  """Test module galton.py by downloading
   galton.csv and testing shape of
   extracted data has 898 rows and 6 columns
  """
  test_path = tempfile.mkdtemp()
  x_train, metadata = galton(test_path)
  try:
    assert x_train.shape == (898, 6)
  except:
    shutil.rmtree(test_path)
    raise()
