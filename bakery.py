p_ls = ["Farinha", "Açúcar", "Café", "Fermento", "Sal", "Leite"]

ans = input("Quer começar a verificar? ")

while ans.upper() == "SIM":
  p_check = input("Qual você quer verificar? ")
  for a in p_ls:
    if a == p_check:
      print("Há o produto na lista!")
  if p_check not in p_ls:
    print("Produto não está presente na lista!")
  ans = input("Gostaria de continuar verificando? ")

if ans.upper() == "NÃO":
  print("Até a próxima!")
