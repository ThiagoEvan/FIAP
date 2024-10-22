SELECT NM_FUNCIONARIO, VL_SALARIO_MENSAL
    FROM T_SIP_FUNCIONARIO
    WHERE VL_SALARIO_MENSAL >  ( 
                                    SELECT VL_SALARIO_MENSAL
                                    FROM T_SIP_FUNCIONARIO
                                    WHERE NR_MATRICULA = 12348
                                )
;