from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import shutil
import sys
import tempfile

from observations.r.fringe import fringe


def test_fringe():
  """Test module fringe.py by downloading
   fringe.csv and testing shape of
   extracted data has 616 rows and 39 columns
  """
  test_path = tempfile.mkdtemp()
  x_train, metadata = fringe(test_path)
  try:
    assert x_train.shape == (616, 39)
  except:
    shutil.rmtree(test_path)
    raise()
