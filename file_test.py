import pytest

def test_calc_addition():
  # Foncton test du résultat de 2+4
  output = 2+4
  assert output == 6

def test_calc_substraction():
  # Fonction test du résultat 2-4
  output = 2-4
  assert output == -2

def test_calc_multiply():
  # Fonction test du résultat 2*4
  output = 2*4
  assert output == 8

def test_coucou():
  # Fonction test qui renvoie coucou
  output = "hello"

	assert output == "hello"
