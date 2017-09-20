from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import shutil
import sys
import tempfile

from observations.r.us_tax_words import us_tax_words


def test_us_tax_words():
  """Test module us_tax_words.py by downloading
   us_tax_words.csv and testing shape of
   extracted data has 7 rows and 10 columns
  """
  test_path = tempfile.mkdtemp()
  x_train, metadata = us_tax_words(test_path)
  try:
    assert x_train.shape == (7, 10)
  except:
    shutil.rmtree(test_path)
    raise()
