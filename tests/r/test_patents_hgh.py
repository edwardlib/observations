from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import shutil
import sys
import tempfile

from observations.r.patents_hgh import patents_hgh


def test_patents_hgh():
  """Test module patents_hgh.py by downloading
   patents_hgh.csv and testing shape of
   extracted data has 1730 rows and 18 columns
  """
  test_path = tempfile.mkdtemp()
  x_train, metadata = patents_hgh(test_path)
  try:
    assert x_train.shape == (1730, 18)
  except:
    shutil.rmtree(test_path)
    raise()
