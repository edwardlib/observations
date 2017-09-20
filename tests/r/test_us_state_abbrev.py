from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import shutil
import sys
import tempfile

from observations.r.us_state_abbrev import us_state_abbrev


def test_us_state_abbrev():
  """Test module us_state_abbrev.py by downloading
   us_state_abbrev.csv and testing shape of
   extracted data has 76 rows and 10 columns
  """
  test_path = tempfile.mkdtemp()
  x_train, metadata = us_state_abbrev(test_path)
  try:
    assert x_train.shape == (76, 10)
  except:
    shutil.rmtree(test_path)
    raise()
