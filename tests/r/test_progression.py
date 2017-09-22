from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import shutil
import sys
import tempfile

from observations.r.progression import progression


def test_progression():
  """Test module progression.py by downloading
   progression.csv and testing shape of
   extracted data has 227 rows and 4 columns
  """
  test_path = tempfile.mkdtemp()
  x_train, metadata = progression(test_path)
  try:
    assert x_train.shape == (227, 4)
  except:
    shutil.rmtree(test_path)
    raise()
