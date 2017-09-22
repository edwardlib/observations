from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import shutil
import sys
import tempfile

from observations.r.world_phones import world_phones


def test_world_phones():
  """Test module world_phones.py by downloading
   world_phones.csv and testing shape of
   extracted data has 7 rows and 7 columns
  """
  test_path = tempfile.mkdtemp()
  x_train, metadata = world_phones(test_path)
  try:
    assert x_train.shape == (7, 7)
  except:
    shutil.rmtree(test_path)
    raise()
