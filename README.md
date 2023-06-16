# python basic
Resolução Trabalho com python nivel básico

**Enunciado:** Imagina-se que você e sua equipe foram contratados por uma empresa de logística que acabou de entrar no ramo. Essa empresa trabalha com encomendas de pequeno e médio porte e opera somente entre 3 cidades.
O valor que a empresa cobra por objeto é dado pela seguinte equação:

**total = dimensões x peso x rota**

Em que cada uma das variáveis que compõe o preço total é quantizada da seguinte maneira:
![TABELA1](https://github.com/annybuch/pythonbasic2/assets/132410900/a6dba5f2-f87c-44b0-a1d7-4271e5a02fa3)
![TABELA2](https://github.com/annybuch/pythonbasic2/assets/132410900/621ec9d4-d978-4fee-8beb-e7d59fe0e537)
![TABELA3](https://github.com/annybuch/pythonbasic2/assets/132410900/d466bf0d-24f2-46a1-9847-f12c465c15c0)

Elabore um programa em Python que:

- Pergunte a altura (em cm), comprimento (em cm) e largura (em cm) do objeto. Se digitar um valor não numérico e/ou as dimensões passarem do limite aceito repetir a pergunta;
- Pergunte o peso do objeto (em kg). Se digitar um valor não numérico e/ou o peso passar do limite aceito repetir a pergunta;
- Pergunte a rota do objeto. Se digitar uma opção que não esteja na tabela repetir a pergunta;
- Encerre o total a ser pago com base na equação desse enunciado;
- Calcular o volume (em cm) da caixa p/a objeto (altura x largura x comprimento);
- Deve-se ter try/except para o caso do usuário digitar um valor não numérico;
- Deve-se retornar o valor em (RS) conforme a Quadro 1
- Dentro da função perguntar peso do objeto (em kg);
- Deve-se ter um try/except para o caso de o usuário digitar um valor não numérico;
- Deve-se retornar o multiplicador conforme o Quadro 2
- Dentro da função perguntar a rota do objeto desejada (Sugestão: utilize as siglas para facilitar os testes);
