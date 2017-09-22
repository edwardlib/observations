from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import shutil
import sys
import tempfile

from observations.r.uk_house_of_commons import uk_house_of_commons


def test_uk_house_of_commons():
  """Test module uk_house_of_commons.py by downloading
   uk_house_of_commons.csv and testing shape of
   extracted data has 521 rows and 12 columns
  """
  test_path = tempfile.mkdtemp()
  x_train, metadata = uk_house_of_commons(test_path)
  try:
    assert x_train.shape == (521, 12)
  except:
    shutil.rmtree(test_path)
    raise()
