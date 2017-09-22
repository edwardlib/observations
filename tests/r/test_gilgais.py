from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import shutil
import sys
import tempfile

from observations.r.gilgais import gilgais


def test_gilgais():
  """Test module gilgais.py by downloading
   gilgais.csv and testing shape of
   extracted data has 365 rows and 9 columns
  """
  test_path = tempfile.mkdtemp()
  x_train, metadata = gilgais(test_path)
  try:
    assert x_train.shape == (365, 9)
  except:
    shutil.rmtree(test_path)
    raise()
