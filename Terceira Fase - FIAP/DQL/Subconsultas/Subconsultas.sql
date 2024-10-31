SELECT NM_FUNCIONARIO, VL_SALARIO_MENSAL
    FROM T_SIP_FUNCIONARIO
    WHERE VL_SALARIO_MENSAL >  ( 
                                    SELECT VL_SALARIO_MENSAL
                                    FROM T_SIP_FUNCIONARIO
                                    WHERE NR_MATRICULA = 12348
                                )
;

SELECT NM_FUNCIONARIO, VL_SALARIO_MENSAL
    FROM T_SIP_FUNCIONARIO
    WHERE VL_SALARIO_MENSAL > (
                                    SELECT AVG(VL_SALARIO_MENSAL)
                                    FROM T_SIP_FUNCIONARIO
                                )
;

SELECT F.NR_MATRICULA,
       F.NM_FUNCIONARIO,
       F.DT_ADMISSAO,
       RESFUNC.QTDELOCACAO
FROM T_SIP_FUNCIONARIO F,
                        (
                            SELECT NR_MATRICULA,
                                   COUNT(NR_MATRICULA) "QTDELOCACAO"
                            FROM T_SIP_IMPLANTACAO
                            GROUP BY NR_MATRICULA
                        ) RESFUNC

WHERE F.NR_MATRICULA = RESFUNC.NR_MATRICULA;

-- CRIANDO TABELAS ATRAVÉS DA SUBCONSULTAS

CREATE TABLE T_SIP_FUNC_DEV AS
            SELECT * FROM T_SIP_FUNCIONARIO WHERE CD_DEPTO = 2;

SELECT * FROM T_SIP_FUNC_DEV;
