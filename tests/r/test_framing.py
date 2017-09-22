from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import shutil
import sys
import tempfile

from observations.r.framing import framing


def test_framing():
  """Test module framing.py by downloading
   framing.csv and testing shape of
   extracted data has 265 rows and 15 columns
  """
  test_path = tempfile.mkdtemp()
  x_train, metadata = framing(test_path)
  try:
    assert x_train.shape == (265, 15)
  except:
    shutil.rmtree(test_path)
    raise()
