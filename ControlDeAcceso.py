def ControlDeAcceso(credencial):
    SELECT CUE_ID, CUE_PASS, CUE_TUSER
    FROM CUENTA;

    if(CUE_ID == credencial.username && CUE_PASS = credencial.password && CUE_TUSER == 'A')
    {
        return 'Administrador'
    }
    if(CUE_ID == credencial.username && CUE_PASS = credencial.password && CUE_TUSER == 'U')
    {
        return 'Usuario'
    }
    else
        raise ValueError("Account not found")
