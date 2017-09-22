from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import shutil
import sys
import tempfile

from observations.r.countries import countries


def test_countries():
  """Test module countries.py by downloading
   countries.csv and testing shape of
   extracted data has 288 rows and 3 columns
  """
  test_path = tempfile.mkdtemp()
  x_train, metadata = countries(test_path)
  try:
    assert x_train.shape == (288, 3)
  except:
    shutil.rmtree(test_path)
    raise()
