# angr 符号执行 #

### 安装 ###

在 Ubuntu 上，首先我们应该安装所有的编译所需要的依赖环境：
`$ sudo apt install python-dev libffi-dev build-essential virtualenvwrapper`

强烈建议在虚拟环境中安装 angr，因为有几个 angr 的依赖（比如z3）是从他们的原始库中 fork 而来，如果你已经安装了 z3,那么肯定不希望 angr 的依赖覆盖掉官方的共享库，开一个隔离的环境就好了：

修改 `~/.bashrc`：

    export WORKON_HOME=~/.environments
	source /usr/local/bin/virtualenvwrapper.sh


`source ~/.bashrc` 使.bashrc生效

	$ mkvirtualenv angr
	$ sudo pip install angr

----------

## 使用 ##

给个例子：
 CodegateCTF2017 angrybird
	
	#!/usr/bin/env python

	import angr
	
	main  = 0x004007da
	find  = 0x00404fda  # leave;ret
	avoid = 0x00400590  # puts@plt
	
	p = angr.Project('./angrybird_org')
	init = p.factory.blank_state(addr=main)
	pg = p.factory.simgr(init, threads=4)
	ex = pg.explore(find=find, avoid=avoid)
	
	final = ex.found[0].state
	flag = final.posix.dumps(0)
	
	print "Flag:", final.posix.dumps(1)


以后再更。

#### Bug ####

多线程有个bug：

    pg = p.factory.simgr(init, threads=4)
    
会报错，故只能使用单线程。