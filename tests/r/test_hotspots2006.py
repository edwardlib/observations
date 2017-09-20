from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import shutil
import sys
import tempfile

from observations.r.hotspots2006 import hotspots2006


def test_hotspots2006():
  """Test module hotspots2006.py by downloading
   hotspots2006.csv and testing shape of
   extracted data has 10 rows and 6 columns
  """
  test_path = tempfile.mkdtemp()
  x_train, metadata = hotspots2006(test_path)
  try:
    assert x_train.shape == (10, 6)
  except:
    shutil.rmtree(test_path)
    raise()
