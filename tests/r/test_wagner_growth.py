from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import shutil
import sys
import tempfile

from observations.r.wagner_growth import wagner_growth


def test_wagner_growth():
  """Test module wagner_growth.py by downloading
   wagner_growth.csv and testing shape of
   extracted data has 63 rows and 7 columns
  """
  test_path = tempfile.mkdtemp()
  x_train, metadata = wagner_growth(test_path)
  try:
    assert x_train.shape == (63, 7)
  except:
    shutil.rmtree(test_path)
    raise()
