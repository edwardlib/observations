from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import shutil
import sys
import tempfile

from observations.r.cerealsugar import cerealsugar


def test_cerealsugar():
  """Test module cerealsugar.py by downloading
   cerealsugar.csv and testing shape of
   extracted data has 100 rows and 1 columns
  """
  test_path = tempfile.mkdtemp()
  x_train, metadata = cerealsugar(test_path)
  try:
    assert x_train.shape == (100, 1)
  except:
    shutil.rmtree(test_path)
    raise()
