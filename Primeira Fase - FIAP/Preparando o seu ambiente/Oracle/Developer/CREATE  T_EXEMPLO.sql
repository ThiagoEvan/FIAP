CREATE TABLE T_EXEMPLO_TESTE (

    CD_TESTE    NUMBER(3) NOT NULL,
    NM_TESTE    VARCHAR2(40) NOT NULL,

    CONSTRAINT T_EXEMPLO_TESTE_PK PRIMARY KEY ( CD_TESTE )

    ENABLE

);

ROLLBACK;