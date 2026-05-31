import streamlit as st  # Corrigido aqui
import plotly.express as px
from processamento import carregar_dados

# Configuração da página
st.set_page_config(page_title="Dashboard de Finanças", page_icon="💰", layout="wide")

# Título Principal da Interface
st.title("📊 Meu Dashboard de Finanças Pessoais")
st.markdown("Bem-vindo ao seu painel financeiro automático desenvolvido em Python.")
st.markdown("---")

try:
    # Carrega os dados usando a função do processamento.py
    df = carregar_dados()
    
    # ==========================================
    # BLOCOS DE MÉTRICAS (TOP CARDs)
    # ==========================================
    total_ganhos = df[df['Valor'] > 0]['Valor'].sum()
    total_gastos = df[df['Valor'] < 0]['Valor'].sum()
    saldo_final = total_ganhos + total_gastos
    
    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.metric(label="Total de Receitas (Ganhos)", value=f"R$ {total_ganhos:,.2f}".replace(",", "X").replace(".", ",").replace("X", "."))
    
    with col2:
        st.metric(label="Total de Despesas (Gastos)", value=f"R$ {abs(total_gastos):,.2f}".replace(",", "X").replace(".", ",").replace("X", "."), delta_color="inverse")
        
    with col3:
        st.metric(label="Saldo Final", value=f"R$ {saldo_final:,.2f}".replace(",", "X").replace(".", ",").replace("X", "."))

    st.markdown("---")

    # ==========================================
    # GRÁFICOS INTERATIVOS
    # ==========================================
    st.subheader("📈 Evolução Financeira no Período")
    
    df_diario = df.groupby('Data')['Valor'].sum().reset_index()
    
    fig_linha = px.line(df_diario, x='Data', y='Valor', title="Fluxo de Caixa Diário",
                        labels={'Valor': 'Valor (R$)', 'Data': 'Data'},
                        markers=True)
    
    # Atualizado para o novo padrão: width="stretch"
    st.plotly_chart(fig_linha, width="stretch")

    st.markdown("---")

    # ==========================================
    # VISUALIZAÇÃO DA TABELA DE DADOS
    # ==========================================
    with st.expander("🔍 Visualizar Extrato Completo Tratado"):
        df_exibicao = df.copy()
        df_exibicao['Data'] = df_exibicao['Data'].dt.strftime('%d/%m/%Y')
        # Atualizado para o novo padrão: width="stretch"
        st.dataframe(df_exibicao, width="stretch")

except FileNotFoundError:
    st.warning("⚠️ Nenhum arquivo de extrato encontrado na pasta `dados_brutos/`. Adicione um arquivo .csv para começar.")
except Exception as e:
    st.error(f"❌ Ocorreu um erro ao carregar a interface: {e}")