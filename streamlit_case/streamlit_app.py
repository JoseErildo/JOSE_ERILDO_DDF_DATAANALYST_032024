import streamlit as st
import jsonlines

# Função para ler o arquivo JSONL e extrair os dados
def ler_arquivo_jsonl(caminho_arquivo):
    dados = []
    with jsonlines.open(caminho_arquivo) as reader:
        for linha in reader:
            dados.append(linha)
    return dados

# Função para contar o total de produtos cadastrados
def contar_total_produtos(dados):
    return len(dados)

# Caminho para o arquivo JSONL
caminho_arquivo = "modelo.jsonl"

# Lendo os dados do arquivo JSONL
dados = ler_arquivo_jsonl(caminho_arquivo)

# Adicionando uma imagem acima de tudo
st.image("https://storage.googleapis.com/cubo-platform.appspot.com/startups/1650308876249-4dl152kp.png", use_column_width=True)

# Criando duas colunas para posicionar os elementos
col1, col2 = st.columns([2, 3])

# Seção do "visual big number" e da pesquisa por produto
with col1:
    st.title("Dashboard de Produtos", anchor='center')
    st.markdown("""<div style="background-color:#000000;padding:20px;border-radius:5px;"> 
                    <h1 style="text-align:center;font-size:30px;">Nº Produtos: {}</h1>
                    </div>""".format(contar_total_produtos(dados)), unsafe_allow_html=True)

# Mostrando os produtos em uma tabela
with col2:
    st.title("Lista de Produtos Cadastrados")
    for idx, produto in enumerate(dados):
        st.write(f"**Produto {idx+1}**")
        st.write(f"ID: {produto['docid']}")
        st.write(f"Título do Produto: {produto['title']}")
        st.write(f"Descrição: {produto['text']}")
        st.write("")
