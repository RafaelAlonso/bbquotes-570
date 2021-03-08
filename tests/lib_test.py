from bbquotes.lib import get_bbquote

def test_get_bbquote_type():
  assert type(get_bbquote()) == str

def test_get_bbquote():
  assert len(get_bbquote()) > 4