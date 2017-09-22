from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import shutil
import sys
import tempfile

from observations.r.rareplants import rareplants


def test_rareplants():
  """Test module rareplants.py by downloading
   rareplants.csv and testing shape of
   extracted data has 4 rows and 3 columns
  """
  test_path = tempfile.mkdtemp()
  x_train, metadata = rareplants(test_path)
  try:
    assert x_train.shape == (4, 3)
  except:
    shutil.rmtree(test_path)
    raise()
