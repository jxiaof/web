# -*-coding:utf-8 -*-
import fire

def hello(name="World"):
  return "Hello %s!" % name

class Calculator(object):
  """A simple calculator class."""

  def double(self, number):
    return 2 * number

if __name__ == '__main__':
  """
  python test_cli_fire.py "felix"
  python test_cli_fire.py --name=David 
  """

  # fire.Fire(hello)

  """
  python test_cli_fire.py double 10
  python test_cli_fire.py double --number=10
  """
  fire.Fire(Calculator)