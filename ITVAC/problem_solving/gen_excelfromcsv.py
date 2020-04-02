import xlwt

string='''KALAM37228,Pradeep ragul S,1606pradeepragul@gmail.com,9500890076,SNS College of technology
KALAM97445,R KARTHICK,killerfox080101@gmail.com,9361643501,KGISL INSTITUTE OF TECHNOLOGY
KALAM87754,Jananipriya.K,jananipriyak2022@srishakthi.ac.in,8056558432,Sri shakthi institute of engrr and technology
KALAM87754,Jananipriya.K,jananipriyak2022@srishakthi.ac.in,8056558432,Sri shakthi institute of engrr and technology
KALAM10017,Harikrishnan ,krishnanhari86927@gmail.com,6382372782,Srishakthi institute of Engineering and technology
KALAM31031,Mogit.B.T,btmogit@gmail.com,9786594309,Sns college of technology
KALAM69891,Sruthi R,sruthilakshmi2000@gmail.com,9787664635,Karpagam College Of Engineering
KALAM16756,Nithya Chenthoorani.P,nanichenthur@gmail.com,8072291633,Karpagam Collee of Engineering
KALAM59749,S.Kumaresan,kumaresans2022@srishakthi.ac.in,7010173139,Sri Shakthi Institute Of Engineering And Technology
KALAM87195,S.Sasi,sasisiva5253@gmail.com,8940215253,Sri Shakthi institute of engineering and technology
KALAM15245,Harshini V,harshiniv1611@gmail.com,9655440437,sri krishna college of engineering and technology
KALAM50522,Janani sree.G,18tuit039@skct.edu.in,9566437182,Sri Krishna college of technology
KALAM30696,B.Manikandan,manihackers62@gmail.com,7502953166,SNS College of technology
KALAM25104,Godwin Daniel.V,godwindaniel2001@gmail.com,6369909598,KGISL Institute of Technology
KALAM49537,Blesson G,blessondaniel8@gmail.com,9043541643,Sri shakthi institute of engineering and technology
KALAM21962,T.NAVEENKUMAR,naveencsemkce@gmail.com,9043263100,M.kumarasamy college of engineering,karur
KALAM19083,Mohanraj.M,mohanrajmanoharan2001@gmail.com,7904591843,M.kumarasamy college of engineering
KALAM13660,Prasanth S,prasanthsubramani2000@gmail.com,7397647181,M.kumarasamy college of engineering
KALAM85282,Nantha Gopal K,nanthagopalksa@gmail.com,6379154616,M.kumarasamy college of engineering
KALAM13280,Nandhakumar K,knandhu744fe@gmail.com,9791256969,M.Kumarasamy College of Engineering
KALAM43063,Saravanan,saravanaalone007@gmail.com,6379176981,M.kumarasamy college of engineering
KALAM79572,Kalaiselvan,kalaiselvan1360@gmail.com,6382510382,M. Kumarasamy college of engineering
KALAM92478,Abinash.S,abinashsece2021@srishakthi.ac.in,8825907698,Sri shakthi institute of engineering and technology
KALAM35998,Deepakk,Sddeepakk0806@gmail.com,9788671237,Sri Shakthi institute of engineering and technology
KALAM24262,Raja,rajakirupa007@gmail.com,+919994917699,Karpagam college of engineering
KALAM27980,Prabhakaran S,prabhu311020@gmail.com,+917904876026,Karpagam college of engineering
KALAM55111,Gokul srinath,mgokul06@gmail.com,9790256987,Sri shakthi institute of engineering and technology
KALAM55111,Gokul srinath,mgokul06@gmail.com,9790256987,Sri shakthi institute of engineering and technology
KALAM27214,Gowthaman M,gowthamankyo12@gmail.com,9566615244,Sri shakthi institute of engineering and technology
KALAM27214,Gowthaman M,gowthamankyo12@gmail.com,9566615244,Sri shakthi institute of engineering and technology
KALAM92615,Sabitha Begam.s,sabithabegam2017@gmail.com,8778596395,Vivekananda college of engineering for women
KALAM25008,J Reena,reena0809daisy@gmail.com,6381639076,Vivekananda college of engineering for women (autonomous)
KALAM36273,M.monisha,kiruthimonisha@gmail.com,9361209850,Vivekananda college of engineering for women
KALAM13091,Pooja,poojajogan@gmail.com,8778014696,Karpagam College of Engineering
KALAM89565,V.P.Milesh Kummaar ,mileshkummaar2000@gmail.com,9842453736,Karpagam College of Engineering
KALAM42372,Anil Kumar,anilhoney893@gmail.com,6381859097,RVS Technical Campus
KALAM42372,Anil Kumar,anilhoney893@gmail.com,6381859097,RVS Technical Campus
KALAM27289,Himanshu Ranjan,hranjan742@gmail.com,8248097181,Rvs technical campus, Coimbatore'''




style0 = xlwt.easyxf('font: name Times New Roman, color-index red, bold on',
    num_format_str='#,##0.00')
str=string.split('\n')
wb = xlwt.Workbook()
ws = wb.add_sheet('CodeFlix')
n=0
for a,b,c,d,e in [k for k in sorted([i.split(',')[:5] for i in set(str)],key=lambda x:x[4])]:
    ws.write(n,0,b)
    ws.write(n,1,e)
    n+=1
wb.save('codeflix.xls')
