# ProjetoIntegrador-CD

Projeto Integrador entre as metérias Versionamento, Lógica de Programação e Metodologias Ágeis

---


## Levantamento de Requisitos

### Regras de Negócio (RN)
- RN01 (Critério de Recuperação): Um aluno é considerado em recuperação se a sua média de notas for inferior a 7.0.
- RN02 (Variabilidade de Dados): O sistema deve suportar um número variável de notas por aluno, dependendo do que foi entregue.
- RN03 (Destaque de Desempenho): Apenas o aluno com a maior média global deve ser classificado como "Top Student".
- RN04 (Integridade): Dados vazios ou corrompidos devem ser identificados e tratados antes do cálculo para evitar erros na situação acadêmica.   

###  Requisitos Funcionais (RF) 
- RF01: O sistema deve processar uma lista de tuplas contendo nome e notas do aluno.
- RF02: O sistema deve validar se a lista de notas não está vazia ou corrompida.
- RF03: O sistema deve calcular a média aritmética das notas de cada aluno.
- RF04: O sistema deve identificar alunos em situação de recuperação.
- RF05: O sistema deve identificar o aluno com a maior média.
- RF06: O sistema deve gerar um arquivo resultado.txt formatado com o relatório final.

### Requisitos Não-Funcionais (RNF)
- RNF01: O código deve ser obrigatoriamente dividido nos arquivos main.py e processamento.py.
- RNF02: Uso de branches separadas para cada funcionalidade e realização de merge para a main.
- RNF03: O processamento deve garantir que dados corrompidos não interrompam a execução ou gerem médias falsas.
- RNF04: O repositório deve conter um arquivo README.md com requisitos, Kanban e Mapa de Empatia.

---

## Kanban no Trello
```bash
https://trello.com/invite/b/69b886a634563dfe89d2f0f9/ATTId914bb208702316647a7aedfd629b017A49AE01C/kanban-quadro-modelo
```
<img width="1022" height="612" alt="image" src="https://github.com/user-attachments/assets/fd21a055-840f-4653-ad70-52cc045cb4ce" />

--- 
## Mapa da Empatia
<img width="1520" height="680" alt="Pastel Tabs Customer Empathy Map Brainstorm" src="https://github.com/user-attachments/assets/dec5ddbd-2b06-446c-85de-f1d013ad4b96" />

