from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import shutil
import sys
import tempfile

from observations.r.marriage import marriage


def test_marriage():
  """Test module marriage.py by downloading
   marriage.csv and testing shape of
   extracted data has 98 rows and 15 columns
  """
  test_path = tempfile.mkdtemp()
  x_train, metadata = marriage(test_path)
  try:
    assert x_train.shape == (98, 15)
  except:
    shutil.rmtree(test_path)
    raise()
