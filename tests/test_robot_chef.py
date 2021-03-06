import sys

from mock import patch
from io import StringIO


@patch("sys.stdout", new_callable=StringIO)
def test_peking_duck(stdout):
    arguments = ["robotchef", "Jacket Potato"]
    from robotchef_v2.main import main

    with patch.object(sys, "argv", arguments):
        main()
        assert stdout.getvalue() == "I can bake Jacket Potato\n"
