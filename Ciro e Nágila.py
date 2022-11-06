i=1
while i<1000:
    print("[1]-Cadastro")
    opcao=int(input("Digite a opção: "))
    if opcao==1:
        print("===============================================================")
        nome=input("Digite seu nome: ")
        cpf=input("Digite o seu CPF: ")
        email=input("Digite o seu email: ")
        senha=input("Digite a sua senha: ")
        user=input("Digite o seu usuário: ")
        print("===============================================================")
            
        conf=int(input("[1]-Sim\n[2]-Não\nConfirma o seu cadastro? "))
        if conf==1:
            i=1
            while i<1000:
                print("===============================================================")
                print("OPÇÕES DO PROGRAMA")
                print("[1]-Ver dados")
                print("[2]-Atualizar dados")
                print("[3]-Deletar dados")
                print("[4]-Sair")
                opcad=int(input("Digite a opção: "))
                print("===============================================================")
            
                if opcad==1:
                    print("VER SEUS DADOS\nNome: %s\nCPF: %s\nEmail: %s\nSenha: %s\nUsuário: %s" %(nome, cpf, email, senha, user))
                    print("ㅤ\n")
                    print("VOLTANDO AO MENU  PRINCIPAL")
                            
                elif opcad==2:
                    atu=int(input("[1]-Sim\n[2]-Não\nDeseja atualizar seus dados? "))
                    print("===============================================================")
                    if atu==1:
                        print("SEUS DADOS\nNome: %s\nCPF: %s\nEmail: %s\nSenha: %s\nUsuário: %s" %(nome, cpf, email, senha, user))
                        print("ㅤ\n")
                        atop=int(input("[1]-Apenas 1\n[2]-Todos os dados\nDeseja atualizar apenas uma informação ou todos os dados? "))
                        if atop==1:
                            print("[1]-Nome")
                            print("[2]-CPF")
                            print("[3]-Email")
                            print("[4}-Senha")
                            print("[5]-Usuário")
                            atop1=int(input("Digite a opção: "))
                            if atop1==1:
                                nome1=input("Digite seu nome: ")
                                print("CPF: %s\nEmail: %s\nSenha: %s\nUsuário: %s" %(cpf, email, senha, user))
                            elif atop1==2:
                                print("Nome: %s" %nome)
                                cpf=input("Digite o seu CPF: ")
                                print("Email: %s\nSenha: %s\nUsuário: %s\n" %(email,senha,user))
                            elif atop1==3:
                                print("Nome: %s\nCPF: %s" %(nome, cpf))
                                email=input("Digite o seu email: ")
                                print("Senha: %s\nUsuário: %s" %(senha, user))
                            elif atop==4:
                                print("Nome: %s\nCPF: %s\nEmail: %s" %(nome, cpf, email))
                                senha=input("Digite a sua senha: ")
                                print("Usuário: %s" %user)
                            elif atop==5:
                                print("Nome: %s\nCPF: %s\nEmail: %s\nSenha: %s" %(nome, cpf, email, senha))
                                user1=input("Digite o seu usuário: ")
                            else:
                                print("ESCOLHA APENAS OS NÚMEROS INDICADOS")
                        
                        
                        
                        
                            print("ㅤ\n")
                            print("SEUS NOVOS DADOS\nNome: %s\nCPF: %s\nEmail: %s\nSenha: %s\nUsuário: %s" %(nome, cpf, email, senha, user))
                            print("===============================================================")
                            print("===============================================================")
                            print("OPÇÕES DO PROGRAMA")
                            print("[1]-Ver dados")
                            print("[2]-Atualizar dados")
                            print("[3]-Deletar dados")
                            print("[4]-Sair")
                            opcad=int(input("Digite a opção: "))
                            print("===============================================================")
                        
                            if opcad==1:
                                print("VER SEUS DADOS\nNome: %s\nCPF: %s\nEmail: %s\nSenha: %s\nUsuário: %s" %(nome, cpf, email, senha, user))
                                print("ㅤ\n")
                                print("VOLTANDO AO MENU  PRINCIPAL")
                                        
                            if opcad==2:
                                atu=int(input("[1]-Sim\n[2]-Não\nDeseja atualizar seus dados? "))
                                print("===============================================================")
                        elif atop==2:
                            print("SEUS DADOS\nNome: %s\nCPF: %s\nEmail: %s\nSenha: %s\nUsuário: %s" %(nome, cpf, email, senha, user))
                            print("ㅤ\n")
                            nome=input("Digite seu nome: ")
                            cpf=input("Digite o seu CPF: ")
                            email=input("Digite o seu email: ")
                            senha=input("Digite a sua senha: ")
                            user=input("Digite o seu usuário: ")
                            print("ㅤ\n")
                            print("SEUS NOVOS DADOS\nNome: %s\nCPF: %s\nEmail: %s\nSenha: %s\nUsuário: %s" %(nome, cpf, email, senha, user))
                            
                        else:
                            print("ESCOLHA APENAS 1 OU 2")
                        
                        
                            i=i+1
                        
                            
                elif opcad==3:
                    delet=int(input("[1]-Sim\n[2]-Não\nDeseja deletar seus dados? "))
                    if delet==1:
                        print("DELETANDO SEUS DADOS...")
                        print("===============================================================")
                        i=1
                        while i<1000:
                            print("[1]-Cadastro")
                            opcao=int(input("Digite a opção: "))
                            if opcao==1:
                                print("===============================================================")
                                nome=input("Digite seu nome: ")
                                cpf=input("Digite o seu CPF: ")
                                email=input("Digite o seu email: ")
                                senha=input("Digite a sua senha: ")
                                user=input("Digite o seu usuário: ")
                                print("===============================================================")
                                    
                                conf=int(input("[1]-Sim\n[2]-Não\nConfirma o seu cadastro? "))
                                if conf==1:
                                    i=1
                                    while i<1000:
                                        print("===============================================================")
                                        print("OPÇÕES DO PROGRAMA")
                                        print("[1]-Ver dados")
                                        print("[2]-Atualizar dados")
                                        print("[3]-Deletar dados")
                                        print("[4]-Sair")
                                        opcad=int(input("Digite a opção: "))
                                        print("===============================================================")
                                    
                                        if opcad==1:
                                            print("VER SEUS DADOS\nNome: %s\nCPF: %s\nEmail: %s\nSenha: %s\nUsuário: %s" %(nome, cpf, email, senha, user))
                                            print("ㅤ\n")
                                            print("VOLTANDO AO MENU  PRINCIPAL")
                                                    
                                        elif opcad==2:
                                            atu=int(input("[1]-Sim\n[2]-Não\nDeseja atualizar seus dados? "))
                                            print("===============================================================")
                                            if atu==1:
                                                print("SEUS DADOS\nNome: %s\nCPF: %s\nEmail: %s\nSenha: %s\nUsuário: %s" %(nome, cpf, email, senha, user))
                                                print("ㅤ\n")
                                                atop=int(input("[1]-Apenas 1\n[2]-Todos os dados\nDeseja atualizar apenas uma informação ou todos os dados? "))
                                                if atop==1:
                                                    print("[1]-Nome")
                                                    print("[2]-CPF")
                                                    print("[3]-Email")
                                                    print("[4}-Senha")
                                                    print("[5]-Usuário")
                                                    atop1=int(input("Digite a opção: "))
                                                    if atop1==1:
                                                        nome1=input("Digite seu nome: ")
                                                        print("CPF: %s\nEmail: %s\nSenha: %s\nUsuário: %s" %(cpf, email, senha, user))
                                                    elif atop1==2:
                                                        print("Nome: %s" %nome)
                                                        cpf=input("Digite o seu CPF: ")
                                                        print("Email: %s\nSenha: %s\nUsuário: %s\n" %(email,senha,user))
                                                    elif atop1==3:
                                                        print("Nome: %s\nCPF: %s" %(nome, cpf))
                                                        email=input("Digite o seu email: ")
                                                        print("Senha: %s\nUsuário: %s" %(senha, user))
                                                    elif atop==4:
                                                        print("Nome: %s\nCPF: %s\nEmail: %s" %(nome, cpf, email))
                                                        senha=input("Digite a sua senha: ")
                                                        print("Usuário: %s" %user)
                                                    elif atop==5:
                                                        print("Nome: %s\nCPF: %s\nEmail: %s\nSenha: %s" %(nome, cpf, email, senha))
                                                        user1=input("Digite o seu usuário: ")
                                                    else:
                                                        print("ESCOLHA APENAS OS NÚMEROS INDICADOS")
                                                
                                                
                                                
                                                
                                                    print("ㅤ\n")
                                                    print("SEUS NOVOS DADOS\nNome: %s\nCPF: %s\nEmail: %s\nSenha: %s\nUsuário: %s" %(nome, cpf, email, senha, user))
                                                    print("===============================================================")
                                                    print("===============================================================")
                                                    print("OPÇÕES DO PROGRAMA")
                                                    print("[1]-Ver dados")
                                                    print("[2]-Atualizar dados")
                                                    print("[3]-Deletar dados")
                                                    print("[4]-Sair")
                                                    opcad=int(input("Digite a opção: "))
                                                    print("===============================================================")
                                                
                                                    if opcad==1:
                                                        print("VER SEUS DADOS\nNome: %s\nCPF: %s\nEmail: %s\nSenha: %s\nUsuário: %s" %(nome, cpf, email, senha, user))
                                                        print("ㅤ\n")
                                                        print("VOLTANDO AO MENU  PRINCIPAL")
                                                                
                                                    if opcad==2:
                                                        atu=int(input("[1]-Sim\n[2]-Não\nDeseja atualizar seus dados? "))
                                                        print("===============================================================")
                                                elif atop==2:
                                                    print("SEUS DADOS\nNome: %s\nCPF: %s\nEmail: %s\nSenha: %s\nUsuário: %s" %(nome, cpf, email, senha, user))
                                                    print("ㅤ\n")
                                                    nome=input("Digite seu nome: ")
                                                    cpf=input("Digite o seu CPF: ")
                                                    email=input("Digite o seu email: ")
                                                    senha=input("Digite a sua senha: ")
                                                    user=input("Digite o seu usuário: ")
                                                    print("ㅤ\n")
                                                    print("SEUS NOVOS DADOS\nNome: %s\nCPF: %s\nEmail: %s\nSenha: %s\nUsuário: %s" %(nome, cpf, email, senha, user))
                                                    
                                                else:
                                                    print("ESCOLHA APENAS 1 OU 2")
                                                
                                                
                                                i=i+1
                                                
                                                    
                                        elif opcad==3:
                                            delet=int(input("[1]-Sim\n[2]-Não\nDeseja deletar seus dados? "))
                                            if delet==1:
                                                print("DELETANDO SEUS DADOS...")
                                                print("===============================================================")
                                                i=i+1
                                            
                    
                            
                    elif delet==2:
                        print("VOLTANDO AO MENU")
                    else:
                        print("ESCOLHA APENAS 1 OU 2")
                    
        
        
                
                
                elif opcad==4:
                    sair=int(input("[1]-Sim\n[2]-Não\nDeseja sair? "))
                    print("SAINDO...")
                    i=1
                    while i<1000:
                        print("[1]-Cadastro")
                        print("[2]-Login")
                        opcao=int(input("Digite a opção: "))
                        if opcao==1:
                            print("===============================================================")
                            nome=input("Digite seu nome: ")
                            cpf=input("Digite o seu CPF: ")
                            email=input("Digite o seu email: ")
                            senha=input("Digite a sua senha: ")
                            user=input("Digite o seu usuário: ")
                            print("===============================================================")
                                
                            conf=int(input("[1]-Sim\n[2]-Não\nConfirma o seu cadastro? "))
                            if conf==1:
                                i=1
                                while i<1000:
                                    print("===============================================================")
                                    print("[1]-Cadastro")
                                    opcao=int(input("Digite a opção: "))
                                    if opcao==1:
                                        print("===============================================================")
                                        nome=input("Digite seu nome: ")
                                        cpf=input("Digite o seu CPF: ")
                                        email=input("Digite o seu email: ")
                                        senha=input("Digite a sua senha: ")
                                        user=input("Digite o seu usuário: ")
                                        print("===============================================================")
                                            
                                        conf=int(input("[1]-Sim\n[2]-Não\nConfirma o seu cadastro? "))
                                        if conf==1:
                                            i=1
                                            while i<1000:
                                                print("===============================================================")
                                                print("OPÇÕES DO PROGRAMA")
                                                print("[1]-Ver dados")
                                                print("[2]-Atualizar dados")
                                                print("[3]-Deletar dados")
                                                print("[4]-Sair")
                                                opcad=int(input("Digite a opção: "))
                                                print("===============================================================")
                                            
                                                if opcad==1:
                                                    print("VER SEUS DADOS\nNome: %s\nCPF: %s\nEmail: %s\nSenha: %s\nUsuário: %s" %(nome, cpf, email, senha, user))
                                                    print("ㅤ\n")
                                                    print("VOLTANDO AO MENU  PRINCIPAL")
                                                            
                                                elif opcad==2:
                                                    atu=int(input("[1]-Sim\n[2]-Não\nDeseja atualizar seus dados? "))
                                                    print("===============================================================")
                                                    if atu==1:
                                                        print("SEUS DADOS\nNome: %s\nCPF: %s\nEmail: %s\nSenha: %s\nUsuário: %s" %(nome, cpf, email, senha, user))
                                                        print("ㅤ\n")
                                                        atop=int(input("[1]-Apenas 1\n[2]-Todos os dados\nDeseja atualizar apenas uma informação ou todos os dados? "))
                                                        if atop==1:
                                                            print("[1]-Nome")
                                                            print("[2]-CPF")
                                                            print("[3]-Email")
                                                            print("[4}-Senha")
                                                            print("[5]-Usuário")
                                                            atop1=int(input("Digite a opção: "))
                                                            if atop1==1:
                                                                nome1=input("Digite seu nome: ")
                                                                print("CPF: %s\nEmail: %s\nSenha: %s\nUsuário: %s" %(cpf, email, senha, user))
                                                            elif atop1==2:
                                                                print("Nome: %s" %nome)
                                                                cpf=input("Digite o seu CPF: ")
                                                                print("Email: %s\nSenha: %s\nUsuário: %s\n" %(email,senha,user))
                                                            elif atop1==3:
                                                                print("Nome: %s\nCPF: %s" %(nome, cpf))
                                                                email=input("Digite o seu email: ")
                                                                print("Senha: %s\nUsuário: %s" %(senha, user))
                                                            elif atop==4:
                                                                print("Nome: %s\nCPF: %s\nEmail: %s" %(nome, cpf, email))
                                                                senha=input("Digite a sua senha: ")
                                                                print("Usuário: %s" %user)
                                                            elif atop==5:
                                                                print("Nome: %s\nCPF: %s\nEmail: %s\nSenha: %s" %(nome, cpf, email, senha))
                                                                user1=input("Digite o seu usuário: ")
                                                            else:
                                                                print("ESCOLHA APENAS OS NÚMEROS INDICADOS")
                                                        
                                                        
                                                        
                                                        
                                                            print("ㅤ\n")
                                                            print("SEUS NOVOS DADOS\nNome: %s\nCPF: %s\nEmail: %s\nSenha: %s\nUsuário: %s" %(nome, cpf, email, senha, user))
                                                            print("===============================================================")
                                                            print("===============================================================")
                                                            print("OPÇÕES DO PROGRAMA")
                                                            print("[1]-Ver dados")
                                                            print("[2]-Atualizar dados")
                                                            print("[3]-Deletar dados")
                                                            print("[4]-Sair")
                                                            opcad=int(input("Digite a opção: "))
                                                            print("===============================================================")
                                                        
                                                            if opcad==1:
                                                                print("VER SEUS DADOS\nNome: %s\nCPF: %s\nEmail: %s\nSenha: %s\nUsuário: %s" %(nome, cpf, email, senha, user))
                                                                print("ㅤ\n")
                                                                print("VOLTANDO AO MENU  PRINCIPAL")
                                                                        
                                                            if opcad==2:
                                                                atu=int(input("[1]-Sim\n[2]-Não\nDeseja atualizar seus dados? "))
                                                                print("===============================================================")
                                                        elif atop==2:
                                                            print("SEUS DADOS\nNome: %s\nCPF: %s\nEmail: %s\nSenha: %s\nUsuário: %s" %(nome, cpf, email, senha, user))
                                                            print("ㅤ\n")
                                                            nome=input("Digite seu nome: ")
                                                            cpf=input("Digite o seu CPF: ")
                                                            email=input("Digite o seu email: ")
                                                            senha=input("Digite a sua senha: ")
                                                            user=input("Digite o seu usuário: ")
                                                            print("ㅤ\n")
                                                            print("SEUS NOVOS DADOS\nNome: %s\nCPF: %s\nEmail: %s\nSenha: %s\nUsuário: %s" %(nome, cpf, email, senha, user))
                                                            
                                                        else:
                                                            print("ESCOLHA APENAS 1 OU 2")
                                                        
                                                        
                                                            i=i+1
                                                        
                                                            
                                                elif opcad==3:
                                                    delet=int(input("[1]-Sim\n[2]-Não\nDeseja deletar seus dados? "))
                                                    if delet==1:
                                                        print("DELETANDO SEUS DADOS...")
                                                        print("===============================================================")
                                                        i=1
                                                        while i<1000:
                                                            print("[1]-Cadastro")
                                                            opcao=int(input("Digite a opção: "))
                                                            if opcao==1:
                                                                print("===============================================================")
                                                                nome=input("Digite seu nome: ")
                                                                cpf=input("Digite o seu CPF: ")
                                                                email=input("Digite o seu email: ")
                                                                senha=input("Digite a sua senha: ")
                                                                user=input("Digite o seu usuário: ")
                                                                print("===============================================================")
                                                                    
                                                                conf=int(input("[1]-Sim\n[2]-Não\nConfirma o seu cadastro? "))
                                                                if conf==1:
                                                                    i=1
                                                                    while i<1000:
                                                                        print("===============================================================")
                                                                        print("OPÇÕES DO PROGRAMA")
                                                                        print("[1]-Ver dados")
                                                                        print("[2]-Atualizar dados")
                                                                        print("[3]-Deletar dados")
                                                                        print("[4]-Sair")
                                                                        opcad=int(input("Digite a opção: "))
                                                                        print("===============================================================")
                                                                    
                                                                        if opcad==1:
                                                                            print("VER SEUS DADOS\nNome: %s\nCPF: %s\nEmail: %s\nSenha: %s\nUsuário: %s" %(nome, cpf, email, senha, user))
                                                                            print("ㅤ\n")
                                                                            print("VOLTANDO AO MENU  PRINCIPAL")
                                                                                    
                                                                        elif opcad==2:
                                                                            atu=int(input("[1]-Sim\n[2]-Não\nDeseja atualizar seus dados? "))
                                                                            print("===============================================================")
                                                                            if atu==1:
                                                                                print("SEUS DADOS\nNome: %s\nCPF: %s\nEmail: %s\nSenha: %s\nUsuário: %s" %(nome, cpf, email, senha, user))
                                                                                print("ㅤ\n")
                                                                                atop=int(input("[1]-Apenas 1\n[2]-Todos os dados\nDeseja atualizar apenas uma informação ou todos os dados? "))
                                                                                if atop==1:
                                                                                    print("[1]-Nome")
                                                                                    print("[2]-CPF")
                                                                                    print("[3]-Email")
                                                                                    print("[4}-Senha")
                                                                                    print("[5]-Usuário")
                                                                                    atop1=int(input("Digite a opção: "))
                                                                                    if atop1==1:
                                                                                        nome1=input("Digite seu nome: ")
                                                                                        print("CPF: %s\nEmail: %s\nSenha: %s\nUsuário: %s" %(cpf, email, senha, user))
                                                                                    elif atop1==2:
                                                                                        print("Nome: %s" %nome)
                                                                                        cpf=input("Digite o seu CPF: ")
                                                                                        print("Email: %s\nSenha: %s\nUsuário: %s\n" %(email,senha,user))
                                                                                    elif atop1==3:
                                                                                        print("Nome: %s\nCPF: %s" %(nome, cpf))
                                                                                        email=input("Digite o seu email: ")
                                                                                        print("Senha: %s\nUsuário: %s" %(senha, user))
                                                                                    elif atop==4:
                                                                                        print("Nome: %s\nCPF: %s\nEmail: %s" %(nome, cpf, email))
                                                                                        senha=input("Digite a sua senha: ")
                                                                                        print("Usuário: %s" %user)
                                                                                    elif atop==5:
                                                                                        print("Nome: %s\nCPF: %s\nEmail: %s\nSenha: %s" %(nome, cpf, email, senha))
                                                                                        user1=input("Digite o seu usuário: ")
                                                                                    else:
                                                                                        print("ESCOLHA APENAS OS NÚMEROS INDICADOS")
                                                                                
                                                                                
                                                                                
                                                                                
                                                                                    print("ㅤ\n")
                                                                                    print("SEUS NOVOS DADOS\nNome: %s\nCPF: %s\nEmail: %s\nSenha: %s\nUsuário: %s" %(nome, cpf, email, senha, user))
                                                                                    print("===============================================================")
                                                                                    print("===============================================================")
                                                                                    print("OPÇÕES DO PROGRAMA")
                                                                                    print("[1]-Ver dados")
                                                                                    print("[2]-Atualizar dados")
                                                                                    print("[3]-Deletar dados")
                                                                                    print("[4]-Sair")
                                                                                    opcad=int(input("Digite a opção: "))
                                                                                    print("===============================================================")
                                                                                
                                                                                    if opcad==1:
                                                                                        print("VER SEUS DADOS\nNome: %s\nCPF: %s\nEmail: %s\nSenha: %s\nUsuário: %s" %(nome, cpf, email, senha, user))
                                                                                        print("ㅤ\n")
                                                                                        print("VOLTANDO AO MENU  PRINCIPAL")
                                                                                                
                                                                                    if opcad==2:
                                                                                        atu=int(input("[1]-Sim\n[2]-Não\nDeseja atualizar seus dados? "))
                                                                                        print("===============================================================")
                                                                                elif atop==2:
                                                                                    print("SEUS DADOS\nNome: %s\nCPF: %s\nEmail: %s\nSenha: %s\nUsuário: %s" %(nome, cpf, email, senha, user))
                                                                                    print("ㅤ\n")
                                                                                    nome=input("Digite seu nome: ")
                                                                                    cpf=input("Digite o seu CPF: ")
                                                                                    email=input("Digite o seu email: ")
                                                                                    senha=input("Digite a sua senha: ")
                                                                                    user=input("Digite o seu usuário: ")
                                                                                    print("ㅤ\n")
                                                                                    print("SEUS NOVOS DADOS\nNome: %s\nCPF: %s\nEmail: %s\nSenha: %s\nUsuário: %s" %(nome, cpf, email, senha, user))
                                                                                    
                                                                                else:
                                                                                    print("ESCOLHA APENAS 1 OU 2")
                                                                                
                                                                                
                                                                                i=i+1
                                                                                
                                                                                    
                                                                        elif opcad==3:
                                                                            delet=int(input("[1]-Sim\n[2]-Não\nDeseja deletar seus dados? "))
                                                                            if delet==1:
                                                                                print("DELETANDO SEUS DADOS...")
                                                                                print("===============================================================")
                                                                                i=i+1
                                                                                i=i+1
                                            
                    
                            
                    
        
        
                
                
                elif opcad==4:
                    sair=int(input("[1]-Sim\n[2]-Não\nDeseja sair? "))
                    print("SAINDO...")
                    i=1
                    while i<1000:
                        print("[1]-Cadastro")
                        opcao=int(input("Digite a opção: "))
                        if opcao==1:
                            print("===============================================================")
                            nome=input("Digite seu nome: ")
                            cpf=input("Digite o seu CPF: ")
                            email=input("Digite o seu email: ")
                            senha=input("Digite a sua senha: ")
                            user=input("Digite o seu usuário: ")
                            print("===============================================================")
                                
                            conf=int(input("[1]-Sim\n[2]-Não\nConfirma o seu cadastro? "))
                            if conf==1:
                                i=1
                                while i<1000:
                                    print("===============================================================")
                                    i=i+1
                    
        
        
        
        
        
        
        
        
        
        

        elif conf==2:
            print("===============================================================")
            print("REVEJA SEUS DADOS")
        else:
            print("ESCOLHA APENAS 1 OU 2")
        
        
        
        
        
        
        
        
        
    else:
        print("===============================================================")
        print("ESCOLHA APENAS 1")
        i=i+1