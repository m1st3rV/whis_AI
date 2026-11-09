🪽 Whis — Agente de IA para Programadores e Profissionais de Segurança


Um agente de IA didático que explica vulnerabilidades conhecidas com provas de conceito (PoC) educacionais e revela as particularidades do Python e de suas bibliotecas. Inspirado no mestre e anjo Whis, de Dragon Ball.



📌 Sobre o projeto

Assim como Whis é o mentor que treina Goku e Vegeta, este agente atua como um mentor técnico: ele guia quem está aprendendo programação e segurança da informação, explicando por que uma falha existe, como ela funciona e como corrigi-la.

O projeto é voltado para:

Programadores que querem escrever código mais seguro e entender as armadilhas do Python.
Profissionais de segurança de TI que querem estudar vulnerabilidades conhecidas em ambientes de laboratório.
Estudantes de tecnologia e segurança que aprendem melhor com exemplos práticos.
✨ Funcionalidades
🔍 Provas de conceito didáticas: demonstra vulnerabilidades já conhecidas e documentadas (com CVEs públicos, quando aplicável) em ambiente controlado, com explicação passo a passo.
🧪 Como identificar se o seu sistema está vulnerável: ensina a verificar versões de bibliotecas afetadas, configurações inseguras e padrões de código de risco no seu próprio ambiente.
🛡️ Foco em mitigação: toda demonstração vem acompanhada da correção recomendada e de boas práticas.
🐍 Particularidades do Python: explica comportamentos curiosos da linguagem e das bibliotecas (por exemplo: pickle, eval, subprocess, mutabilidade, escopo, serialização, injeção de dependências).
📚 Explicações para vários níveis: do iniciante ao avançado.
💬 Interface de chat simples feita com Streamlit.
⚠️ Aviso de uso responsável

Este projeto tem fins exclusivamente educacionais.

Use as provas de conceito apenas em ambientes próprios, de laboratório ou com autorização expressa do proprietário do sistema.
O conteúdo cobre vulnerabilidades já conhecidas e públicas, com foco em aprendizado e defesa.
O autor não se responsabiliza por qualquer uso indevido, ilegal ou antiético das informações aqui apresentadas.
Testar sistemas sem autorização é crime em diversos países, incluindo o Brasil.
🛠️ Tecnologias utilizadas
Python
Streamlit
grok


API do modelo de IA utilizado (ex.: Anthropic)


📂 Estrutura do projeto
.
├── app.py              # Código principal da aplicação Streamlit
├── whis.png            # Imagem usada na interface
├── requirements.txt    # Dependências do projeto
├── .env.example        # Exemplo das variáveis de ambiente
├── LICENSE
└── README.md




💡 Exemplos de uso

Você pode perguntar coisas como:

"Explique por que desserializar dados não confiáveis com pickle é perigoso e mostre uma PoC didática."
"Por que eval() é considerado arriscado? Como substituir por ast.literal_eval?"
"Como posso verificar se o meu projeto usa uma versão vulnerável de determinada biblioteca?"
"Quais sinais no meu código indicam que ele pode estar vulnerável a injeção de comandos?"
"Quais são as armadilhas de argumentos padrão mutáveis em Python?"
"Como funciona uma injeção de comandos via subprocess e como evitá-la?"

☁️ Deploy

O projeto pode ser publicado gratuitamente no Streamlit Community Cloud:

Suba o código para o GitHub (com o requirements.txt na raiz).
Acesse o Streamlit Cloud e conecte sua conta do GitHub.
Selecione o repositório e o arquivo principal (app.py).
Configure as chaves de API em Secrets.
Clique em Deploy.


🗺️ Próximos passos
 Adicionar mais categorias de vulnerabilidades (OWASP Top 10)
 Criar modo "treino": desafios para o usuário encontrar e corrigir a falha
 Incluir referências automáticas a CVEs e documentação oficial
 Histórico de conversas
 Testes automatizados


🤝 Contribuindo

Contribuições são bem-vindas!

🙏 Créditos e inspiração

O personagem Whis pertence a Akira Toriyama / Toei Animation / Shueisha. Este projeto é uma homenagem de fã, sem fins lucrativos e sem qualquer afiliação oficial com os detentores dos direitos.

📄 Licença

Este projeto está sob a licença MIT. Veja o arquivo LICENSE para mais detalhes.

👤 Autor

Danilo França

GitHub: @m1st3rV
