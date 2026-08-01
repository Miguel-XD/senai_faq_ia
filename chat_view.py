import streamlit as st
from config import PROMPT_SISTEMA_SENAI
from services import calcular_tokens, gerar_resposta_ia

GROQ_KEY = st.secrets.get("GROQ_API_KEY", None)

st.title("Consultor Virtual de Cursos SENAI")

prompt_final = PROMPT_SISTEMA_SENAI

if "base_conhecimento_extra" in st.session_state and st.session_state["base_conhecimento_extra"]:
    prompt_final += f"\n\n Base de Conecimento Adicional (ADMIN): \n{st.session_state['base_conhecimento_extra']}"

if "mensagens" not in st.session_state:
    st.session_state.mensagens = [{"role": "system", "content": prompt_final}]

else:
    st.session_state.mensagens[0] = [{"role": "system", "content": prompt_final}]
    
# Side bar

with st.sidebar:
    st.header("Monitor")
    provedor = st.selectbox("Escolha qual IA irá responder", [
        "GPT-4o Mini (Via G4F)",
        "Llama 3.3 (Via Groq)"])
    temperatura = st.slider("Temperatura: ", 0.0, 1.0, 2.0, step = 0.1)
    
    if "base_conhecimento_extra" in st.session_state: st.success("Base Ativa!!")
    
    st.divider()
    
    if st.button("Limpar Conversa"):
        st.session_state.mensagem = [{
            "role": "user", "content": prompt_final
        }]
        st.rerun()
    
    st.divider()
    
    total_tokens = sum(calcular_tokens(m["content"]) for m in st.session_state.mensagens) 
    st.metric("Tokens de Entrada", f"{total_tokens} tokens")
    
# Exibir histórico
for msg in st.session_state.mensagens:
    if msg["role"] != "system":
        with st.chat_message(msg["role"]):
            st.markdown(msg["content"])
            
# Caixa de Entrada
if prompt := st.chat_input("Faça uma pergunta para a IA ..."):
    with st.chat_message("user"):
        st.markdown(prompt)
        
    st.session_state.mensagens.append({"role": "user", "content": prompt})
    
    with st.chat_message("assistant"):
        with st.spinner("Pensando..."):
            try:
                resposta, tempo = gerar_resposta_ia(provedor, st.session_state.mensagens, GROQ_KEY, temperatura)
                
                st.markdown(resposta)
                st.caption(f"Resposta em {tempo}s")
                
                st.session_state.mensagens.append({
                    "role": "assistante", "content": resposta
                })
                
                st.rerun()
                
            except Exception as e:
                st.error(f"Erro ao conectar com a IA: {e}")