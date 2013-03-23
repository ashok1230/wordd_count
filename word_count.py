class strcou:
    def method(self,str):
	self.str=str
	a=self.str.split()
	temp=[]
	for i in a:
	    temp.append(i)
	    if temp.count(i)>1:
		pass
	    else:
		print i,a.count(i)

z=strcou()
z.method("""ashok kumar ashok raju kumar ashok svec tirupathi
krishna puram""")