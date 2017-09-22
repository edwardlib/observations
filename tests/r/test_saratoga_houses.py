from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import shutil
import sys
import tempfile

from observations.r.saratoga_houses import saratoga_houses


def test_saratoga_houses():
  """Test module saratoga_houses.py by downloading
   saratoga_houses.csv and testing shape of
   extracted data has 1728 rows and 16 columns
  """
  test_path = tempfile.mkdtemp()
  x_train, metadata = saratoga_houses(test_path)
  try:
    assert x_train.shape == (1728, 16)
  except:
    shutil.rmtree(test_path)
    raise()
