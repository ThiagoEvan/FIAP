-- COUNT()
SELECT * FROM T_SIP_FUNCIONARIO;
SELECT COUNT(*) FROM T_SIP_FUNCIONARIO;

SELECT * FROM T_SIP_PROJETO;
SELECT COUNT(DT_TERMINO) FROM T_SIP_PROJETO;

  -- Contando as linhas onde não há data do termino do projeto
SELECT COUNT(CD_PROJETO) 
    FROM T_SIP_PROJETO
    WHERE DT_TERMINO IS NULL;

  -- COUNT - cláusula DISTINCT
SELECT * FROM T_SIP_IMPLANTACAO;

SELECT COUNT(CD_PROJETO)
  FROM T_SIP_IMPLANTACAO;

 SELECT COUNT(DISTINCT CD_PROJETO)
  FROM T_SIP_IMPLANTACAo;

-- SUM()
SELECT * FROM T_SIP_FUNCIONARIO;
SELECT SUM(VL_SALARIO_MENSAL) FROM T_SIP_FUNCIONARIO;

-- AVG() - Média Aritmética
SELECT AVG(VL_SALARIO_MENSAL) FROM T_SIP_FUNCIONARIO;

-- MIN()
SELECT MIN(VL_SALARIO_MENSAL) FROM T_SIP_FUNCIONARIO;