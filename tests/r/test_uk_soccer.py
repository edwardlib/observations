from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import shutil
import sys
import tempfile

from observations.r.uk_soccer import uk_soccer


def test_uk_soccer():
  """Test module uk_soccer.py by downloading
   uk_soccer.csv and testing shape of
   extracted data has 5 rows and 5 columns
  """
  test_path = tempfile.mkdtemp()
  x_train, metadata = uk_soccer(test_path)
  try:
    assert x_train.shape == (5, 5)
  except:
    shutil.rmtree(test_path)
    raise()
