-- CONVERSÃO DE CARACTERES
SELECT F.NM_FUNCIONARIO "ATUAL",
    LOWER(F.NM_FUNCIONARIO) "MINUSCULAS",
    UPPER(F.NM_FUNCIONARIO) "MAIUSCULA",
    INITCAP(F.NM_FUNCIONARIO) "MAIUSCULA/MINUSCULA "
FROM T_SIP_FUNCIONARIO F;

-- MANIPULAÇÃO DE CARACTERES 

-- ASCII() E CHR()
SELECT ASCII('T') "CÓDIGO ASCII",
    CHR(84) "LETRA CORRESPONDENTE"
FROM DUAL;

-- CONCAT()
SELECT CONCAT(CONCAT(F.NR_MATRICULA,'-'), F.NM_FUNCIONARIO)
FROM T_SIP_FUNCIONARIO F;

-- INSTR()
SELECT F.NM_FUNCIONARIO,
    INSTR(F.NM_FUNCIONARIO,'A'),
    INSTR(F.NM_FUNCIONARIO,'JOS'),
    INSTR(F.NM_FUNCIONARIO,'A',3),
    INSTR(F.NM_FUNCIONARIO,'A',3,2)
FROM T_SIP_FUNCIONARIO F;

-- LENGTH()
SELECT F.NM_FUNCIONARIO,
    LENGTH(F.NM_FUNCIONARIO)
FROM T_SIP_FUNCIONARIO F;

-- RPAD() e LPAD()
SELECT F.NM_FUNCIONARIO,
       F.VL_SALARIO_MENSAL,
       RPAD(F.NM_FUNCIONARIO,40),
       RPAD(F.NM_FUNCIONARIO,30,'_'),
       LPAD(F.VL_SALARIO_MENSAL,10,'-')   
  FROM T_SIP_FUNCIONARIO F;