from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import shutil
import sys
import tempfile

from observations.r.university import university


def test_university():
  """Test module university.py by downloading
   university.csv and testing shape of
   extracted data has 62 rows and 17 columns
  """
  test_path = tempfile.mkdtemp()
  x_train, metadata = university(test_path)
  try:
    assert x_train.shape == (62, 17)
  except:
    shutil.rmtree(test_path)
    raise()
