from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import shutil
import sys
import tempfile

from observations.r.{{function}} import {{function}}


def test_{{function}}():
  """Test module {{function}}.py by downloading
   {{file_name}} and testing shape of
   extracted data has {{rows}} rows and {{cols}} columns
  """
  test_path = tempfile.mkdtemp()
  x_train, metadata = {{function}}(test_path)
  try:
    assert x_train.shape == ({{rows}}, {{cols}})
  except:
    shutil.rmtree(test_path)
    raise()

