from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import shutil
import sys
import tempfile

from observations.r.portpirie import portpirie


def test_portpirie():
  """Test module portpirie.py by downloading
   portpirie.csv and testing shape of
   extracted data has 65 rows and 2 columns
  """
  test_path = tempfile.mkdtemp()
  x_train, metadata = portpirie(test_path)
  try:
    assert x_train.shape == (65, 2)
  except:
    shutil.rmtree(test_path)
    raise()
