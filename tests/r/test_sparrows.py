from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import shutil
import sys
import tempfile

from observations.r.sparrows import sparrows


def test_sparrows():
  """Test module sparrows.py by downloading
   sparrows.csv and testing shape of
   extracted data has 116 rows and 3 columns
  """
  test_path = tempfile.mkdtemp()
  x_train, metadata = sparrows(test_path)
  try:
    assert x_train.shape == (116, 3)
  except:
    shutil.rmtree(test_path)
    raise()
