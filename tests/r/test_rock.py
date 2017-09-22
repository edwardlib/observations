from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import shutil
import sys
import tempfile

from observations.r.rock import rock


def test_rock():
  """Test module rock.py by downloading
   rock.csv and testing shape of
   extracted data has 48 rows and 4 columns
  """
  test_path = tempfile.mkdtemp()
  x_train, metadata = rock(test_path)
  try:
    assert x_train.shape == (48, 4)
  except:
    shutil.rmtree(test_path)
    raise()
