class InitPage:
    login_success_date = [
        {"username": "lanpangzi", "pwd": "admin", "expect": "Student Login"},
        {"username": "lanpangzi", "pwd": "admin", "expect": "Student Login12345"}
    ]

    login_error_data = [
        #  id:msg_uname
        {"username": "lanpangzi", "pwd": "1234567", "expect": "账户名错误或密码错误!别瞎弄!"},
        {"username": "lanpangz", "pwd": "admin", "expect": "账户名错误或密码错误!别瞎弄!"}
    ]
    
    login_kong_data = [
        {'username':"lanpangzi","pwd":"","expect":"账户不能为空！"},
        {"username":"","pwd":"admin","expect":"密码不能为空！"},
    ]









