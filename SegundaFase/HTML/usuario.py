import streamlit as st

# Dados do usuário
def usuario():
    name = st.text_input("Nome do usuário: ")
    age = st.number_input("Idade: ", value=0, step=1, min_value= 0, max_value= 150)
    return name, age

def principal():
    st.title("Formulário")
    st.subheader("Por favor, informe seus dados abaixo: ")

    # Coleta dos dados usando a função usuario
    name, age = usuario()

    # Cria uma lista com as categorias dos estados civis
    st.write("Selecione o estado civil do usuário:")
    category = st.selectbox("Estado civil", ("Solteiro","Casado","Viúvo","Divorciado"))

    # Cria um botão para enviar os dados 
    submit = st.button("Enviar")

    if submit:
        st.write("Dados enviados com sucesso.")

if __name__ =="__main__":
    principal()