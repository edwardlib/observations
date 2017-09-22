from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import shutil
import sys
import tempfile

from observations.r.foster import foster


def test_foster():
  """Test module foster.py by downloading
   foster.csv and testing shape of
   extracted data has 61 rows and 3 columns
  """
  test_path = tempfile.mkdtemp()
  x_train, metadata = foster(test_path)
  try:
    assert x_train.shape == (61, 3)
  except:
    shutil.rmtree(test_path)
    raise()
