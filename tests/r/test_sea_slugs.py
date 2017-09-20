from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import shutil
import sys
import tempfile

from observations.r.sea_slugs import sea_slugs


def test_sea_slugs():
  """Test module sea_slugs.py by downloading
   sea_slugs.csv and testing shape of
   extracted data has 36 rows and 2 columns
  """
  test_path = tempfile.mkdtemp()
  x_train, metadata = sea_slugs(test_path)
  try:
    assert x_train.shape == (36, 2)
  except:
    shutil.rmtree(test_path)
    raise()
