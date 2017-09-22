from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import shutil
import sys
import tempfile

from observations.r.patents_rd import patents_rd


def test_patents_rd():
  """Test module patents_rd.py by downloading
   patents_rd.csv and testing shape of
   extracted data has 1629 rows and 7 columns
  """
  test_path = tempfile.mkdtemp()
  x_train, metadata = patents_rd(test_path)
  try:
    assert x_train.shape == (1629, 7)
  except:
    shutil.rmtree(test_path)
    raise()
