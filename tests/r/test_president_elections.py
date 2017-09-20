from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import shutil
import sys
import tempfile

from observations.r.president_elections import president_elections


def test_president_elections():
  """Test module president_elections.py by downloading
   president_elections.csv and testing shape of
   extracted data has 1047 rows and 4 columns
  """
  test_path = tempfile.mkdtemp()
  x_train, metadata = president_elections(test_path)
  try:
    assert x_train.shape == (1047, 4)
  except:
    shutil.rmtree(test_path)
    raise()
