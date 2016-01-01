Search.setIndex({envversion:46,filenames:["conventions","crypto.abstract","crypto.games","crypto.primitives","crypto.simulator","crypto.tools","design_and_architecture","index","intro","modules","quick_start"],objects:{"crypto.abstract":{block_cipher:[1,0,0,"-"],digital_signature:[1,0,0,"-"],hash_function:[1,0,0,"-"],message_authentication_code:[1,0,0,"-"]},"crypto.abstract.block_cipher":{BlockCipher:[1,3,1,""]},"crypto.abstract.block_cipher.BlockCipher":{decrypt:[1,2,1,""],encrypt:[1,2,1,""]},"crypto.abstract.digital_signature":{DigitalSignature:[1,3,1,""]},"crypto.abstract.digital_signature.DigitalSignature":{key_gen:[1,2,1,""],sign:[1,2,1,""],verify:[1,2,1,""]},"crypto.abstract.hash_function":{HashFunction:[1,3,1,""]},"crypto.abstract.hash_function.HashFunction":{hash:[1,2,1,""]},"crypto.abstract.message_authentication_code":{MAC:[1,3,1,""]},"crypto.abstract.message_authentication_code.MAC":{tag:[1,2,1,""],verify:[1,2,1,""]},"crypto.games":{game:[2,0,0,"-"],game_bind:[2,0,0,"-"],game_cca:[2,0,0,"-"],game_cr:[2,0,0,"-"],game_int_ctxt:[2,0,0,"-"],game_kr:[2,0,0,"-"],game_lr:[2,0,0,"-"],game_prf:[2,0,0,"-"],game_ufcma:[2,0,0,"-"]},"crypto.games.game":{Game:[2,3,1,""]},"crypto.games.game.Game":{finalize:[2,2,1,""],initialize:[2,2,1,""]},"crypto.games.game_bind":{GameBIND:[2,3,1,""]},"crypto.games.game_bind.GameBIND":{finalize:[2,2,1,""],initialize:[2,2,1,""]},"crypto.games.game_cca":{GameCCA:[2,3,1,""]},"crypto.games.game_cca.GameCCA":{dec:[2,2,1,""],lr:[2,2,1,""]},"crypto.games.game_cr":{GameCR:[2,3,1,""]},"crypto.games.game_cr.GameCR":{finalize:[2,2,1,""],initialize:[2,2,1,""]},"crypto.games.game_int_ctxt":{GameINTCTXT:[2,3,1,""]},"crypto.games.game_int_ctxt.GameINTCTXT":{dec:[2,2,1,""],enc:[2,2,1,""],finalize:[2,2,1,""],initialize:[2,2,1,""]},"crypto.games.game_kr":{GameKR:[2,3,1,""]},"crypto.games.game_kr.GameKR":{finalize:[2,2,1,""],fn:[2,2,1,""],initialize:[2,2,1,""]},"crypto.games.game_lr":{GameLR:[2,3,1,""]},"crypto.games.game_lr.GameLR":{finalize:[2,2,1,""],initialize:[2,2,1,""],lr:[2,2,1,""]},"crypto.games.game_prf":{GamePRF:[2,3,1,""]},"crypto.games.game_prf.GamePRF":{finalize:[2,2,1,""],fn:[2,2,1,""],initialize:[2,2,1,""]},"crypto.games.game_ufcma":{GameUFCMA:[2,3,1,""]},"crypto.games.game_ufcma.GameUFCMA":{finalize:[2,2,1,""],initialize:[2,2,1,""],tag:[2,2,1,""],verify:[2,2,1,""]},"crypto.primitives":{AES:[3,1,1,""],AES_I:[3,1,1,""],random_string:[3,1,1,""],random_string_bits:[3,1,1,""],rsa_keygen:[3,1,1,""]},"crypto.simulator":{base_sim:[4,0,0,"-"],bind_sim:[4,0,0,"-"],cca_sim:[4,0,0,"-"],cr_sim:[4,0,0,"-"],ctxt_sim:[4,0,0,"-"],kr_sim:[4,0,0,"-"],lr_sim:[4,0,0,"-"],ufcma_sim:[4,0,0,"-"],world_sim:[4,0,0,"-"]},"crypto.simulator.base_sim":{BaseSim:[4,3,1,""]},"crypto.simulator.bind_sim":{BINDSim:[4,3,1,""]},"crypto.simulator.bind_sim.BINDSim":{compute_advantage:[4,2,1,""],compute_success_ratio:[4,2,1,""],run:[4,2,1,""]},"crypto.simulator.cca_sim":{CCASim:[4,3,1,""]},"crypto.simulator.cca_sim.CCASim":{compute_advantage:[4,2,1,""],compute_success_ratio:[4,2,1,""],run:[4,2,1,""]},"crypto.simulator.cr_sim":{CRSim:[4,3,1,""]},"crypto.simulator.cr_sim.CRSim":{compute_advantage:[4,2,1,""],compute_success_ratio:[4,2,1,""],run:[4,2,1,""]},"crypto.simulator.ctxt_sim":{CTXTSim:[4,3,1,""]},"crypto.simulator.ctxt_sim.CTXTSim":{compute_advantage:[4,2,1,""],compute_success_ratio:[4,2,1,""],run:[4,2,1,""]},"crypto.simulator.kr_sim":{KRSim:[4,3,1,""]},"crypto.simulator.kr_sim.KRSim":{compute_advantage:[4,2,1,""],compute_success_ratio:[4,2,1,""],run:[4,2,1,""]},"crypto.simulator.lr_sim":{LRSim:[4,3,1,""]},"crypto.simulator.lr_sim.LRSim":{compute_advantage:[4,2,1,""],compute_success_ratio:[4,2,1,""],run:[4,2,1,""]},"crypto.simulator.ufcma_sim":{UFCMASim:[4,3,1,""]},"crypto.simulator.ufcma_sim.UFCMASim":{compute_advantage:[4,2,1,""],compute_success_ratio:[4,2,1,""],run:[4,2,1,""]},"crypto.simulator.world_sim":{WorldSim:[4,3,1,""]},"crypto.simulator.world_sim.WorldSim":{compute_advantage:[4,2,1,""],compute_success_ratio:[4,2,1,""],run:[4,2,1,""]},"crypto.tools":{add_int_to_string:[5,1,1,""],egcd:[5,1,1,""],int_to_string:[5,1,1,""],join:[5,1,1,""],modinv:[5,1,1,""],split:[5,1,1,""],string_to_int:[5,1,1,""],xor_strings:[5,1,1,""]},crypto:{"abstract":[1,0,0,"-"],games:[2,0,0,"-"],primitives:[3,0,0,"-"],simulator:[4,0,0,"-"],tools:[5,0,0,"-"]}},objnames:{"0":["py","module","Python module"],"1":["py","function","Python function"],"2":["py","method","Python method"],"3":["py","class","Python class"]},objtypes:{"0":"py:module","1":"py:function","2":"py:method","3":"py:class"},terms:{"_tag":2,"_verifi":2,"byte":[1,2,3],"class":[1,2,4,6],"default":1,"final":[2,8,10],"function":[0,1,2,3,5,6,8,10],"import":[0,1,5,10],"int":[0,5],"long":3,"new":[2,8,10],"null":8,"public":[2,10],"return":[1,2,3,4,5,8],"switch":10,"true":[1,2,4],"while":[8,10],abc:5,abcdef:5,abcdefgh:1,abil:6,abl:2,about:6,abov:[4,10],acc:2,accept:2,access:[0,2],accuraci:8,achiev:8,add:[5,10],add_int_to_str:[0,5],addit:6,adv:4,advantag:[4,6,8,10],adversari:[2,4,6,8,10],aes_i:[0,3],after:10,again:[2,6],against:[1,2,4,6],algorithm:[2,3],all:[0,1,2,4,5,6,7,8],allow:[2,4,6,8,10],almost:2,also:[6,8,10],alwai:2,amaz:8,ani:[1,2,6],anyth:2,api:8,appear:10,approxim:[4,6],arbitrari:8,area:8,arrai:[0,5],assign:[6,8],attack:[2,8],attempt:10,authent:[1,2,6],automat:2,avail:[2,8],base:[2,4,8],basesim:4,becaus:[4,6],been:2,befor:[6,10],behavior:[2,6],behind:[6,8],believ:8,bellar:8,belong:1,below:[0,10],between:[0,2,5,6],bigger:5,bind:[2,4],bindsim:4,bit:3,bitwis:5,blank:[],block:[1,2,6,8],block_len:[1,2],block_siz:5,blockciph:1,both:8,bottom:10,brief:7,built:[6,8],bundl:8,california:8,call:[2,6],callabl:2,can:[1,2,3,6,8,10],candid:2,capabl:8,ccasim:4,central:8,challeng:6,check:[1,2],choic:10,choos:10,chosen:2,cipher:[0,1,2,3,6,8],cipher_text:1,clean:6,click:10,close:6,code:[0,1,6,8,10],collis:2,com:5,combin:2,come:[2,8],command:10,commit:2,common:[0,2,8,10],compel:8,complet:[8,10],compon:[3,8],comput:[4,5,10],compute_advantag:[4,6],compute_success_ratio:4,connect:5,consist:[2,8],construct:[2,8],constructor:[4,6],contain:[3,8,10],continu:10,control:2,convers:0,convert:5,corner:10,correct:[1,2,8,10],correspond:[2,6],could:8,counterpart:6,cours:[7,8],cover:8,creat:6,creation:[6,8],crsim:4,crypto:0,cryptograph:[6,8],cse207:10,cse:8,ctxtsim:4,current:[6,8],custom:[0,8],cypher:2,data:2,debug:10,dec:2,decrypt:[1,2,3,10],decrypted_messag:1,deeper:[6,8],def:5,defin:[2,8],definit:6,deliv:8,deliver:[],demonstr:8,descript:8,determin:2,develop:8,dictionari:3,did:2,diego:8,differ:[4,6,8,10],digit:[1,6],digitalsignatur:1,directori:10,displai:10,dive:6,document:6,doesn:2,doubl:10,down:10,download:[],drill:10,dropbox:10,due:8,each:6,easi:8,easier:8,ecb:3,edit:[],editor:10,egcd:[0,5],either:2,emul:1,enc:2,encount:8,encrypt:[1,2,3],end:[6,10],enforc:2,enter:10,environ:[8,10],equal:2,equat:4,error:8,evalu:2,even:[2,8],everi:[2,10],exact:2,exampl:[1,5,6,8,10],except:8,exercis:8,exist:[5,10],expand:8,expens:4,explain:[6,8],explan:7,exploit:8,explor:8,expon:3,expos:[2,6],ext:0,extend:5,extens:6,factor:[2,3],failur:4,fals:[1,2,4],fewer:4,file:10,find:7,finish:6,first:[3,5,10],floor:3,focu:10,folder:[6,10],follow:[7,8,10],forgeri:2,form:8,formal:[6,8],found:6,framework:[2,6,7,8],frequent:6,from:[1,2,4,5,6,8],further:8,furthermor:[6,8],gain:8,gamebind:[2,4],gamecca:[2,4],gamecr:2,gameintctxt:[2,4],gamekr:[2,4],gamelr:[2,4],gameprf:[2,4],gameufcma:[2,4],gcd:[0,5],gener:[2,3,6,8],get:8,given:8,goal:6,good:[2,8],greater:[1,3],guess:2,guid:[7,8],h3110:1,half:5,hand:10,handl:8,hash:[1,2,6,8],hash_f:2,hashfunct:1,have:[0,1,2,6,8],hello:1,help:2,here:[2,6,10],hide:2,high:8,homework:8,hope:8,how:[2,3,6,8,10],howev:[2,6,8],http:5,idea:[6,8],ideal:6,impract:8,improv:8,includ:[6,8,10],ind_cpa:10,index:7,indic:[2,6],inform:[6,10],inherit:4,init:2,initi:2,input:2,instal:[],instanc:6,instanti:4,instead:[8,10],instructor:[6,8],int_to_str:[0,5],integ:5,integr:2,interact:[6,8],interfac:2,intern:2,intro:[],introduct:[],introductori:[7,8],inv:0,invers:5,join:[0,5],just:6,kei:[1,2,3,6,8],key_gen:1,key_guess:2,key_len:[1,2],keygen:3,knowledg:6,krsim:4,lack:8,larger:8,last:10,left:[2,4,10],len:[0,1,3,5],length:[0,1,2,3,5,6,8],level:8,like:[2,3,4,6],link:10,linux:10,list:10,locat:[0,8,10],lose:6,lost:2,lrsim:4,mac:[1,2,8,10],machin:10,made:[2,5],main:10,make:8,match:2,math:4,mean:0,meant:2,measur:2,member:2,menu:10,messag:[0,1,2,6,8],met:1,method:[2,6,8],might:6,mihir:8,mirror:6,mod:[0,5],mode:[3,10],model:8,modifi:10,modinv:[0,5],modul:0,modular:5,modulo:3,more:[2,6,8],motiv:8,much:6,multipl:[3,5],must:[1,2,3,10],name:10,navig:10,need:[0,2,6,7],next:[],none:[0,1,2,5,8],note:10,notebook:8,notion:6,num:[0,5],number:[5,6,8],object:[2,8],obtain:6,off:8,offer:8,often:8,onc:[2,8,10],onli:[2,8,10],open:8,oper:[5,8],option:[2,10],optional_length:0,oracl:[2,6],order:[0,2,6,8,10],otherwis:[1,2],our:[0,2,6,7,8],out_len:1,output:[1,2,10],over:4,overal:8,own:8,page:[7,10],pair:2,panel:10,param:2,paramet:[1,2,3,4,5,6],part:2,particular:[2,6,8],pass:[1,6],peculiar:6,per:2,perform:[0,4,6],philosophi:8,piec:6,plai:2,plain:[0,2],plaintext:[2,3],pleas:6,pop:10,portion:5,possibl:[6,8],postul:8,practic:8,pre:8,prf:2,primit:[0,1],print:[1,5],procedur:10,produc:2,professor:8,project:8,proper:1,provid:[4,8],pseduocod:0,pseudo:2,pseudocod:[0,8],pycharm:[],python:[0,2,5,6,7,8,10],quantiti:8,queri:[2,6],question:5,quick:7,quickli:8,quit:8,ran:10,rand:4,rand_str:0,random:[1,2,3],random_str:[1,3],random_string_bit:3,ratio:4,real:[2,4,6],receiv:2,recoveri:2,rememb:10,replac:10,repres:0,represent:5,requir:2,resembl:8,reset:2,resist:2,result:[1,2,5],right:[2,4,10],rsa:[3,4],rsa_keygen:3,run:[2,4,6],runnabl:8,same:[2,10],sampl:6,san:8,scheme:[1,2,6,8],scratch:8,search:7,second:[3,5],section:[6,10],secur:2,see:[1,2,6,8],select:[2,10],self:[1,2],sender:2,sent:2,seri:8,set:[2,6,8],sever:[0,6,8],should:[2,3,10],side:10,sign:1,signatur:[1,2,6,8],signific:8,similar:[8,10],simpli:1,simul:[1,2],site:8,size:[0,1,2,3,5,8],slide:2,slow:4,smaller:8,some:[2,5,6,8],sourc:[1,2,3,4,5,10],specif:4,split:5,stackoverflow:5,standard:3,start:[6,8],state:[2,6],storag:2,str:1,straightforward:8,string1:0,string2:0,string:[0,1,3,5],string_to_int:[0,5],strive:8,struggl:8,student:8,success:[2,4],successfulli:[2,10],superclass:2,suppli:[5,8],surfac:8,suspect:2,syntax:8,tabl:0,tag:[1,2],tag_len:1,take:[2,6],target:2,task:0,taught:8,templat:[6,8],termin:[],test:[1,2,8],text:[0,1,2,3],than:[1,3,4],thei:[2,6],themselv:6,theoret:[6,7,8],thi:[0,1,2,4,6],thing:[6,8],think:[2,6],those:0,thu:6,time:[2,4,8,10],togeth:[0,6],tool:0,top:10,total:4,total_run:4,toward:8,transform:8,tree:10,tri:4,trivial:8,troubl:8,turn:5,tutori:8,two:[0,2],type:[6,8],typic:6,ufcma:4,ufcmasim:4,unclear:8,under:2,understand:8,univers:8,unzip:10,usag:1,user:8,usual:[2,4],valid:2,valu:3,veri:10,verif:[1,2],verifi:[1,2,8],version:6,via:2,vim:10,w0r1d:1,wai:[6,7,8],want:2,well:[2,5,8],were:8,what:[],when:[2,8],where:2,whether:2,which:[2,4,6,7,8],who:8,why:[],win:[2,6],window:10,winter:8,wish:[4,10],within:8,without:1,won:2,work:[6,8,10],world:[1,2,4,6],worldsim:[2,4],worri:6,would:[2,3,4,8],written:4,x00:0,xff:0,xor:5,xor_str:[0,5],xore:0,yet:8,you:[0,1,2,3,4,6,7,10],your:10,zip:10},titles:["Conventions","crypto.abstract package","crypto.games package","crypto.primitives module","crypto.simulator package","crypto.tools module","Design and Architecture","Welcome to 207project&#8217;s documentation!","Intro","&lt;no title&gt;","Getting Started"],titleterms:{"207project":7,"abstract":[1,6],architectur:6,assign:10,base_sim:4,bind_sim:4,blank:10,block_ciph:1,cca_sim:4,content:[1,2,4],convent:0,cr_sim:4,creat:[8,10],crypto:[1,2,3,4,5],cryptographi:6,ctxt_sim:4,deliver:8,design:6,did:8,digital_signatur:1,document:7,download:10,edit:10,from:10,game:[2,6],game_bind:2,game_cca:2,game_cr:2,game_int_ctxt:2,game_kr:2,game_lr:2,game_prf:2,game_ufcma:2,get:10,goal:8,hash_funct:1,indic:7,instal:10,intro:8,introduct:10,kr_sim:4,librari:6,lr_sim:4,message_authentication_cod:1,modul:[1,2,3,4,5,10],next:8,open:10,packag:[1,2,4],primit:3,project:10,pycharm:10,run:10,sampl:10,simul:[4,6],start:10,submodul:[1,2,4],tabl:7,termin:10,thi:8,tool:5,ufcma_sim:4,welcom:7,what:8,why:8,world_sim:4}})