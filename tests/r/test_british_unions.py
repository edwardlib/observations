from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import shutil
import sys
import tempfile

from observations.r.british_unions import british_unions


def test_british_unions():
  """Test module british_unions.py by downloading
   british_unions.csv and testing shape of
   extracted data has 17 rows and 7 columns
  """
  test_path = tempfile.mkdtemp()
  x_train, metadata = british_unions(test_path)
  try:
    assert x_train.shape == (17, 7)
  except:
    shutil.rmtree(test_path)
    raise()
