from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import shutil
import sys
import tempfile

from observations.r.help_miss import help_miss


def test_help_miss():
  """Test module help_miss.py by downloading
   help_miss.csv and testing shape of
   extracted data has 470 rows and 25 columns
  """
  test_path = tempfile.mkdtemp()
  x_train, metadata = help_miss(test_path)
  try:
    assert x_train.shape == (470, 25)
  except:
    shutil.rmtree(test_path)
    raise()
