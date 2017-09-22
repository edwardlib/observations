from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import shutil
import sys
import tempfile

from observations.r.ability import ability


def test_ability():
  """Test module ability.py by downloading
   ability.csv and testing shape of
   extracted data has 1525 rows and 16 columns
  """
  test_path = tempfile.mkdtemp()
  x_train, metadata = ability(test_path)
  try:
    assert x_train.shape == (1525, 16)
  except:
    shutil.rmtree(test_path)
    raise()
