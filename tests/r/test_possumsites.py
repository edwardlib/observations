from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import shutil
import sys
import tempfile

from observations.r.possumsites import possumsites


def test_possumsites():
  """Test module possumsites.py by downloading
   possumsites.csv and testing shape of
   extracted data has 7 rows and 3 columns
  """
  test_path = tempfile.mkdtemp()
  x_train, metadata = possumsites(test_path)
  try:
    assert x_train.shape == (7, 3)
  except:
    shutil.rmtree(test_path)
    raise()
