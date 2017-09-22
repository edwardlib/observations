from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import shutil
import sys
import tempfile

from observations.r.us_pop import us_pop


def test_us_pop():
  """Test module us_pop.py by downloading
   us_pop.csv and testing shape of
   extracted data has 22 rows and 2 columns
  """
  test_path = tempfile.mkdtemp()
  x_train, metadata = us_pop(test_path)
  try:
    assert x_train.shape == (22, 2)
  except:
    shutil.rmtree(test_path)
    raise()
