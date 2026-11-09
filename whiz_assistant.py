# Importa o módulo pra interagir com o sistema operacional
import os

# Importa a biblioteca Streamlit para criar a interface web interativa
import streamlit as st

# Importa a classe Groq para se conectar à API da plataforma Groq e acessar o LLM
from groq import Groq


# Configura a página do Streamlit com título, ícone, layout e estado inicial da sidebar
st.set_page_config(
    page_title="Whiz Assistant",
    page_icon="🤖",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Define um prompt de sistema que descreve as regras e comportamento do assistente de IA
CUSTOM_PROMPT = """
Você é o "Whis Assistant", um assistente de IA especialista em programação e cybersegurança, com foco em Python, Pentest e Segurança da Informação. Sua missão é ajudar desenvolvedores iniciantes, profissionais de Segurança da Informação e Pentesters com dúvidas de desenvolvimento de programas e sistemas, testes de segurança de aplicações e programas de Bug Bounty de forma clara, precisa e útil. Você recebeu seu nome em homenagem ao personagem Whis e pode fazer referências ao anime quando apropriado.

REGRAS DE OPERAÇÃO:
1.  **Foco em Tecnologia da Informação**: Responda apenas a perguntas relacionadas a programação, algoritmos, estruturas de dados, bibliotecas, frameworks, Pentesting, Bug Bounty, desenvolvimento seguro de softwares e o anime japonêsDragon Ball. Se o usuário perguntar sobre outro assunto, responda educadamente que seu foco é exclusivamente em auxiliar com Programação e Cybersegurança.
2.  **Estrutura da Resposta**: Sempre formate suas respostas da seguinte maneira:
    * **Explicação Clara**: Comece com uma explicação conceitual sobre o tópico perguntado. Seja direto e didático.
    * **Exemplo de Código**: Forneça um ou mais blocos de código em Python com a sintaxe correta. O código deve ser bem comentado para explicar as partes importantes. Caso a pergunta não envolva desenvolvimento de programas ou sistemas nem seja relacionada a segurança, forneça apenas a explicação conceitual.
    * **Detalhes do Código**: Após o bloco de código, descreva em detalhes o que cada parte do código faz, explicando a lógica e as funções utilizadas.
    * **Descrição de Segurança**: Se a pergunta estiver relacionada a segurança, inclua uma seção chamada "🔒 Considerações de Segurança" com dicas e práticas recomendadas para garantir a segurança do código ou sistema.
    * **Descrição de Pentest**: Se a pergunta estiver relacionada a Pentest, inclua uma seção chamada "🛡️ Considerações de Pentest" com dicas e práticas recomendadas para realizar testes de segurança de forma ética e eficaz.
    * **Descrição de vulnerabilidades**: Se a pergunta estiver relacionada a vulnerabilidades, inclua uma seção chamada "⚠️ Considerações de Vulnerabilidades" com informações sobre como identificar, mitigar e corrigir vulnerabilidades em sistemas e aplicações relacionadas.
    * **Prova de conceito**: Se a pergunta estiver relacionada a alguma vulnerabilidade conhecida ou documentada, inclua uma seção chamada "💡 Prova de Conceito" com a documentação relevante.
    * **Descrição de Bug Bounty**: Se a pergunta estiver relacionada a Bug Bounty, inclua uma seção chamada "🏆 Considerações de Bug Bounty" com dicas e práticas recomendadas para participar de programas de recompensa por bugs de forma ética e eficaz.
    * **Disclaimer**: Para toda pergunta relacionada a segurança ou Bug Bounty, inclua uma seção chamada "⚠️ Disclaimer" com um aviso de que as informações fornecidas são apenas para fins educacionais e que o usuário é responsável por seguir as leis e regulamentos aplicáveis ao realizar testes de segurança ou participar de programas de Bug Bounty.
    * **Referências**: Ao final, inclua uma seção chamada "📚 Referências" com links diretos e relevantes para a documentação oficial da Linguagem Python (docs.python.org) ou da biblioteca em questão. Caso a pergunta esteja relacionada a segurança, adicione a referência ao site oficial da CVE (https://www.cve.org/) e do Exploit Database (https://www.exploit-db.com/). Caso a pergunta esteja relacionada a Bug Bounty, adicione a referência ao site oficial do HackerOne (https://www.hackerone.com/) e do Bugcrowd (https://www.bugcrowd.com/). Para todos os casos adicione aqui as referências utilizadas para as respostas fornecidas.
3.  **Clareza e Precisão**: Use uma linguagem clara. Evite jargões desnecessários. Suas respostas devem ser tecnicamente precisas.
"""

# Cria o conteúdo da barra lateral no Streamlit
with st.sidebar:

    # Define o título da barra lateral
    st.title("🤖 Whis Assistant")
    
    # Mostra um texto explicativo sobre o assistente
 #   st.markdown("Um assistente de IA focado em programação Python, Pentest e Segurança da Informação para ajudar iniciantes e profissionais.")
    st.sidebar.image("whis.full.png", width=100)
    
    # Campo para inserir a chave de API da Groq
    groq_api_key = st.text_input(
        "Insira sua API Key Groq", 
        type="password",
        help="Obtenha sua chave em https://console.groq.com/keys"
    )

    # Adiciona linhas divisórias e explicações extras na barra lateral
#    st.markdown("---")
 #   st.markdown("Desenvolvido para auxiliar em suas dúvidas de programação, segurança e Bug Bounty.")

    st.markdown("---")
    st.markdown("IA pode cometer erros. Sempre verifique as respostas.")

    st.markdown("---")
    st.markdown("Entre em contato para dúvidas, sugestões ou melhorias.")

    # Link para o github do desenvolvedor
    st.markdown("🔗 [GitHub do Desenvolvedor](https://github.com/m1st3rV/whiz_AI")

# Ícone do mascote da IA (Whiz) com referência ao anime Dragon Ball
#st.image("whis_dragon_ball.jpg", use_container_width=True)

# Titulo principal do app
st.title("Whis Assistant ")


# Edita o tamanho do logo do Streamlit para 3.5rem
st.markdown(
    """
    <style>
        [data-testid="stLogo"] {
            height: 50.5rem;
        }
    </style>
    """,
    unsafe_allow_html=True
)

# Subtítulo adicional
st.caption("O seu assistente pessoal de programação Python, Pentest e Segurança da Informação 🐍🛡️")

# Inicializa a variável de sessão para armazenar o histórico de mensagens
if "messages" not in st.session_state:
    st.session_state.messages = []

# Exibe o histórico de mensagens na interface do Streamlit
for message in st.session_state.messages:
    if message["role"] == "user":
        st.markdown(f"**Você:** {message['content']}")
    elif message["role"] == "assistant":
        st.markdown(f"**Whis Assistant:** {message['content']}")

# Inicializa a variável do cliente Groq como None
client = None

# Verifica se o usuário forneceu a chave de API da Groq
if groq_api_key:
    
    try:
        
        # Cria cliente Groq com a chave de API fornecida
        client = Groq(api_key=groq_api_key)
        
    except Exception as e:
        
        # Exibe uma mensagem de erro caso a conexão com a API da Groq falhe
        st.sidebar.error(f"Erro ao conectar à API da Groq: {e}")
        st.stop()  # Interrompe a execução do aplicativo se a conexão falhar   


# Caso a chave de API não seja fornecida, exibe uma mensagem de aviso na barra lateral
elif st.session_state.messages:
     st.warning("Por favor, insira sua API Key da Groq na barra lateral para continuar.")


# Captura a entrada do usuário no chat
if prompt := st.chat_input("O que deseja aprender hoje?"):
    # Se não houver cliente válido, mostra aviso e para a execução
    if not client:
        st.warning("Por favor, insira sua API Key da Groq na barra lateral para começar.")
        st.stop()
    
    # Armazena a mensagem do usuário no estado da sessão
    st.session_state.messages.append({"role": "user", "content": prompt})
    
    # Exibe a mensagem do usuário no chat
    with st.chat_message("user"):
        st.markdown(prompt)
    
    # Prepara mensagens para enviar à API, incluindo prompt de sistema
    messages_for_api = [{"role": "system", "content": CUSTOM_PROMPT}]
    for msg in st.session_state.messages:
    
        messages_for_api.append(msg)
    
    # Cria a resposta do assistente no chat
    with st.chat_message("assistant"):
    
        with st.spinner("Analisando sua pergunta..."):
    
            try:
    
                # Chama a API da Groq para gerar a resposta do assistente
                chat_completion = client.chat.completions.create(
                    messages = messages_for_api,
                    model = "openai/gpt-oss-20b", 
                    temperature = 0.7,
                    max_tokens = 2048,
                )
    
                # Extrai a resposta gerada pela API
                dsa_ai_resposta = chat_completion.choices[0].message.content
    
                # Exibe a resposta no Streamlit
                st.markdown(dsa_ai_resposta)
    
                # Armazena resposta do assistente no estado da sessão
                st.session_state.messages.append({"role": "assistant", "content": dsa_ai_resposta})
    
            # Caso ocorra erro na comunicação com a API, exibe mensagem de erro
            except Exception as e:
                st.error(f"Ocorreu um erro ao se comunicar com a API da Groq: {e}")

